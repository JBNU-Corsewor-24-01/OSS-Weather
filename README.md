
# Project Overview

This project processes location and weather data, converts geographical coordinates, and visualizes the data on a map of South Korea.


# Reference Site

   - https://www.data.go.kr/data/15084084/openapi.do
   - https://mkjjo.github.io/python/2019/08/18/korea_population.html


## Directory Structure

```
project/
│
├── output/
│   ├── LOC_CODE_WEATHER_EUC_KR.csv
│   ├── LOC_CODE_WEATHER_UTF8.csv
│   └── tmp/
│
├── static/
│   └── resource/
│       ├── LOC_CODE_EUC_KR.csv
│       ├── LOC_CODE_UTF8.csv
│       └── TL_SCCO_SIG_WGS84.json
│
├── util/
│   ├── __init__.py
│   ├── ParseGeoInfo.py
│   └── Weather.py
│
├── .gitignore
├── folium_kr.html
├── main.py
└── prepare.py
```

## Files and Their Usage

### CSV Files

- `LOC_CODE_EUC_KR.csv`: Contains location codes with coordinates in EUC-KR encoding.
- `LOC_CODE_UTF8.csv`: Contains location codes with coordinates in UTF-8 encoding.
- `LOC_CODE_WEATHER_EUC_KR.csv`: Output file with weather data in EUC-KR encoding.
- `LOC_CODE_WEATHER_UTF8.csv`: Output file with weather data in UTF-8 encoding.

### JSON File

- `TL_SCCO_SIG_WGS84.json`: Contains geographical shape data for visualization.

## How to Use

1. **Prepare the data:**
   - Ensure the `LOC_CODE_EUC_KR.csv` file is in the `./static/resource/` directory.
   - Run the `prepare.py` script to process the location data, convert coordinates, fetch weather data, and save the results in the `./output/` directory.

2. **Visualize the data:**
   - Ensure the `TL_SCCO_SIG_WGS84.json` file is in the `./static/resource/` directory.
   - Run the `main.py` script to create a choropleth map based on the processed data.
   - The generated map will be saved as `folium_kr.html` and will automatically open in your default web browser.

## Dependencies

- pandas
- folium
- requests
- tqdm

## Setup

1. Install the required dependencies using pip:
   ```
   pip install pandas folium requests tqdm
   ```
2. Update the `service_key` and `base_url` in `Weather.py` with your API key and the base URL for the weather service.

## Notes

- Ensure that the API service key and base URL are correctly set up in `Weather.py`.
- The scripts rely on specific file paths for input and output. Ensure the directory structure is maintained as provided.
