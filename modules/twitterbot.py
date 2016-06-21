import tweepy
from surveybot import SurveyBot
from statement import Statement
from response import Response
import re
import pdb

class TwitterBot(SurveyBot):
    """ A twitter 
    """
    def __init__(self,
        statement_tree_source,
        image_folder="",
        access_token=None,
        access_token_secret=None,
        consumer_key=None,
        consumer_secret=None):

        super(TwitterBot, self).__init__(statement_tree_source, image_folder=image_folder)
        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.twitter = tweepy.API(auth)
        self.twitter_handle = self.twitter.me().screen_name

    def say(self, statement, *args, **kwargs):
        """ Make a status update.
            Pass 
        """
        user = ""
        in_reply_to_status_id = None
        if "reply_to" in kwargs:
            user_status = kwargs["reply_to"]
            user = "@" + user_status.user.screen_name + " "
            in_reply_to_status_id = user_status.id

        status_text = user + statement.body

        print "**** NEW TWEET ****"
        print status_text
        print "********************"

        if statement.image:
            self.twitter.update_with_media(statement.image, status=status_text, in_reply_to_status_id=in_reply_to_status_id)
        else:
            self.twitter.update_status(status_text, in_reply_to_status_id=in_reply_to_status_id)

    def reply(self, user_status):
        """ Reply to a tweet by a user
        """
        if not self._has_reply(user_status) and not user_status.user.screen_name == u"askchartbot":
            # What was the previous statement of the bot?
            statement_history = self._get_statement_history(user_status)
            if len(statement_history) > 0:
                last_statement = statement_history[-1]

                user_input = self._clean_tweet(user_status.text)
                resp = last_statement.interpret(user_input)

                if isinstance(resp, Statement):
                    self.say(resp, reply_to=user_status)

                elif isinstance(resp, Response):
                    if resp.next_statement:
                        next_statement = self._get_statement_by_id(resp.next_statement)
                        self.say(next_statement, reply_to=user_status)
            else:
                self.start_conversation(reply_to=user_status)


    def _clean_tweet(self, tweet_text):
        # Remove twitter handles 
        tweet_text = re.sub("@([A-Za-z]+[A-Za-z0-9]+)", '', tweet_text)

        return tweet_text.strip()

    def _get_statement_history(self, status):
        """ Get a list of statements preceeding a status
            Will only return statements that are in the conversaiton tree
            (and ignore "didn't understand" responses)
        """
        status_history = []
        statement_history = []

        # Get the previous tweets of the bot in the conversation 
        while status.in_reply_to_status_id:
            status = self.twitter.get_status(status.in_reply_to_status_id)
            if status.user.screen_name == self.twitter_handle:
                status_history.append(status)
        
        for status in reversed(status_history):
            status_text = self._clean_tweet(status.text)
            statement = self._get_statement_by_text(status_text)
            if statement:
                if statement.in_tree():
                    statement_history.append(statement)

        return statement_history

    def _has_reply(self, user_status):
        """ Check if the bot as already replied to a  status from a user
        """
        if not hasattr(self, "timeline"):
            self.timeline = self.twitter.home_timeline()

        return len([x for x in self.timeline if x.in_reply_to_status_id == user_status.id]) > 0

    def react_to_mention(self, status):
        if status.in_reply_to_screen_name == self.twitter_handle:
            # Someone responded to me!
            self.reply(status)
            
        else:
            # This is a new conversation
            self.start_conversation(reply_to=status)

