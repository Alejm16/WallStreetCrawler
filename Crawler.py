import requests
import praw
import datetime
import pandas as pd
# The below is used to get Oauthorization for them
# Api documentation below
# Search by specific key words
# Search type of post to crawl, and crawl all elements that show that type of post. 
# Access to post depending on post keywords on either title, and description


client_Id='_SMrSNxE9KWJwd2SLMKV7A'
secret_Id='UZd7BFy66EyyPlxRdjLYIdi8wFmqsA'
csvOuptput = 'WallStreetBetts.csv'

reddit = praw.Reddit(client_id=client_Id, client_secret=secret_Id, user_agent='WallstreetCrawler')

allPosts=[] # Created for the dataframe

numPosts = int(input("How many posts will you like to look at: "))
hot_posts = reddit.subreddit('wallstreetbets').hot(limit=numPosts)

for post in hot_posts: #Reads in each specific post and adds them to the allPosts list
    if "Daily" in post.title:
        print(post.title)
    allPosts.append([post.id,post.title,post.score,post.num_comments,post.created])

allPosts = pd.DataFrame(allPosts,columns=['ID','Title','Upvotes','Comments',"Date"]) # Creates a dataframs that holds the information with column names

allPosts.to_csv(csvOuptput) #Ouputs the dataframes to the csv file

