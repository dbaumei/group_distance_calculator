from ..group_distance_calculator import MeetingLocation
import pytest_check as check


def test_it_parses_correct_input_correctly(ors_client):
    # Setup
    correct_location_line = r'{"name": "Haus der Musik", "city": "Heiden", "postal_code": "46359", "street": "Am Sportzentrum", "housenumber": "7"}'

    subject = MeetingLocation.MeetingLocation(ors_client, correct_location_line)

    # Test
    check.equal(subject.name, "Haus der Musik")
    check.equal(subject.city, "Heiden")
    check.equal(subject.postal_code, "46359")
    check.equal(subject.street, "Am Sportzentrum")
    check.equal(subject.housenumber, "7")


def test_it_sets_invalid_input_to_an_empty_string(ors_client):
    incorrect_location_line = r'{"name": "Haus der Mus1k", "city": "Heiden", "postal_code": "-", "street": "Am ~Sportzentrum", "housenumber": "§89"}'
    subject = MeetingLocation.MeetingLocation(ors_client, incorrect_location_line)

    check.equal(subject.name, "Haus der Mus1k")
    check.equal(subject.city, "Heiden")
    check.equal(subject.postal_code, "")
    check.equal(subject.street, "")
    check.equal(subject.housenumber, "")

def test_it_returns_a_valid_geocode(ors_client):
    # Setup
    correct_location_line = r'{"name": "Haus der Musik", "city": "Heiden", "postal_code": "46359", "street": "Am Sportzentrum", "housenumber": "7"}'
    subject = MeetingLocation.MeetingLocation(ors_client, correct_location_line)

    # Test
    check.almost_equal([6.9342899, 51.8213412], subject.getGeocode())
