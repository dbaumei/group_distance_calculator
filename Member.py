import openrouteservice as ors
import json
from statistics import mean

class Member:

    def __init__(self, name: str, city: str):
        self.name = name
        self.city = city
    
    def getGeocode(self, client: ors.Client):
        pelias_search_result = client.pelias_search(text = f"{self.city}, Germany", size = 1)
        # bbox = pelias_search_result['bbox']
        # lon = mean([bbox[0], bbox[2]])
        # lat = mean([bbox[1], bbox[3]])
        # self.geocode = [lon, lat]
        self.geocode = pelias_search_result['features'][0]['geometry']['coordinates']
        return self.geocode
        