import openrouteservice as ors
from openrouteservice.distance_matrix import distance_matrix
import json


class GroupDistanceCalculator:

    matrix = None

    def __init__(self, key: str):
        self.client = ors.Client(key = key)

    def getMatrix(self, members, meetingLocations):
        """
        Takes the geocodes of members and meetingLocations and fetches the time/distance matrix.
        """

        locations = self.getMemberGeocodes(members)
        locations.extend(self.getMeetingLocationGeocodes(meetingLocations))

        memberIndices = [i for i in range(len(members))]
        meetingLocationIndices = [i + memberIndices[-1] + 1 for i in range(len(meetingLocations))]
        
        self.matrix = distance_matrix(  self.client,
                                        locations=locations,
                                        metrics=['distance', 'duration'],
                                        sources=memberIndices,
                                        destinations=meetingLocationIndices
                                    )

    def calculateTotalTime(self):
        pass

    def calculateTotalDistance(self):
        pass

    def getMemberGeocodes(self, members: []):
        geocodes = [member.getGeocode(self.client) for member in members]
        return geocodes

    def getMeetingLocationGeocodes(self, meetingLocations: []):
        geocodes = [meetingLocation.getGeocode(self.client) for meetingLocation in meetingLocations]
        return geocodes

    def getDurationsMinutes(self):
        rawDurations = self.matrix['durations']
        durationsMinutes = [[]]
        print(rawDurations)

        for sublistIndex in range(len(rawDurations)):
            print(f"{sublistIndex} / {len(rawDurations)}")
            print(rawDurations[sublistIndex])
            durationsMinutes[sublistIndex] = [round(element / 60.0) for element in rawDurations[sublistIndex]]
        # durationsMinutes = [ for sublist in rawDurations for element in sublist]

        return durationsMinutes