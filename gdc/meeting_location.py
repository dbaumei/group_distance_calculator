from .address import Address
import openrouteservice as ors


class MeetingLocation(Address):

    COUNTRY = "Germany"

    def __str__(self):
        return f"MeetingLocation: {self.name}, {self.city}"

    def __init__(self, client: ors.Client, line: str):
        """Store information about a meeting location.

        Args:
            client (ors.Client): Client to perform the API queries with.
            line (str): Line of data from NDJSON of meeting locations.

        Raises:
            ValueError: If city is empty.

        """
        super().__init__(client, line)

        self.country = MeetingLocation.COUNTRY
        self.address = self._combineInfoToAddress()
