import json
import openrouteservice as ors
import re


class Address:
    """Store information about a location. This is a base class and not meant to be implemented directly."""

    def __init__(self, client: ors.Client, line: str):
        """Implement the ``Address`` class.

        Args:
            client: Client to perform the API queries with.
            line: Line of data from NDJSON with address information.

        Raises:
            ValueError: If city is empty.

        """
        self.client = client

        raw_data = json.loads(line)
        if not raw_data['city']:
            raise ValueError("city must not be empty.")

        self.name = raw_data['name'] if raw_data['name'] else "Unnamed"
        self.city = raw_data['city']
        self.postal_code = raw_data['postal_code'] if re.fullmatch(r"[\s\w]+", raw_data['postal_code']) else ""
        self.street = raw_data['street'] if re.fullmatch(r"[\w\s]+", raw_data['street']) else ""
        self.housenumber = raw_data['housenumber'] if re.fullmatch(r"\d+\s*\w*", raw_data['housenumber']) else ""

        self.geocode = []


    def getGeocode(self):
        """Fetch the meeting locations geocode.

        Returns:
            Tuple: Float values of longitude and latitude.

        """
        # Save as member variable to minimize the number of calls to the API
        if not self.geocode:
            pelias_search_result = self.client.pelias_search(text = f"{self.address}", size = 1)
            self.geocode = pelias_search_result['features'][0]['geometry']['coordinates']

        return self.geocode


    def _combineInfoToAddress(self):
        """Take the information initialized during the construction of the object and combine it to an address-like string.

        Returns:
            str: Address formatted as Street Housenumber, Postalcode City, Country

        """
        if self.street:
            if self.housenumber:
                address = f"{self.street} {self.housenumber}, {self.city}, {self.country}"
            else:
                address = f"{self.street}, {self.city}, {self.country}"
        else:
            address = f"{self.city}, {self.country}"

        return address
