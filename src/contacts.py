CONTACTS = {
    "IN": {
        "Fire": "101",
        "Ambulance": "102",
        "Police": "100",
        "Disaster Helpline": "108"
    },
    "US": {
        "Emergency": "911",
        "FEMA Helpline": "1-800-621-3362"
    },
    "DEFAULT": {
        "Red Cross": "+1-202-303-4498"
    }
}

def get_emergency_contacts(country_code):
    return CONTACTS.get(country_code.upper(), CONTACTS["DEFAULT"])
