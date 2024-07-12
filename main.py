import tweepy
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_user_info():
    user = api.me()
    print(f'Name: {user.name}')
    print(f'Screen Name: {user.screen_name}')
    print(f'Followers Count: {user.followers_count}')

def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)

def follow_users(target_name):
    for follower in limit_handle(tweepy.Cursor(api.followers).items()):
        if follower.name == target_name:
            print(f'Following {follower.name}')
            follower.follow()

def like_tweets(search_term, number_of_tweets):
    for tweet in tweepy.Cursor(api.search, q=search_term).items(number_of_tweets):
        try:
            tweet.favorite()
            print(f'Liked the tweet: {tweet.text}')
        except tweepy.TweepError as e:
            print(f'Error: {e.reason}')
        except StopIteration:
            break

if __name__ == "__main__":
    get_user_info()
    
    # Change 'Usernamehere' to the actual username you want to follow
    follow_users('Usernamehere')
    
    # Change 'dhiya' and 2 to the actual search term and number of tweets you want to like
    like_tweets('dhiya', 2)
