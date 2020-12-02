import openrouteservice as ors
import json
# from statistics import mean
import re

class Member:

    COUNTRY = "Germany"

    def __init__(self, client: ors.Client, line: str):
        raw_data = json.loads(line)

        if not city:
            raise ValueError("city must not be empty.")

        self.name = raw_data['name']
        self.city = raw_data['city']
        self.postal_code = raw_data['postal_code'] if re.fullmatch(r"[\s\w]+", raw_data['postal_code']) else ""
        self.street = raw_data['street'] if re.fullmatch(r"[\w\s]+", raw_data['street']) else ""
        self.housenumber = raw_data['housenumber'] if re.fullmatch(r"\d+\s*\w*", raw_data['housenumber']) else ""
        self.client = client

        self.geocode = []

    def getGeocode(self):
        if not self.geocode:

            pelias_search_result = self.client.pelias_search(text = f"{self.postal_code} {self.city}, {Member.COUNTRY}", size = 1)
            # bbox = pelias_search_result['bbox']
            # lon = mean([bbox[0], bbox[2]])
            # lat = mean([bbox[1], bbox[3]])
            # self.geocode = [lon, lat]
            self.geocode = pelias_search_result['features'][0]['geometry']['coordinates']

        return self.geocode

    def __str__(self):
        return f"Member: {self.name}: {self.city}"
