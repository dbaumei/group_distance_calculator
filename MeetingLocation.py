import openrouteservice as ors
import json
from statistics import mean

class MeetingLocation:

    def __init__(self, city: str, street: str = "", house_number: int = 0, country: str = "Germany"):

        # Bare minimum: city must be defined
        if city == "":
            raise ValueError("city must not be empty.")

        self.city = city
        self.street = street
        self.house_number = house_number

        if street != "":
            if house_number > 0:
                self.adress = f"{street} {house_number}, {city}, {country}"
            else:
                self.adress = f"{street}, {city}, {country}"
        else:
            self.adress = f"{city}, {country}"

    def getGeocode(self, client: ors.Client):
        pelias_search_result = client.pelias_search(text = self.adress)
        bbox = pelias_search_result['bbox']
        lon = mean([bbox[0], bbox[2]])
        lat = mean([bbox[1], bbox[3]])
        self.geocode = [lon, lat]
        return self.geocode
