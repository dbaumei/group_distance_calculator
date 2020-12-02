import openrouteservice as ors
from openrouteservice.distance_matrix import distance_matrix
import json
from os import path

from Member import Member
from MeetingLocation import MeetingLocation
from GroupDistanceCalculator import GroupDistanceCalculator as GDC


#TODO
# Generate hashes for locations and store them with the data in /data or so
# Get more adresses for meeting locations
# Calculate separate distances and times
# Aggregate distances and times
# Add JSON validation
# Write unit tests
# Automate tests with GH Actions
# Figure out how to get secrets into GH Action (API token)

key_path = "./ors.key"
members_path = "./data/members.ndjson"
locations_path = "./data/locations.ndjson"

with open(path.abspath(key_path)) as key_file:
    ors_api_key = key_file.readline().strip()

ors_client = ors.Client(ors_api_key)

with open(path.abspath(members_path)) as members_file:
    members = [Member(ors_client, line) for line in members_file]

with open(path.abspath(locations_path)) as locations_file:
    locations_raw = [json.loads(line) for line in locations_file]

# print(locations_raw)

gdc = GDC(ors_api_key)

# # Get proper objects from list
# members = [Member(member[0], member[1]) for member in list_of_members]
# meetingLocations = [MeetingLocation(city = location["city"], street = location["street"], house_number = location["house_number"]) for location in list_of_locations]

# gdc.getMatrix(members, meetingLocations)

# durations = gdc.getDurationsMinutes()
# distances = gdc.getDistancesKm()

# totalDurations = gdc.calculateTotalTime()
# totalDistances = gdc.calculateTotalDistance()

# for (location, i) in zip(meetingLocations, range(len(meetingLocations))):
#     padding = " " * (12 - len(location.city))
#     print(f"{location.city}: {padding}{totalDurations[i]} min / {totalDistances[i]} km")
