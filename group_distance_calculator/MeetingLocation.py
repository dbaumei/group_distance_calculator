import openrouteservice as ors
import json
import re

class MeetingLocation:

    COUNTRY = "Germany"

    def __init__(self, client: ors.Client, line: str):
        """Store information about a meeting location.

        Args:
            client (ors.Client): Client to perform the API queries with.
            line (str): Line of data from NDJSON if meeting locations.

        Raises:
            ValueError: If city is empty.

        """
        raw_data = json.loads(line)

        if not raw_data['city']:
            raise ValueError("city must not be empty.")

        self.name = raw_data['name']
        self.city = raw_data['city']
        self.postal_code = raw_data['postal_code'] if re.fullmatch(r"[\s\w]+", raw_data['postal_code']) else ""
        self.street = raw_data['street'] if re.fullmatch(r"[\w\s]+", raw_data['street']) else ""
        self.housenumber = raw_data['housenumber'] if re.fullmatch(r"\d+\s*\w*", raw_data['housenumber']) else ""
        self.client = client

        if self.street:
            if self.housenumber:
                self.adress = f"{self.street} {self.housenumber}, {self.city}, {MeetingLocation.COUNTRY}"
            else:
                self.adress = f"{self.street}, {self.city}, {MeetingLocation.COUNTRY}"
        else:
            self.adress = f"{self.city}, {MeetingLocation.COUNTRY}"

        self.geocode = []


    def getGeocode(self):
        """Fetch the meeting locations geocode.

        Returns:
            Tuple: Float values of longitude and latitude.

        """
        if not self.geocode:

            pelias_search_result = self.client.pelias_search(text = f"{self.adress}", size = 1)
            self.geocode = pelias_search_result['features'][0]['geometry']['coordinates']

        return self.geocode


    def __str__(self):
        return f"MemMeetingLocation: {self.name}: {self.city}"
