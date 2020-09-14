from openrouteservice.distance_matrix import distance_matrix
import json

from Member import Member
from MeetingLocation import MeetingLocation
from GroupDistanceCalculator import GroupDistanceCalculator as GDC


#TODO
# Generate hashes for locations and store them with the data in /data or so
# Get more adresses for meeting locations
# Calculate separate distances and times
# Aggregate distances and times

with open("/Users/dominicbaumeister/workspace/group_distance_calculator/ors.key") as key_file:
    ors_api_key = key_file.readline().strip()

list_of_members = [ ("Christin", "Bocholt"),
                    ("Daniel", "Ottenstein Ahaus"),
                    ("David", "46359 Heiden"),
                    ("Dominic", "46359 Heiden"),
                    ("Jan", "48599 Gronau"),
                    ("Lars", "Ahaus-Wessum"),
                    ("Lisa-Marie", "Bocholt"),
                    ("Lukas", "Raesfeld"),
                    ("Vincent", "Bocholt"),
                    ("Heiner", "Velen")
]

list_of_locations = [{  "city": "Heiden",
                        "street": "Am Sportzentrum",
                        "house_number": 7
                    },
                    {  "city": "Bocholt",
                        "street": "Anholter Postweg",
                        "house_number": 3
                    },
                    {  "city": "Raesfeld",
                        "street": "",
                        "house_number": 0
                    },
                    {  "city": "Suedlohn",
                        "street": "",
                        "house_number": 0
                    },
                    {  "city": "Heek",
                        "street": "",
                        "house_number": 0
                    }
]

gdc = GDC(ors_api_key)

# Get proper objects from list
members = [Member(member[0], member[1]) for member in list_of_members]
meetingLocations = [MeetingLocation(city = location["city"], street = location["street"], house_number = location["house_number"]) for location in list_of_locations]

gdc.getMatrix(members, meetingLocations)

durations = gdc.getDurationsMinutes()
distances = gdc.getDistancesKm()

totalDurations = gdc.calculateTotalTime()
totalDistances = gdc.calculateTotalDistance()

for (location, i) in zip(meetingLocations, range(len(meetingLocations))):
    padding = " " * (12 - len(location.city))
    print(f"{location.city}: {padding}{totalDurations[i]} min / {totalDistances[i]} km")
