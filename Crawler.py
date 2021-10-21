import requests
import praw
import datetime
import pandas as pd
import re
# The below is used to get Oauthorization for them
# Api documentation below

client_Id='_SMrSNxE9KWJwd2SLMKV7A'
secret_Id='UZd7BFy66EyyPlxRdjLYIdi8wFmqsA'
# Search by specific key words
# Search type of post to crawl, and crawl all elements that show that type of post. 
# Access to post depending on post keywords on either title, and description

def KeywordPrint(dataframe, key): # To print by keyword 
    for title in dataframe:
        if key in title:
            print(title)
    df_filtered = dataframe[dataframe['Title'] == re.compile('* '+key+' *')]
    return df_filtered

def dataframeInitKey(sub, key): #Initializes the Dataframw by given subreddit and keyword
    allPosts = []
    numPosts = int(input("How many posts will you like to look at: "))
    hot_posts = reddit.subreddit(sub).hot(limit=numPosts)

    for post in hot_posts: #Reads in each specific post and adds them to the allPosts list
        if key in post.title:
            allPosts.append([post.id,post.title,post.score,post.num_comments,post.created])

    allPosts = pd.DataFrame(allPosts,columns=['ID','Title','Upvotes','Comments',"Date"]) # Creates a dataframs that holds the information with column names

    return allPosts


def dataframeInit(sub): #Initializaes the dataframe by given subreddit with no keywords
    allPosts = []
    numPosts = int(input("How many posts will you like to look at: "))
    hot_posts = reddit.subreddit(sub).hot(limit=numPosts)

    for post in hot_posts: #Reads in each specific post and adds them to the allPosts list
        allPosts.append([post.id,post.title,post.score,post.num_comments,post.created])

    allPosts = pd.DataFrame(allPosts,columns=['ID','Title','Upvotes','Comments',"Date"]) # Creates a dataframs that holds the information with column names

    return allPosts



#-----------Main Method-----------#


subreddit = input("What Subreddit will you like to Crawl: ")
reddit = praw.Reddit(client_id=client_Id, client_secret=secret_Id, user_agent='WallstreetCrawler') #Connect to the Wallstreet Reddi API

ans = input("Would you like to crawl by a keyword in post title? (y/n):")
while (1):
    if ans == 'y' or ans == 'n':
        break
    print("You inputed ["+ ans + "] ")
    ans = input("Input ERROR\nWould you like to crawl by a keyword in post title? (y/n): ")


if ans == 'y':

    key = input("Please Enter Keyword to Crawl by: ")
    while key != 'STOP':

        Posts = dataframeInitKey(subreddit,key)

        csvOutput = subreddit + '_' + key + '.csv'  #Creates CSV file for output
        Posts.to_csv(csvOutput)                     #Creates CSV file depending on the KeyWord and Subreddit

        key = input("Type 'STOP' if you would like to quit. Otherwise, please insert Keyword to Crawl: ")
else:
    Posts = dataframeInit(subreddit)        #Initilizes the dataframe using function with given subreddit
    csvOutput = subreddit + '.csv'
    Posts.to_csv(csvOutput)




#-----------Main Method-----------#
