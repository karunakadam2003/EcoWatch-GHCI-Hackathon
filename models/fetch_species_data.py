# fetch_species_data.py
import requests

def fetch_species_data(latitude, longitude, radius=5, limit=10):
    """Fetch endangered species occurrence data from GBIF API."""
    url = "https://api.gbif.org/v1/occurrence/search"
    params = {
        "decimalLatitude": latitude,
        "decimalLongitude": longitude,
        "radius": radius,
        "threatened": True,  # Optional: Only fetch endangered/threatened species if available
        "hasCoordinate": True,
        "limit": limit  # Adjust the limit as needed
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        results = response.json().get('results', [])
        species_list = [species.get('scientificName', 'Unknown Species') for species in results]
        return species_list
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

if __name__ == "__main__":
    # Example coordinates
    latitude = 34.0522  # Los Angeles
    longitude = -118.2437
    species = fetch_species_data(latitude, longitude)
    print("Fetched species:", species)

