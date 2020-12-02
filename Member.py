import openrouteservice as ors
import json
from statistics import mean

class Member:

    COUNTRY = "Germany"

    def __init__(self, client: ors.Client, line: str):
        raw_data = json.loads(line)

        self.name = raw_data['name']
        self.city = raw_data['city']
        self.postal_code = raw_data['postal_code']
        self.street = raw_data['street']
        self.house_number = raw_data['house_number']
        self.client = client

        self.geocode = []

    def getGeocode(self):
        if not self.geocode:
            pelias_search_result = self.client.pelias_search(text = f"{self.city}, {Member.COUNTRY}", size = 1)
            # bbox = pelias_search_result['bbox']
            # lon = mean([bbox[0], bbox[2]])
            # lat = mean([bbox[1], bbox[3]])
            # self.geocode = [lon, lat]
            self.geocode = pelias_search_result['features'][0]['geometry']['coordinates']

        return self.geocode

    def __str__(self):
        return f"Member: {self.name}: {self.city}"
