import json

states = {
    "Andhra Pradesh": "Hyderabad",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow"
}

with open('states.json', 'w') as f:
    json.dump(states, f)

