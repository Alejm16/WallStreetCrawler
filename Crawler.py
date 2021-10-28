import requests
import praw
from prawcore import NotFound
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


def sub_exists(sub): #used to check if subreddit does exist
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists



def dataframeInitTitleKey(sub, key, hotOrNaa): #Initializes the Dataframe by given subreddit and keyword for Title
    allPosts = []
    numPosts = int(input("How many posts will you like to look at: "))
    if hotOrNaa == 'y':
        hot_posts = reddit.subreddit(sub).hot(limit=numPosts)
    else:
        hot_posts = reddit.subreddit(sub).new(limit=numPosts)

    for post in hot_posts: #Reads in each specific post and adds them to the allPosts list
        if key in post.title:
            allPosts.append([post.id,post.title,post.score,post.num_comments,datetime.datetime.fromtimestamp(post.created_utc),post.selftext])

    allPosts = pd.DataFrame(allPosts,columns=['ID','Title','Upvotes','Comments',"Date","Body"]) # Creates a dataframs that holds the information with column names

    return allPosts

def dataframeInitPostKey(sub, key,hotOrNaa): #Initializes the Dataframw by given subreddit and keyword for Post description
    allPosts = []
    numPosts = int(input("\nHow many posts will you like to look at: "))
    if hotOrNaa == 'y':
        hot_posts = reddit.subreddit(sub).hot(limit=numPosts)
    else:
        hot_posts = reddit.subreddit(sub).new(limit=numPosts)

    for post in hot_posts: #Reads in each specific post and adds them to the allPosts list
        if key in post.selftext:
            allPosts.append([post.id,post.title,post.score,post.num_comments,datetime.datetime.fromtimestamp(post.created_utc),post.selftext])

    allPosts = pd.DataFrame(allPosts,columns=['ID','Title','Upvotes','Comments',"Date","Body"]) # Creates a dataframs that holds the information with column names

    return allPosts

def dataframeInit(sub,hotOrNaa): #Initializaes the dataframe by given subreddit with no keywords

    allPosts = []
    numPosts = int(input("\nHow many posts will you like to look at: "))
    if hotOrNaa == 'y':
        hot_posts = reddit.subreddit(sub).hot(limit=numPosts)
    else:
        hot_posts = reddit.subreddit(sub).new(limit=numPosts)

    for post in hot_posts: #Reads in each specific post and adds them to the allPosts list
        allPosts.append([post.id,post.title,post.score,post.num_comments,datetime.datetime.fromtimestamp(post.created_utc),post.selftext])

    allPosts = pd.DataFrame(allPosts,columns=['ID','Title','Upvotes','Comments',"Date","Body"]) # Creates a dataframs that holds the information with column names

    return allPosts



#-----------Main Method-----------#


tryAgain = 'y'

print("\n+++++++++++++++++++++++++++++++++++++++\n")
print("Welcome to my Reddit Web Crawler!\nHow it Works:\nYou will be given choices below and once they are answerd a csv file will be created with the choice you selected.\n")
while tryAgain == 'y':
    print("Please input a number from the choices below\n")
    crawlChoice = int(input("1 - Crawl certain number of posts.\n2 - Crawl by keyword in Post Title.\n3 - Crawl by keyword in Post Description.\nInput:"))

    while 1:
        print(crawlChoice)
        if crawlChoice == 1 or crawlChoice == 2 or crawlChoice == 3:
            break
        print("you inputed [" + str(crawlChoice) + "]")
        crawlChoice = int(input("INPUT ERROR\n1 - Crawl certain number of posts.\n2 - Crawl by keyword in Post Title.\n3 - Crawl by keyword in Post Description.\nInput: "))



    typeChoice = input("Would you like to sort by hot posts (y/n): ")
    while(1):
        if typeChoice == 'y' or typeChoice == 'n':
            break
        print("You inputed ["+ typeChoice + "] ")
        typeChoice = input("Input ERROR\nWould you like to sort by hot posts (y/n): \n")



    subreddit = input("\nWhat Subreddit will you like to Crawl: ")
    reddit = praw.Reddit(client_id=client_Id, client_secret=secret_Id, user_agent='WallstreetCrawler') #Connect to the Wallstreet Reddi API
    while sub_exists(subreddit) == False:               #Makes sure Subreddit exists to begin with
        subreddit = input("Subreddit does not exist. Please input another: ")

    if crawlChoice == 1:
        Posts = dataframeInit(subreddit,typeChoice)        #Initilizes the dataframe using function with given subreddit
        csvOutput = subreddit + '.csv'
        Posts.to_csv(csvOutput)
        print("\nSubreddit has been Crawled! Please go to " + csvOutput + " to view your results\n" )

    if crawlChoice == 2:
        key = input("\nPlease Enter Keyword to Crawl by: ")
        Posts = dataframeInitTitleKey(subreddit,key,typeChoice)

        csvOutput = subreddit + '_' + key + '.csv'  #Creates CSV file for output
        Posts.to_csv(csvOutput)                     #Creates CSV file depending on the KeyWord and Subreddit
        print("\nSubreddit has been Crawled! Please go to " + csvOutput + " to view your results\n" )

    if crawlChoice == 3:
        key = input("\nPlease Enter Keyword to Crawl by: ")
        Posts = dataframeInitPostKey(subreddit,key,typeChoice)

        csvOutput = subreddit + '_' + key + '.csv'  #Creates CSV file for output
        Posts.to_csv(csvOutput)                     #Creates CSV file depending on the KeyWord and Subreddit
        print("\nSubreddit has been Crawled! Please go to " + csvOutput + " to view your results\n" )

    tryAgain = input("\nWould you like to do another subreddit? (y/n): ")

    print("\n\n+++++++++++++++++++++++++++++++++++++++\n")
    while(1):
        if tryAgain == 'y' or tryAgain == 'n':
            break
        print("You inputed ["+ tryAgain + "] ")
        tryAgain = input("INPUT ERROR!\nWould you like to do another subreddit? (y/n): ")

print("Thank you for using my Crawler! Have a good day!\n")



#-----------Main Method-----------#
