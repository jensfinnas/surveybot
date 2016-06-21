
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
"""

mentions = x.twitter.mentions_timeline()


for mention in reversed(mentions):
    print "*********"
    print mention.user.screen_name, mention.text, x._has_reply(mention)
    x.interpret_mention(mention)

"""

x.say(x.statements[-2])

"""
mentionlistener = MentionListener
myStream = tweepy.Stream(auth = x.twitter.auth, listener=mentionlistener(x))
myStream.filter(track=['askchartbot'])
"""