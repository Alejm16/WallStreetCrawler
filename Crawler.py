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

def dataframeInitTitleKey(sub, key): #Initializes the Dataframw by given subreddit and keyword
    allPosts = []
    numPosts = int(input("How many posts will you like to look at: "))
    hot_posts = reddit.subreddit(sub).hot(limit=numPosts)

    for post in hot_posts: #Reads in each specific post and adds them to the allPosts list
        if key in post.title:
            allPosts.append([post.id,post.title,post.score,post.num_comments,datetime.datetime.fromtimestamp(post.created_utc),post.selftext])

    allPosts = pd.DataFrame(allPosts,columns=['ID','Title','Upvotes','Comments',"Date","Body"]) # Creates a dataframs that holds the information with column names

    return allPosts

def dataframeInitPostKey(sub, key): #Initializes the Dataframw by given subreddit and keyword
    allPosts = []
    numPosts = int(input("How many posts will you like to look at: "))
    hot_posts = reddit.subreddit(sub).hot(limit=numPosts)

    for post in hot_posts: #Reads in each specific post and adds them to the allPosts list
        if key in post.selftext:
            allPosts.append([post.id,post.title,post.score,post.num_comments,datetime.datetime.fromtimestamp(post.created_utc),post.selftext])

    allPosts = pd.DataFrame(allPosts,columns=['ID','Title','Upvotes','Comments',"Date","Body"]) # Creates a dataframs that holds the information with column names

    return allPosts

def dataframeInit(sub): #Initializaes the dataframe by given subreddit with no keywords
    allPosts = []
    numPosts = int(input("How many posts will you like to look at: "))
    hot_posts = reddit.subreddit(sub).hot(limit=numPosts)

    for post in hot_posts: #Reads in each specific post and adds them to the allPosts list
        allPosts.append([post.id,post.title,post.score,post.num_comments,datetime.datetime.fromtimestamp(post.created_utc),post.selftext])

    allPosts = pd.DataFrame(allPosts,columns=['ID','Title','Upvotes','Comments',"Date","Body"]) # Creates a dataframs that holds the information with column names

    return allPosts



#-----------Main Method-----------#



while 1:
    print("Welcome to my Reddit Web Crawler!\nPlease input a number from the choices below\n")
    crawlChoice = input("1 - Crawl certain number of posts.\n2 - Crawl by keyword in Post Title.\n3 - Crawl by keyword in Post Description.")

    while (1):
        if crawlChoice == 1 or crawlChoice == 2 or crawlChoice == 3:
            break
        print("you inputed [" + crawlChoice + "]")
        crawlChoice = input("INPUT ERROR\n1 - Crawl certain number of posts.\n2 - Crawl by keyword in Post Title.\n3 - Crawl by keyword in Post Description.")



    typeChoice = input("Would you like to sort by hot posts? (y/n)\n")
    while(1):
        if typeChoice == 'y' or typeChoice == 'n':
            break
        print("You inputed ["+ typeChoice + "] ")
        typeChoice = input("Input ERROR\nWould you like to sort by hot posts? (y/n)\n")



    subreddit = input("What Subreddit will you like to Crawl: ")
    reddit = praw.Reddit(client_id=client_Id, client_secret=secret_Id, user_agent='WallstreetCrawler') #Connect to the Wallstreet Reddi API

    if crawlChoice == 1:
        Posts = dataframeInit(subreddit)        #Initilizes the dataframe using function with given subreddit
        csvOutput = subreddit + '.csv'
        Posts.to_csv(csvOutput)

    if crawlChoice == 2:
        key = input("Please Enter Keyword to Crawl by: ")
        Posts = dataframeInitTitleKey(subreddit,key)

        csvOutput = subreddit + '_' + key + '.csv'  #Creates CSV file for output
        Posts.to_csv(csvOutput)                     #Creates CSV file depending on the KeyWord and Subreddit


    if crawlChoice == 3:
        key = input("Please Enter Keyword to Crawl by: ")
        Posts = dataframeInitPostKey(subreddit,key)

        csvOutput = subreddit + '_' + key + '.csv'  #Creates CSV file for output
        Posts.to_csv(csvOutput)                     #Creates CSV file depending on the KeyWord and Subreddit




#-----------Main Method-----------#
