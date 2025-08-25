import requests
import pandas as pd
from io import BytesIO

# URL of the Excel file containing approved mobile camera locations
excel_url = "https://www.vic.gov.au/sites/default/files/2024-10/Mobile-Camera-Locations-November-2024.xlsx"

# Send a GET request to download the Excel file
response = requests.get(excel_url)
response.raise_for_status()  # Check for request errors

# Read the Excel file into a pandas DataFrame
excel_data = pd.read_excel(BytesIO(response.content))

# Save the DataFrame to a CSV file
csv_filename = "Approved_Mobile_Camera_Locations_November_2024.csv"
excel_data.to_csv(csv_filename, index=False)

print(f"Data has been saved to {csv_filename}")