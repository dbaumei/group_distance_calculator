from .address import Address
import openrouteservice as ors


class Member(Address):
    """Store information about a member. Is a subclass of ``Address``.

    Attributes:
        COUNTRY (str): Default country for the member's address.
    """

    # Default country is Germany to simplify the input data. Maybe add a configuration file to make this adjustable.
    COUNTRY = "Germany"

    def __str__(self):
        """Return string representation of the Member class."""
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
