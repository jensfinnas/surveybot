# encoding: utf-8

import tweepy

class MentionListener(tweepy.StreamListener):
    def __init__(self, surveybot):
        super(MentionListener, self).__init__()
        self.surveybot = surveybot

    def on_status(self, status):
        self.surveybot.react_to_mention(status)
        