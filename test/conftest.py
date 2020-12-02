import openrouteservice as ors
from os import path
import pytest


@pytest.fixture
def ors_client() -> ors.Client:
    """Implements an open route service client.
    Needs to have a valid path to an API token text file.

    Yields:
        An open route service client.

    """
    key_path = "./ors.key"
    ors_api_key = ""
    with open(path.abspath(key_path)) as key_file:
        ors_api_key = key_file.readline().strip()

    yield ors.Client(ors_api_key)
