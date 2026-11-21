import tracker
from datetime import datetime
import json

records = [
    tracker.create_record("Kochi", "Beautiful place", "05-06-2022"),
    tracker.create_record("Munnar", "Cool weather", "10-01-2023"),
    tracker.create_record("Ooty", "Amazing trip", "15-05-2024")
]

for record in records:
    date = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date.strftime("%B %d, %Y")

data = json.dumps(records)

print(data)

new_data = json.loads(data)

for record in new_data:
    print(record)