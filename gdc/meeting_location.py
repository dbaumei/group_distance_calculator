from .address import Address
import openrouteservice as ors


class MeetingLocation(Address):
    """Store information about a meeting location. Is a subclass of ``Address``.

    Attributes:
        COUNTRY (str): Default country for the meeting location's address.

    """

    COUNTRY = "Germany"

    def __str__(self):
        """Return string representation of the ``MeetingLocation`` class."""
        return f"MeetingLocation: {self.name}, {self.city}"

    def __init__(self, client: ors.Client, line: str):
        """Store information about a meeting location.

        Args:
            client: Client to perform the API queries with.
            line: Line of data from NDJSON of meeting locations.

        Raises:
            ValueError: If city is empty.

        """
        super().__init__(client, line)

        self.country = MeetingLocation.COUNTRY
        self.address = self._combineInfoToAddress()
