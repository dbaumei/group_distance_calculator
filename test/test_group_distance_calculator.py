from gdc import GroupDistanceCalculator
import pytest_check as check


def test_it_initializes(ors_client, member_list, meeting_location_list):
    subject = GroupDistanceCalculator(ors_client, member_list, meeting_location_list)

def test_it_fetches_a_time_distance_matrix(ors_client, member_list, meeting_location_list):
    subject = GroupDistanceCalculator(ors_client, member_list, meeting_location_list)

    matrix = subject.getMatrix()
    check.greater(len(matrix['durations']), 0)
    check.greater(len(matrix['distances']), 0)


def test_it_calculates_total_times_in_min(ors_client):
    subject = GroupDistanceCalculator(ors_client, [], [])

    test_matrix = {'durations': [[300, 600, 900], [120, 180, 1080]]}
    sums_minutes = [7.0, 13.0, 33.0]
    result = subject.totalTimes(test_matrix)

    check.almost_equal(result, sums_minutes, rel=0.001)

def test_it_calculates_total_distances_in_km(ors_client):
    subject = GroupDistanceCalculator(ors_client, [], [])

    test_matrix = {'distances': [[4600.0, 1300.0], [1000.0, 2000.0], [5000.0, 7000.0]]}
    sums_km = [11.0, 10.0]
    result = subject.totalDistances(test_matrix)

    check.almost_equal(result, sums_km, rel=0.001)

# This test is not really necessary. The function only collects the output of other functions.
# Just making sure it does not crash.
def test_it_gets_total_times_and_distances(ors_client, member_list, meeting_location_list):
    subject = GroupDistanceCalculator(ors_client, member_list, meeting_location_list)

    result = subject.getTotals()
    check.is_not_none(result['times'])
    check.is_not_none(result['distances'])
