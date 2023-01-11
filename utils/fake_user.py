import requests
from models.user import User

class FakeUser:
    
    def get_fake_user(self):
        response = requests.get("https://randomuser.me/api/")
        user_json = response.json()["results"][0]
        user = User(user_json)
        return user