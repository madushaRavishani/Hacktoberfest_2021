#Import libraries
import googlemaps
import pandas as pd

#Get a googlemaps object
gmaps = googlemaps.Client(key='your API key')

#Get place details
place_name = 'The Fab'
place_details = gmaps.places(place_name)
place_details

#Get place Id
place_details['results'][0]['place_id']

#Get Google Reviews
place = gmaps.place('ChIJmxoAhvdX4joR9aZdwt5FjgE')
place['result']['reviews']
