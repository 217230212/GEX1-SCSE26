######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################



airport_info = ("OUL", 1, "14-09-2026")


allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}


restricted_destinations = {"Moscow", "Pyongyang"}


flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"]
    }
}



def find_flight(flights, flight_number):
    """Return the normalized (original) flight key if found, else None.
    Match is case-insensitive and ignores surrounding whitespace."""
    if flight_number is None:
        return None
    normalized = flight_number.strip()
    for key in flights:
        if key.upper() == normalized.upper():
            return key
    return None



def passenger_exists(passengers, passenger_name):
    """Return True if passenger_name is in the list (case-insensitive)."""
    if passenger_name is None:
        return False
    target = passenger_name.strip().lower()
    for name in passengers:
        if name.lower() == target:
            return True
    return False


def _normalize_name(name):
    return " ".join(part.capitalize() for part in name.strip().split())



def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    """Check in a passenger. Returns one of:
    OK, FLIGHT_NOT_FOUND, EMPTY_NAME, DUPLICATE, FULL, RESTRICTED"""


    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    flight = flights[flight_key]


    if passenger_name is None or passenger_name.strip() == "":
        return "EMPTY_NAME"

    normalized_name = _normalize_name(passenger_name)


    destination = flight["destination"]
    for restricted in restricted_destinations:
        if destination.lower() == restricted.lower():
            return "RESTRICTED"


    if passenger_exists(flight["passengers"], normalized_name):
        return "DUPLICATE"


    if len(flight["passengers"]) >= flight["capacity"]:
        return "FULL"


    flight["passengers"].append(normalized_name)
    return "OK"


def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    """Remove a passenger. Returns OK, FLIGHT_NOT_FOUND, or PASSENGER_NOT_FOUND."""


    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    flight = flights[flight_key]

    target = passenger_name.strip().lower()
    for i, name in enumerate(flight["passengers"]):
        if name.lower() == target:
            flight["passengers"].pop(i)
            return "OK"

    return "PASSENGER_NOT_FOUND"



def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    """Change a flight's gate. Returns OK, FLIGHT_NOT_FOUND, or INVALID_GATE."""

    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

if new_gate is None:
        return "INVALID_GATE"

    gate_input = new_gate.strip()
    for gate in allowed_gates:
        if gate.upper() == gate_input.upper():
 
            flights[flight_key]["gate"] = gate
            return "OK"

    return "INVALID_GATE"



def flight_status(flight):
    """Return AVAILABLE, ALMOST FULL, or FULL based on passenger fill percentage."""
    capacity = flight["capacity"]
    passenger_count = len(flight["passengers"])

    if capacity <= 0:
        return "FULL"

    percentage = passenger_count / capacity * 100

    if percentage >= 100:
        return "FULL"
    elif percentage >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"



def sorted_manifest(
    flights,
    flight_number
):
    """Return a sorted copy of passenger names, or None if flight not found."""
    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return None

    return sorted(flights[flight_key]["passengers"])



def total_passengers(flights):
    """Return the total passenger count across all flights."""
    total = 0
    for flight in flights.values():
        total += len(flight["passengers"])
    return total



def any_full_flight(flights):
    """Return True if at least one flight is full, False otherwise."""
    for flight in flights.values():
        if len(flight["passengers"]) >= flight["capacity"]:
            return True
    return False



def all_flights_have_passengers(flights):
    """Return True if every flight has at least one passenger, False otherwise."""
    if not flights:
        return True
    for flight in flights.values():
        if len(flight["passengers"]) == 0:
            return False
    return True
