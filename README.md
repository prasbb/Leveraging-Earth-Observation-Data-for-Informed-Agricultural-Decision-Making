# AgriSphere

**Leveraging Earth Observation Data for Informed Agricultural Decision-Making**  
_A submission for the 2024 NASA Space Apps Challenge (October 5–6, 2024)_

AgriSphere is a full-stack web platform designed to empower farmers with access to NASA Earth observation data in an intuitive and actionable way. Our goal was to help agricultural communities facing water-related challenges—such as droughts, floods, and unpredictable weather—by translating complex satellite datasets into visual and conversational insights.

This project was developed for the 2024 NASA Space Apps Challenge under the theme of using satellite and geospatial data to support water-focused agricultural decision-making.

---

## Features

- **Geospatial Visualization**  
  Interactive visualization of `.nc4` and `.csv` datasets using tools like GeoViews, HoloViews, Xarray, and Cartopy.

- **AgriAI Chatbot**  
  A custom assistant powered by OpenAI’s GPT-3.5 Turbo, fine-tuned on NASA datasets and our project’s architecture to answer agricultural questions using Earth data.

- **Automated NASA Data Updates**  
  A custom-built web scraper integrates live updates from NASA APIs and the Earth Observatory Natural Event Tracker (EONET), ensuring data is refreshed in sync with NASA’s publication frequency.

- **User-Friendly Interface**  
  Built with React, Flask, and Node.js, our frontend presents clean, interactive maps and chat interfaces to support non-technical users.

---

## Technologies Used

**Languages:** Python, JavaScript, HTML, CSS  
**Frameworks:** Flask, React, Node.js  
**Libraries and Tools:**
- `Xarray`, `GeoViews`, `HoloViews`, `Cartopy`, `Matplotlib`, `Pandas`, `netCDF4`, `Bokeh`
- `requests`, `BeautifulSoup`, `selenium`, `os`
- OpenAI GPT-3.5 Turbo API
- `Leaflet`, `Chat-UI`

**APIs:**  
- NASA EarthData (GES DISC)  
- NASA Earth Observatory Natural Event Tracker (EONET)

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/prasbb/Leveraging-Earth-Observation-Data-for-Informed-Agricultural-Decision-Making.git
