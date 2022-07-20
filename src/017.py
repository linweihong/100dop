### Quiz Game ###

from res017.data import question_data


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(1, "angela")
user_2 = User(2, "jack")

user_1.follow(user_2)
print(user_1.following, user_1.followers, user_2.following, user_2.followers)
