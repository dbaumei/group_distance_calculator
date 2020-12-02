import openrouteservice as ors
from openrouteservice.distance_matrix import distance_matrix
import json


class GroupDistanceCalculator:

    matrix = None
    durationsMinutes = []
    distancesKm = []

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
        durations = self.matrix['durations']
        sums = [0.0] * len(durations[0])

        for sublistIndex in range(len(durations)):
            for elementIndex in range(len(durations[0])):
                sums[elementIndex] += durations[sublistIndex][elementIndex]

        self.totalDurationsMinutes = [round(element / 60.0) for element in sums]
        return self.totalDurationsMinutes

    def calculateTotalDistance(self):
        distances = self.matrix['distances']
        sums = [0.0] * len(distances[0])

        for sublistIndex in range(len(distances)):
            for elementIndex in range(len(distances[0])):
                sums[elementIndex] += distances[sublistIndex][elementIndex]

        self.totalDistancesKm = [round(element / 1000.0) for element in sums]
        return self.totalDistancesKm

    # def getMemberGeocodes(self, members: []):
    #     geocodes = [member.getGeocode(self.client) for member in members]
    #     return geocodes

    # def getMeetingLocationGeocodes(self, meetingLocations: []):
    #     geocodes = [meetingLocation.getGeocode(self.client) for meetingLocation in meetingLocations]
    #     return geocodes

    def getDurationsMinutes(self):
        rawDurations = self.matrix['durations']

        for sublistIndex in range(len(rawDurations)):
            sublist = [round(element / 60.0) for element in rawDurations[sublistIndex]]
            self.durationsMinutes.append(sublist)

        return self.durationsMinutes

    def getDistancesKm(self):
        rawDistances = self.matrix['distances']

        for sublistIndex in range(len(rawDistances)):
            sublist = [round(element / 1000.0) for element in rawDistances[sublistIndex]]
            self.distancesKm.append(sublist)

        return self.distancesKm
