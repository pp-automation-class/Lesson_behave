import datetime


class Person:
    marriages = []
    children = []
    pets = []
    jobs = []
    addresses = []
    phone_numbers = []
    emails = []
    social_media = []
    relatives = []
    medical_conditions = []
    allergies = []
    medications = []
    hobbies = []
    skills = []
    languages = []
    education = []
    certifications = []
    memberships = []
    notes = []
    documents = []
    photos = []
    videos = []
    audio_recordings = []
    websites = []
    social_security_number = None
    driver_license_number = None
    passport_number = None
    tax_identification_number = None
    credit_card_number = None
    bank_account_number = None
    insurance_policy_number = None
    emergency_contacts = []
    favorite_colors = []
    favorite_foods = []
    favorite_movies = []
    favorite_books = []
    favorite_authors = []
    favorite_music = []
    favorite_places = []
    favorite_quotes = []
    favorite_sports = []
    favorite_activities = []
    favorite_holidays = []
    favorite_seasons = []
    favorite_animals = []
    favorite_flowers = []
    favorite_countries = []
    favorite_cities = []
    favorite_restaurants = []
    favorite_shops = []
    favorite_websites = []
    favorite_apps = []
    favorite_games = []
    favorite_tv_shows = []
    favorite_podcasts = []
    favorite_youtubers = []
    favorite_influencers = []
    favorite_celebrities = []
    favorite_historical_figures = []
    favorite_fictional_characters = []
    favorite_heroes = []
    favorite_villains = []
    favorite_superheroes = []
    favorite_supervillains = []
    favorite_mythological_figures = []
    favorite_folklore_figures = []
    favorite_legends = []
    favorite_fables = []
    favorite_fairy_tales = []
    favorite_nursery_rhymes = []
    favorite_jokes = []
    favorite_memes = []
    favorite_sayings = []
    favorite_idioms = []
    favorite_proverbs = []
    favorite_catchphrases = []
    favorite_slogans = []
    favorite_mottos = []
    favorite_mantras = []
    favorite_affirmations = []
    favorite_prayers = []
    favorite_quotes_from_books = []
    favorite_quotes_from_movies = []
    favorite_quotes_from_tv_shows = []
    favorite_quotes_from_songs = []
    favorite_quotes_from_speeches = []
    favorite_quotes_from_historical_figures = []
    favorite_quotes_from_fictional_characters = []
    favorite_quotes_from_heroes = []
    favorite_quotes_from_villains = []
    favorite_quotes_from_superheroes = []
    favorite_quotes_from_supervillains = []
    favorite_quotes_from_mythological_figures = []
    favorite_quotes_from_folklore_figures = []
    favorite_quotes_from_legends = []
    favorite_quotes_from_fables = []
    favorite_quotes_from_fairy_tales = []
    favorite_quotes_from_nursery_rhymes = []
    favorite_quotes_from_jokes = []
    favorite_quotes_from_memes = []
    favorite_quotes_from_sayings = []

    def __init__(self, first_name: str, last_name: str, birthday=None):
        self.birthday = birthday
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, born on {self.birthday}"

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


p1 = Person("John", "Smith", "8/1/1990")

print(p1.first_name)
print(p1.last_name)

print(p1.birthday)

print(p1.age)

print(p1)
