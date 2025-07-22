import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

def create_driver():
    """Initialize and return a headless Chrome webdriver."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

def open_panel(driver) -> bool:
    """Click the 'Subset / Get Data' button to open the data panel."""
    try:
        open_panel_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-gtm-tag="Subset / Get Data"]'))
        )
        open_panel_btn.click()
        print('Open Panel Button "Subset / Get Data" clicked successfully!')
        return True
    except Exception as e:
        print(f"Error opening panel: {e}")
        return False

def click_get_data(driver) -> bool:
    """Click the 'Get Data' button in the modal/panel."""
    try:
        get_data_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-success.modal-footer-btn'))
        )
        get_data_btn.click()
        print("Get Data Button clicked successfully")
        return True
    except Exception as e:
        print(f"Error clicking 'Get Data' button: {e}")
        return False

def get_data(file_extension: str, driver) -> str:
    """
    Parse the page to find the latest download link with given file extension.
    Returns the link URL or empty string if not found.
    """
    try:
        readme_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH,  "//a[contains(@download, 'README Document')]"))
        )
        if readme_link:
            print('README link found!')
        else:
            print('README link not found!')

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a', {'class': ['word-wrap', 'ng-binding']}) if link.get('href') and link.get('href').endswith(file_extension)]

        if not links:
            print(f'No {file_extension} file links found.')
            return ''

        latest_link = links[0]
        print("Latest file link:", latest_link)
        return latest_link

    except Exception as e:
        print(f"Error getting data link: {e}")
        return ''

def download_data(link: str, token: str) -> str:
    """Download the file from the given link using token authorization and save to `data` folder."""
    if not link:
        raise ValueError("No download link provided.")

    download_folder = 'data'
    os.makedirs(download_folder, exist_ok=True)
    filename = os.path.join(download_folder, os.path.basename(link))

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(link, allow_redirects=True, headers=headers)
    response.raise_for_status()

    with open(filename, 'wb') as f:
        f.write(response.content)

    print('File downloaded successfully!')
    print(filename)
    return filename

def scrape() -> str:
    """
    Main scraping function:
    - Loads the NASA data page
    - Opens the data panel
    - Clicks get data
    - Finds the latest .nc4 link
    - Downloads the file with token authorization
    Returns the filename of the downloaded file.
    """
    token = os.getenv('EARTHDATA_TOKEN')
    if not token:
        raise EnvironmentError("EARTHDATA_TOKEN environment variable is not set.")

    driver = create_driver()

    try:
        url = 'https://disc.gsfc.nasa.gov/datasets?keywords=GLDAS&sort=endDate&page=1'
        driver.get(url)

        if not open_panel(driver):
            raise RuntimeError("Failed to open data panel.")

        if not click_get_data(driver):
            raise RuntimeError("Failed to click Get Data button.")

        link = get_data('.nc4', driver)
        if not link:
            raise RuntimeError("No valid data file link found.")

        filename = download_data(link, token)
        return filename

    finally:
        driver.quit()
