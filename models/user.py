class User:
    def __init__(self, user):
        self.email = user["email"]
        self.first_name = user["name"]["first"]
        self.last_name = user["name"]["last"]
        self.title = user["name"]["title"]
        self.gender = user["gender"]
        self.phone = user["phone"]
        self.age = user["dob"]["age"]
        self.date_of_birth = user["dob"]["date"]
        self.picture = user["picture"]["medium"]
        self.username = user["login"]["username"]
        self.password = user["login"]["password"]

    def __str__(self):
        return f"Email: {self.email}, First Name: {self.first_name}, Last Name: {self.last_name}, Title: {self.title}, Gender: {self.gender}, Phone: {self.phone}, Age: {self.age}, Date of Birth: {self.date_of_birth}, Picture: {self.picture}, Username: {self.username}, Password: {self.password}"
