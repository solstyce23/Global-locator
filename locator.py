import webbrowser
import logging
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.extra.rate_limiter import RateLimiter
import folium
from folium import IFrame
import os

# Initialize logging
logging.basicConfig(filename='location_queries.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Initialize the geolocator
geolocator = Nominatim(user_agent="global_locator")

# Add rate limiter to avoid hitting API too frequently
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Function to locate a place with detailed information and handle errors
def locate_place(place_name, language="en", radius=1000):
    try:
        # Get the location data
        location = geocode(place_name, language=language, timeout=10)

        if not location:
            print("❌ No results found. Try a more precise name or check your internet connection.")
            return None

        # Extract data from location object
        latitude = location.latitude
        longitude = location.longitude
        address = location.address
        country = location.raw.get('address', {}).get('country', 'Unknown')
        state = location.raw.get('address', {}).get('state', 'Unknown')
        city = location.raw.get('address', {}).get('city', 'Unknown')

        # Log the query for later reference
        logging.info(f"Query: {place_name}, Address: {address}, Latitude: {latitude}, Longitude: {longitude}")

        # Print information
        print(f"📍 Location found: {place_name}")
        print(f"🗺️ Address: {address}")
        print(f"🌐 Coordinates: {latitude}, {longitude}")
        print(f"🌎 Country: {country}, State: {state}, City: {city}")
        
        # Generate Google Maps link
        maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        print(f"🔗 Google Maps link: {maps_url}")
        
        # Open Google Maps in a web browser
        webbrowser.open(maps_url)

        # Create a map and place a marker
        m = folium.Map(location=[latitude, longitude], zoom_start=12)
        folium.Marker([latitude, longitude], popup=IFrame(f"<strong>{place_name}</strong><br>{address}", width=250, height=100)).add_to(m)

        # Save map to HTML file
        map_filename = "location_map.html"
        m.save(map_filename)
        print(f"📍 A map has been saved as {map_filename}")

        # Open the map in the browser
        webbrowser.open(map_filename)

    except GeocoderTimedOut:
        print("❌ Geocoding service timed out. Please try again later.")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")


# Function to get user input and invoke the locator
def main():
    print("Welcome to the Global Locator! 🌍")
    
    # Prompt user for place name and optional parameters
    place_name = input("Enter a place to locate: ")
    language = input("Enter the language code (default is 'en'): ") or 'en'
    radius = input("Enter a search radius in meters (default is 1000m): ") or 1000

    try:
        radius = int(radius)
    except ValueError:
        print("⚠️ Invalid radius input. Defaulting to 1000 meters.")
        radius = 1000
    
    print("🔎 Locating the place...")
    locate_place(place_name, language, radius)

if __name__ == "__main__":
    main()
