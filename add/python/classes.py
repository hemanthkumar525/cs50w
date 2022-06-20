

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passenger)

filght = Flight(5)

people = ['harry', 'hemanth', 'sunny', 'bunny']
for person in people:
    sucess = filght.add_passenger(person)
    if sucess:
        print(f'added {person} to filght successfully.')
    else :
        print(f"the filght is over booked")