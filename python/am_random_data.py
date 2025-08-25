import random
import string


def random_char(char_num):
    return "".join(random.choice(string.ascii_letters) for _ in range(char_num))


print(random_char(7) + "@gmail.com")


def random_email():
    return "".join(random.choice(string.ascii_letters) for _ in range(7)) + "@gmail.com"


print(f"random email: {random_email()}")


def random_password():
    return "".join(
        random.choice(string.ascii_letters + string.digits + string.punctuation)
        for _ in range(10)
    )


print(f"random password: {random_password()}")


def random_username():
    return "".join(random.choice(string.ascii_letters) for _ in range(7))


print(f"random username: {random_username()}")


def random_address():
    return "".join(
        random.choice(string.ascii_letters + string.digits + " ") for _ in range(15)
    )


print(f"random address: {random_address()}")


def random_phone():
    return "".join(random.choice(string.digits) for _ in range(10))


print(f"random phone: {random_phone()}")


def random_zipcode():
    return "".join(random.choice(string.digits) for _ in range(5))


print(f"random zipcode: {random_zipcode()}")


def random_city():
    return "".join(random.choice(string.ascii_letters + " ") for _ in range(10))


print(f"random city: {random_city()}")


def random_state():
    return "".join(random.choice(string.ascii_letters + " ") for _ in range(10))


print(f"random state: {random_state()}")


def random_country():
    return "".join(random.choice(string.ascii_letters + " ") for _ in range(10))


print(f"random country: {random_country()}")


def random_company():
    return "".join(random.choice(string.ascii_letters + " ") for _ in range(10))


print(f"random company: {random_company()}")


def random_website():
    return (
        "".join(random.choice(string.ascii_letters + string.digits) for _ in range(7))
        + ".com"
    )


print(f"random website: {random_website()}")


def random_firstname():
    return "".join(random.choice(string.ascii_letters) for _ in range(7))


print(f"random firstname: {random_firstname()}")


def random_lastname():
    return "".join(random.choice(string.ascii_letters) for _ in range(7))


print(f"random lastname: {random_lastname()}")


def random_fullname():
    return "".join(random.choice(string.ascii_letters + " ") for _ in range(15))


print(f"random fullname: {random_fullname()}")


def random_age():
    return "".join(random.choice(string.digits) for _ in range(2))


print(f"random age: {random_age()}")
