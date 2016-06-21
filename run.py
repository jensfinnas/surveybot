
from modules.twitterbot import TwitterBot
from modules.streamlistener import MentionListener
from config import access_token, access_token_secret, consumer_key, consumer_secret
import tweepy

x = TwitterBot("twine-parser/result.json",
    image_folder="assets/images/",
    access_token=access_token,
    access_token_secret=access_token_secret,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret)


mentionlistener = MentionListener
myStream = tweepy.Stream(auth = x.twitter.auth, listener=mentionlistener(x))
myStream.filter(track=[x.twitter_handle])

