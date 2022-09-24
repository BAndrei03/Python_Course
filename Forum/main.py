class User:
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password
        self.followers = 0
        self.following = 0
        self.user_dict = {
            'id' : user_id,
            'login_username' : username,
            'pass' : password,
            'followers': 0,
            'following': 0
        }

    # return user_dict

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def unfollow(self, user):
        user.followers -= 1
        self.following -= 1
        if user.followers < 0:
            user.followers = 0

    def introduce(self):
        print("Hello! I am", self.username, "and i have", self.followers, "followers!")


class Postare():

    def __init__(self, likes, date):
        self.likes = likes
        self.date = str(date)
        print("This posts was made on", self.date, "and it have", self.likes, "likes")


class Comment():

    # def comentariu(self):
    #     return self.username
    #     return self.likes
#
# def comentariu(users):
#     detalii = []
#     for user in users:

if __name__ == "__main__":
    user_dict={}
    user_1 = User("001", "andrei", "pass1")
    user_2 = User("002", "liviu", "pass2")
    # user_1.follow(user_2)
    # user_2.introduce()
    # post_1 = Postare(14, "03.10.2021")
    # comm = Comment("001", "andrei", "pass1")
    # print(comm.comentariu())