class Person:
    people = {}

    def __init__(
        self,
        name: str,
        age: int
    ) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = []

    for person in people:
        new_person = Person(
            person["name"],
            person["age"]
        )

        if "wife" in person and person["wife"] is not None:
            new_person.wife = person["wife"]
        elif "husband" in person and person["husband"] is not None:
            new_person.husband = person["husband"]

        person_list.append(new_person)

    for person in person_list:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        if hasattr(person, "husband"):
            person.husband = Person.people[person.husband]

    return person_list
