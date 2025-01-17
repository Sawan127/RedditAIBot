import os
from dotenv import load_dotenv
import praw

## Load the environment variables
load_dotenv()

## Set the Reddit Instance variable

def get_reddit_instance():
    """ Authenticates with the Reddit API and returns the Reddit instance """
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent='RedditAI-Bot/1.0'
    )
    return reddit

## Test Connections
if __name__ == "__main__":
    reddit = get_reddit_instance()
    print(f"Authenticated with Reddit as: {reddit.user.me()}")
    
