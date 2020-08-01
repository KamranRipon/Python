people = [
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Cho","house":"Ravenchlow"},
    {"name":"Draco","house":"Slytherin"}
    
    ]



people.sort(key=lambda person: person["name"])

print(people)