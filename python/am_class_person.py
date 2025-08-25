import datetime
import uuid


class PersonData:
    data = {
        "marriages": [],
        "children": [],
        "pets": [],
        "jobs": [],
        "addresses": [],
        "phone_numbers": [],
        "emails": [],
        "social_media": [],
        "relatives": [],
        "medical_conditions": [],
        "allergies": [],
        "medications": [],
        "hobbies": [],
        "skills": [],
        "languages": [],
        "education": [],
        "certifications": [],
        "memberships": [],
        "notes": [],
        "documents": [],
        "photos": [],
        "videos": [],
        "social_security_number": None,
        "driver_license_number": None,
        "passport_number": None,
        "tax_identification_number": None,
        "credit_cards": [],
        "bank_account_numbers": [],
        "insurance_policy_numbers": [],
        "vehicle_information": [],
        "emergency_contacts": [],
        "favorite_foods": [],
        "favorite_movies": [],
        "favorite_books": [],
        "favorite_authors": [],
        "favorite_music": [],
        "favorite_games": [],
    }


class PersonDataCore(PersonData):
    def marriage(self, spouse_id, date):
        self.data["marriages"].append({"spouse": spouse_id, "date": date})


class PersonCore(PersonDataCore):

    def __init__(self, first_name: str, last_name: str, birthday=None):
        self.birthday = birthday
        self.first_name = first_name
        self.last_name = last_name
        self.id = uuid.uuid4()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, born on {self.birthday}, Identifier in matrix: {self.id}"

    @property
    def age(self):
        if self.birthday is None:
            return None
        try:
            birth_date = datetime.datetime.strptime(self.birthday, "%m/%d/%Y").date()
            today = datetime.date.today()
            complement = (today.month, today.day) < (birth_date.month, birth_date.day)
            age = today.year - birth_date.year - complement
            return age
        except ValueError:
            return None


class Person(PersonCore):
    pass


p1 = Person("John", "Smith", "8/1/1990")

print(f"first name: {p1.first_name}")
print(f"last name: {p1.last_name}")

print(f"birthday: {p1.birthday}")

print(f"age: {p1.age}")

print(f"id: {p1.id}")

print(f"object: {p1}")

p2 = Person("Alisa", "North", "4/11/1998")

print(f"object: {p2}")

print(f"marriages: {p1.data['marriages']}")

p1.marriage(p2.id, "6/15/2015")

print(f"marriages: {p1.data['marriages']}")
