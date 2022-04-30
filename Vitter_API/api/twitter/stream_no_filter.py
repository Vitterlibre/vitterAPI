 
from unicodedata import name
import tweepy
import credentials
import tweepy
import time
import sys
import json
import string
import random

auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

alphabet = string.ascii_lowercase + string.digits

# Create API object
api = tweepy.API(auth)

def limpiar_acentos(text):
	acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'E': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
	for acen in acentos:
		if acen in text:
			text = text.replace(acen, acentos[acen])
	return text

tweets = []

class MyListener(tweepy.Stream):
    def on_status(self, status):
        tweets.append({'id':''.join(random.choices(alphabet, k=8))
        ,'author_name':status.author.screen_name
        ,'tweet_text':limpiar_acentos(status.text)
        ,'tweet_date':str(status.created_at)
        ,"tweet_source" :status.source
        ,"tweet_location": limpiar_acentos(str(status.user.location))
        ,"tweet_coordinates":str(status.place.bounding_box.coordinates)
        ,'Lugar':limpiar_acentos(status.place.full_name)
        ,'Latitud':(((str(status.place.bounding_box.coordinates)).replace('[','')).replace(']',''))[12:20]
        ,'Longitud':(((str(status.place.bounding_box.coordinates)).replace('[','')).replace(']',''))[:9]})
        if len(tweets) == 10:
          json_object = json.dumps(tweets, indent= 4)
          print(json_object)
          sys.exit()

    def on_error(self, status):        
        print (status)
        if status == 420:
            print ("Reconectando... ")
            return False
        sys.exit()    
 
twitter_stream = MyListener(
  "GWKSI2kfcwEk3fgsyL8goCyRi", "FeInnXNKDiX8BAgaV8WDKw18RGbOi7MdBqqDUDG1quilcVm8on",
  "1476021417116327937-CNQmH7KaeAdejjIaA3W8O8aw7g5NpG", "lWVNeBGhDlr4Hy9fd6diF0fVLCAVdbKt9bE1Ovn57j0Ui"
)
# for value in trends:
#     for trend in value['trends']:
#         twitter_stream.filter(track=trend['name'],languages='es',filter_level='medium')
#twitter_stream.filter(track='Bogota',languages = ["es"],locations=[-78.8474730429,-2.0337756537,-67.9637787173,12.0054938177])
twitter_stream.filter(languages = ["es"],locations=[-77.4000522034,-0.4666495827,-69.087285033,10.9538219117])

