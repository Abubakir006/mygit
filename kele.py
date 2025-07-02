print(30 + 30)

people = [
    {"name": "Али", "age": 25},
    {"name": "Бек", "age": 20},
    {"name": "Чынгыз", "age": 30}
]

def sort_people_by_age(people: list[dict]) -> list[dict]:
    return sorted(people, key=lambda person: person["age"])
print(sort_people_by_age(people))

def fill(name, age):
    return name, age

print(fill('f',27))






