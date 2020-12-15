import gdc
import json
import openrouteservice as ors
from openrouteservice.distance_matrix import distance_matrix
from os import path


key_path = "./ors.key"
members_path = "./data/members.ndjson"
locations_path = "./data/locations.ndjson"

with open(path.abspath(key_path)) as key_file:
    ors_api_key = key_file.readline().strip()

ors_client = ors.Client(ors_api_key)

with open(path.abspath(members_path)) as members_file:
    members = [gdc.Member(ors_client, line) for line in members_file]

with open(path.abspath(locations_path)) as locations_file:
    meeting_locations = [gdc.MeetingLocation(ors_client, line) for line in locations_file]


group_dist_calc = gdc.GroupDistanceCalculator(ors_client, members, meeting_locations)

totals = group_dist_calc.getTotals()
total_durations = totals['times']
total_distances = totals['distances']

for (location, i) in zip(meeting_locations, range(len(meeting_locations))):
    padding = " " * (12 - len(location.city))
    print(f"{location.city}: {padding}{total_durations[i]} min / {total_distances[i]} km")
