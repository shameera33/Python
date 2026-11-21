import tripdata
from datetime import datetime
import json

trips = [
    tripdata.get_trip("Paris", "15-05-2023", "Beautiful city"),
    tripdata.get_trip("London", "20-06-2023", "Amazing trip"),
    tripdata.get_trip("Dubai", "10-01-2024", "Great experience")
]

for trip in trips:
    date = datetime.strptime(trip["date"], "%d-%m-%Y").date()
    trip["date"] = date.strftime("%B %d, %Y")

result = json.dumps(trips, indent=4)

print(result)