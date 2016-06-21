from os import environ
# Twitter API auth
consumer_key = environ.get('CONSUMER_KEY', None)
consumer_secret = environ.get('CONSUMER_SECRET', None)
access_token = environ.get('ACCESS_TOKEN', None)
access_token_secret = environ.get('ACCESS_TOKEN_SECRET', None)
