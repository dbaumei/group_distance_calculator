import json
from .meeting_location import MeetingLocation
from .member import Member
import openrouteservice as ors
# Import the distance matrix separately to get the annotations in the IDE
from openrouteservice.distance_matrix import distance_matrix
from typing import Dict, List


class GroupDistanceCalculator:
    """TBD

    """
    def __init__(self, client: ors.Client, members: List[Member], meeting_locations: List[MeetingLocation]):
        """Implement the GroupDistanceCalculator class.

        Args:
            client: Client to query the ORS API with.
            members: List of members of the group.
            meeting_locations: List of meeting locations the combined distance should be calculated for.

        """
        self.client = client
        self.members = members
        self.meeting_locations = meeting_locations


    def getMatrix(self) -> distance_matrix:
        """Take the geocodes of members and meeting locations and fetches the time/distance matrix.

        """
        locations = [member.getGeocode() for member in self.members]
        locations.extend([meeting_location.getGeocode() for meeting_location in self.meeting_locations])

        member_indices = [i for i in range(len(self.members))]
        meeting_location_indices = [i + member_indices[-1] + 1 for i in range(len(self.meeting_locations))]

        matrix = distance_matrix(self.client,
                                locations=locations,
                                metrics=['distance', 'duration'],
                                sources=member_indices,
                                destinations=meeting_location_indices
                                )
        return matrix


    def totalTimes(self, matrix: distance_matrix) -> List[float]:
        """Calculate the total times it takes all members to reach each meeting location.

        Args:
            matrix: Time/distance matrix.

        Returns:
            List: Times in minutes (rounded).

        """
        times = matrix['durations']
        sums = [0.0] * len(times[0])

        for sublist_index in range(len(times)):
            for element_index in range(len(times[0])):
                sums[element_index] += times[sublist_index][element_index]

        total_times_minutes = [round(element / 60.0) for element in sums]
        return total_times_minutes


    def totalDistances(self, matrix: distance_matrix) -> List[float]:
        """Calculate the total distances it takes all members to reach each meeting location.

        Args:
            matrix: Time/distance matrix.

        Returns:
            List: Distance in km (rounded).

        """
        distances = matrix['distances']
        sums = [0.0] * len(distances[0])

        for sublist_index in range(len(distances)):
            for element_index in range(len(distances[0])):
                sums[element_index] += distances[sublist_index][element_index]

        total_distances_km = [round(element / 1000.0) for element in sums]
        return total_distances_km


    def getTotals(self) -> Dict:
        """Get the total times and distances for the group to reach each meeting location.

        Returns:
            Dict:
                times (List): Durations in minutes (rounded).
                distances (List): Distance in km (rounded).

        """
        matrix = self.getMatrix()
        times = self.totalTimes(matrix)
        distances = self.totalDistances(matrix)

        return {'times': times, 'distances': distances}
