import random
import time

cryptids = [
    {
        "name": "Wendigo",
        "threat": 9,
        "location": "Snowy Forest",
        "description": "A tall skeletal creature associated with endless hunger."
    },
    {
        "name": "Mothman",
        "threat": 6,
        "location": "Abandoned Town",
        "description": "A winged humanoid seen before disasters."
    },
    {
        "name": "Skinwalker",
        "threat": 8,
        "location": "Desert",
        "description": "A shapeshifting entity mimicking human voices."
    },
    {
        "name": "La Llorona",
        "threat": 5,
        "location": "River",
        "description": "A ghostly woman crying for her lost children."
    },
    {
        "name": "Slender Man",
        "threat": 7,
        "location": "Dark Woods",
        "description": "A tall faceless figure stalking silently."
    }
]

locations = [
    "Black Forest",
    "Abandoned Hospital",
    "Old Village",
    "Foggy Swamp",
    "Mountain Cave"
]

def encounter():
    print("\n🌫️ Exploring area...")
    time.sleep(1)

    place = random.choice(locations)
    print(f"You are exploring: {place}\n")
    time.sleep(1)

    if random.random() < 0.7:  # 70% chance encounter
        cryptid = random.choice(cryptids)
        print("⚠️ CRYPTID ENCOUNTERED!")
        print(f"Name       : {cryptid['name']}")
        print(f"Threat Lv  : {cryptid['threat']}")
        print(f"Location   : {cryptid['location']}")
        print(f"Description: {cryptid['description']}\n")

        outcome = random.choice([
            "You escaped safely.",
            "You barely escaped with your sanity...",
            "You were injured but survived.",
            "The cryptid vanished suddenly."
        ])
        print(f"Result: {outcome}")
    else:
        print("✅ Area clear. No cryptid encountered.")

# MAIN LOOP
while True:
    user = input("\nPress ENTER to explore or type 'exit': ").lower()
    if user == "exit":
        print("👁️ You leave the area...")
        break
    encounter()
