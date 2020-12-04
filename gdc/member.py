from .address import Address
import openrouteservice as ors


class Member(Address):

    COUNTRY = "Germany"

    def __str__(self):
        return f"Member: {self.name}, {self.city}"

    def __init__(self, client: ors.Client, line: str):
        """Store information about a member location.

        Args:
            client (ors.Client): Client to perform the API queries with.
            line (str): Line of data from NDJSON of members.

        Raises:
            ValueError: If city is empty.

        """
        super().__init__(client, line)

        self.country = Member.COUNTRY
        self.address = self._combineInfoToAddress()
