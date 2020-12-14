from gdc import GroupDistanceCalculator
import pytest_check as check


def test_it_initializes(ors_client, member_list, meeting_location_list):
    subject = GroupDistanceCalculator(ors_client, member_list, meeting_location_list)

def test_it_fetches_a_time_distance_matrix(ors_client, member_list, meeting_location_list):
    subject = GroupDistanceCalculator(ors_client, member_list, meeting_location_list)

    matrix = subject.getMatrix()
    check.greater(len(matrix['durations']), 0)
    check.greater(len(matrix['distances']), 0)


def test_it_calculates_total_times_in_min(ors_client, member_list, meeting_location_list):
    subject = GroupDistanceCalculator(ors_client, member_list, meeting_location_list)

    test_matrix = {'durations': [[300, 600, 900], [120, 180, 1080]]}
    sums = [30.0, 23.0]

    result = subject.totalTimes(test_matrix)

    check.almost_equal(result, sums, rel=0.001)

def test_it_calculates_total_distances_in_km(ors_client, member_list, meeting_location_list):
    subject = GroupDistanceCalculator(ors_client, member_list, meeting_location_list)

    pass

def test_it_gets_total_time_and_distance(ors_client, member_list, meeting_location_list):
    subject = GroupDistanceCalculator(ors_client, member_list, meeting_location_list)

    pass
