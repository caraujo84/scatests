import requests

from models.user import User


class FakeUser:

    def get_fake_user(self):
        response = requests.get("https://randomuser.me/api/?nat=us")
        user_json = response.json()["results"][0]
        user = User(user_json)
        return user

    def get_fake_users(self, count):
        users = []
        for _ in range(count):
            users.append(self.get_fake_user())
        return users
