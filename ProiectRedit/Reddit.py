import csv
import os


class Reddit:
    def __init__(self):
        self.url = "www.reddit.com"
        self.subredits = 0

    def createSubreddit(self, title, description):
        self.subreditURL = self.url + "/"
        self.title = title
        self.description = description

        index_number = 0
        with open('Subreddits/subreddits.csv') as file:
            index_number = int(file.readlines()[-1][0]) + 1

        with open('Subreddits/subreddits.csv', 'a', newline='') as f_subreddit:
            subredditDetails = [index_number, self.title, self.description, self.subreditURL + str(index_number), 0]
            writer = csv.writer(f_subreddit)
            writer.writerow(subredditDetails)
            f_subreddit.close()

    def allSubReddit(self):
        with open('Subreddits/subreddits.csv', 'r', newline='') as f_subreddit:
            headings = next(f_subreddit)
            data = csv.reader(f_subreddit, skipinitialspace=False)
            for row in data:
                print(', '.join(row))

           # row = f_subreddit.readlines()
           #  print(row)
           #  for i, line in enumerate(row):
           #      print(line)
        # print("URL of Subredit " + self.subreditURL + "\n"
        #       "Title is " + self.title + "\n"
        #       "Description is " + self.description + "\n" +
        #       "The subreddit have " + str(self.followers) + " followers" + "\n")
        # self.detailSubreddit = [self.title, self.description, self.followers]

    def createPost(self, title, description, owner):
        self.title = title
        self.description = description
        self.owner = owner

        index_post = 0
        try:
            with open('Subreddits/posts.csv') as file:
                index_post = int(file.readlines()[-1][0]) + 1
        except:
            index_post = 0

        index_number = 0
        with open('Subreddits/subreddits.csv') as file:
            index_number = int(file.readlines()[-1][0]) + 1

        with open('Subreddits/posts.csv', 'a', newline='') as f_subreddit:
            postsDetails = [index_post, self.title, self.description, self.owner, index_number]
            writer = csv.writer(f_subreddit)
            writer.writerow(postsDetails)
            f_subreddit.close()

    def showPosts(self):
        with open('Subreddits/posts.csv', 'r') as f_subreddit:
            headings = next(f_subreddit)
            data = csv.reader(f_subreddit, skipinitialspace=False)
            for row in data:
                print(', '.join(row))

    def comment(self):
        pass

    def review(self):
        pass

    def user(self):
        pass


if __name__ == "__main__":
    r = Reddit()
    if os.path.isfile("./Subreddits/subreddits.csv"):
        print("Subreddit file exists")
    else:
        with open('Subreddits/subreddits.csv', 'w+', encoding='utf-8', newline='') as f:
            rowHeader = ["Index_Subreddit", "Title", "Description", "URL", "Followers"]
            writer = csv.writer(f)
            writer.writerow(rowHeader)
            f.close()

    if os.path.isfile("./Subreddits/posts.csv"):
        print("Posts file exists")
    else:
        with open('Subreddits/posts.csv', 'w+', encoding='utf-8', newline='') as f:
            rowHeader = ["Index_Post", "Title", "Description", "Owner", "Index_Subreddit"]
            writer = csv.writer(f)
            writer.writerow(rowHeader)
            f.close()

    while True:
        a = input("Show Subreddits: Y/N" + "\n")
        if a.upper() == "Y":
            r.allSubReddit()
        a = input("Create Subreddit: Y/N" + "\n")
        if a.upper() == "Y":
            title = input("Title: ")
            description = input("Description: ")
            r.createSubreddit(title, description)

        a = input("Create Post: Y/N" + "\n")
        if a.upper() == "Y":
            title = input("Title: ")
            description = input("Description: ")
            owner = input("Created by: ")
            r.createPost(title, description, owner)
        a = input("Show All The Posts: Y/N" + "\n")
        if a.upper() == "Y":
            r.showPosts()