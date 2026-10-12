

table = {
    "Red": "Stop",
    "Yellow": "Slow Down",
    "Green": "Go",
    "Flashing Red": "Stop and Proceed with Caution"
}

def traffic_light_agent(percept):
    return table.get(percept, "Unknown percept")

percept_sequence = ["Red", "Green", "Yellow", "Red"]

print("Percept\t\tAction")
for percept in percept_sequence:
    action = traffic_light_agent(percept)
    print(f"{percept}\t\t{action}")