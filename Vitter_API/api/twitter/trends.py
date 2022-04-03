import credentials
import tweepy


auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
woeid = 23424787
  
# fetching the trends
trends = api.get_place_trends(id = woeid)
tendencias = []
# printing the information
print("Los top 5 trend de Colombia son:")
  
for value in trends:
    for trend in value['trends']:
        tendencias.append(trend['name'])
count = 0
while count < 5:
    print(tendencias[count])
    count = count + 1    