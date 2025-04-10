# Global-locator 
# Global-locator
# 🌍 Global Locator with Map Visualization and Advanced Features

> A Python script to locate any place in the world, show its full geographic details, and open its exact point in Google Maps 🌐

---

## 🚀 What It Does

**Global Locator** is a complex geolocation utility that:

- 🏙️ Accepts any location or city name as input
- 📡 Uses the `geopy` library and the Nominatim API to fetch precise location data
- 📍 Outputs coordinates (latitude & longitude)
- 🧭 Displays the full address associated with the point
- 🌎 Returns additional location details like country, state, and city
- 🔗 Generates and opens a Google Maps link with a direct marker
- 🗺️ Visualizes the location on an interactive map using `folium`
- 📜 Logs queries for future reference

---

## 🧠 How It Works (Behind the Scenes)

This script uses:

1. **Nominatim + `geopy`**:  
   Powered by OpenStreetMap, Nominatim allows detailed geocoding using place names. We use `RateLimiter` from `geopy.extra` to avoid hitting API limits and respect terms of service.

2. **Data Extraction**:  
   From the response, we extract:
   - `latitude`
   - `longitude`
   - `address`
   - `country`, `state`, and `city`

3. **Google Maps Link**:  
   We format a query with:

Then we use Python’s `webbrowser` module to instantly open this link in your default browser.

4. **Map Visualization**:  
The script uses the `folium` library to create an interactive map, adding a marker for the specified location. The map is saved as an HTML file and opened directly in the browser.

5. **Logging**:  
All user queries are logged into `location_queries.log` for later reference, making it easy to track past searches.

---

## 🧰 Requirements

Install dependencies with:

```bash
pip install geopy folium

$ python complex_locator.py
Enter a place to locate: Tokyo
Enter the language code (default is 'en'): en
Enter a search radius in meters (default is 1000m): 1000

📍 Location found: Tokyo
🗺️ Address: Tokyo, Kantō, Japan
🌐 Coordinates: 35.6828387, 139.7594549
🌎 Country: Japan, State: Kantō, City: Tokyo
🔗 Google Maps link: https://www.google.com/maps?q=35.6828387,139.7594549
📍 A map has been saved as location_map.html

Made with ❤️ by Solstyce

