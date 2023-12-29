class Flight():  # Class
    def __init__(self, capacity):  # Constructor
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):  # Method
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)  # Object
people = ["Aman", "Shruti", "Shaikada", "Sanjana", "Kirti", "Rishu"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")

