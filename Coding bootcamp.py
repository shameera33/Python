web_development = ["alex", "john", "sam"]
data_science = ["stella", "steve", "jeeva"]
ui_ux = ["sarah", "aleena", "Asha"]

all_participants = web_development + data_science + ui_ux
print(all_participants)

web_development.append("Anna")
print(web_development)

data_science.insert(2, "Emma")
print(data_science)

ui_ux.pop()

data_science_copy = data_science.copy()

data_science.clear()

print(web_development[:2])

name_lengths = [len(x) for x in data_science_copy]
print("Length of each name:", name_lengths)

asha_present = ("Asha" in web_development or "Asha" in data_science or "Asha" in ui_ux)
print("Asha present:", asha_present)

first_participants = (web_development[0], data_science_copy[0], ui_ux[0])

print("First Participants:", first_participants)

