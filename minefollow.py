   
import tweepy

auth = tweepy.OAuthHandler("KKwsfmkUMpv8ag7ptJPui5Xp8", "w6Fx0fPl7rfNayZXPgQ3crIAsWaNaENmtQJZJSnGgLJtoWs1Wt")
auth.set_access_token("4178185372-Eq4HWoHZtOu1e8uizQhvEKF8ylRAqmBAf7zN2LK", "cC7RTyjoeQr68zAd1Dq6lhtnwAUO6AUQO2GUZow8EdKBC")

api = tweepy.API(auth)
#Get paliourg timeline
first_tweet = api.user_timeline("paliourg")
#Get the first tweet of the timeline
retweet = first_tweet[0]
#Get the id of the original tweet that retweeted
retweet_id = retweet.retweeted_status.id_str
#Get the original tweet
original_tweet = api.get_status(retweet_id)
#print original_tweet

#Get the retweeted ids
retweet_ids = api.retweets(original_tweet.id)
print retweet_ids
#Get the profiles from the ids




