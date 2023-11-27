# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 00:11:00 2023

@author: Windows
"""

import requests
import pandas as pd

# Store your API key
api_key = '0pmQVfEfNT9dsWyGShqhbdbuvUvtIUfcHRuxkPmc'

# Make a request to the NEO API endpoint
neo_url = f'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key={api_key}'
response = requests.get(neo_url)

if response.status_code == 200:
    data = response.json()
    # Process the retrieved data to extract asteroid information
    asteroids = []
    for asteroid in data['near_earth_objects']:
        asteroid_data = {
            'Asteroid ID': asteroid['id'],
            'Asteroid name': asteroid['name'],
            'Minimal estimated diameter (km)': asteroid['estimated_diameter']['kilometers']['estimated_diameter_min'],
            'Absolute magnitude': asteroid['absolute_magnitude_h'],
            'Relative velocity (km/s)': asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_second']
        }
        asteroids.append(asteroid_data)
    
    # Create a Pandas DataFrame
    asteroids_df = pd.DataFrame(asteroids)
    print(asteroids_df.head())  # Displaying the first few rows of the DataFrame

    # Export DataFrame to CSV
    asteroids_df.to_csv('asteroids_data.csv', index = False)
else:
    print("Failed to fetch NEO data:", response.status_code)
    



    
    
