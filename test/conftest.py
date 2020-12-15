from gdc import MeetingLocation, Member
import openrouteservice as ors
from os import path
import pytest
from typing import List


@pytest.fixture
def ors_client() -> ors.Client:
    """Implement an open route service client. Needs to have a valid path to an API token text file.

    Yields:
        An open route service client.

    """
    key_path = "./ors.key"
    ors_api_key = ""
    with open(path.abspath(key_path)) as key_file:
        ors_api_key = key_file.readline().strip()

    yield ors.Client(ors_api_key)

@pytest.fixture
def meeting_location_list(ors_client) -> List:
    """Generate test data.

    Returns:
        List of meeting locations.

    """
    test_locations = [r'''{"name": "", "city": "Bocholt", "postal_code": "46395", "street": "Anholter Postweg", "housenumber": "3"}''',
    r'''{"name": "", "city": "Raesfeld", "postal_code": "", "street": "", "housenumber": ""}''',
    r'''{"name": "", "city": "Suedlohn", "postal_code": "", "street": "", "housenumber": ""}''']

    meeting_locations = [MeetingLocation(ors_client, line) for line in test_locations]
    return meeting_locations

@pytest.fixture
def member_list(ors_client) -> List:
    """Generate test data.

    Returns:
        List of members.

    """
    test_members = [r'''{"name": "Lukas", "city": "Raesfeld", "postal_code": "", "street": "", "housenumber": ""}''',
    r'''{"name": "Vincent", "city": "Bocholt", "postal_code": "", "street": "", "housenumber": ""}''']
    members = [Member(ors_client, line) for line in test_members]
    return members
