class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers=[]
        
    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)   
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
        


flight = Flight(5)
people = ['Kamran', "Ripon","abdullah","Taleb","moinur","sadek","ratul"]
n =flight.capacity
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} is successfull.")
        n -=1
        print(f"Seat leaft {n}.")

