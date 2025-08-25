import requests
import pandas as pd

# Google Maps API Key
API_KEY = # Insert API KEY Here

# # Function to fetch coordinates for a street in a specific suburb
# def get_coordinates(street, suburb):
#     address = f"{street}, {suburb}, Victoria, Australia"
#     url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
#     response = requests.get(url)
#     data = response.json()

#     if data['status'] == 'OK':
#         location = data['results'][0]['geometry']['location']
#         return location['lat'], location['lng']
#     else:
#         print(f"Error fetching data for {address}: {data['status']}")
#         return None, None
# import requests

def get_coordinates(street_name, suburb_name, api_key):
    # Format the address
    address = f"{street_name}, {suburb_name}, Victoria, Australia"
    
    # Send request to Google Maps Geocoding API
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    # Check if the request was successful
    if data['status'] == 'OK':
        results = data['results']
        if results:
            # Get the coordinates of the first and last points of the street
            try:
                northeast = results[0]['geometry']['bounds']['northeast']
                southwest = results[0]['geometry']['bounds']['southwest']
            except KeyError:
                print(results[0])
            return northeast, southwest
        else:
            return None
    else:
        return None


# Load the data (Assuming the data has columns 'Street' and 'Suburb')
data = pd.read_csv("Approved_Mobile_Camera_Locations_November_2024.csv", header=1)

# Add new columns for coordinates
data['Start_Lat'], data['Start_Lng'] = None, None
data['End_Lat'], data['End_Lng'] = None, None

# Loop through the rows and fetch coordinates
for index, row in data.iterrows():
    street = row['LOCATION']
    suburb = row['SUBURB']
    
    # Get Northeast and Southwest coordinates
    northeast, southwest = get_coordinates(street, suburb, API_KEY)

    # Set start coordinates (first end of the street)
    data.at[index, 'Start_Lat'] = northeast['lat']
    data.at[index, 'Start_Lng'] = northeast['lng']
    
    # Set end coordinates (second end of the street)
    data.at[index, 'End_Lat'] = southwest['lat']
    data.at[index, 'End_Lng'] = southwest['lng']

# Save the data with coordinates to a new CSV
output_csv = "Streets_With_Coordinates.csv"
data.to_csv(output_csv, index=False)


print(f"Data with coordinates saved to {output_csv}")
