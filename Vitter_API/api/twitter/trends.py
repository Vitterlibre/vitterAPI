import random
import string
import tweepy
import credentials
import tweepy
import time
import sys
import json

auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# WOEID of Colombia
woeid = 23424787
  
# fetching the trends
trends = api.get_place_trends(id = woeid)
tendencias = []
alphabet = string.ascii_lowercase + string.digits
   
for value in trends:
    for trend in value['trends']:
        tendencias.append({'id':''.join(random.choices(alphabet, k=8)), 'trend':trend['name']},)

json_object = json.dumps(tendencias, indent= 4)



