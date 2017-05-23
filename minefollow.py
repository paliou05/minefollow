   
import tweepy

auth = tweepy.OAuthHandler("KKwsfmkUMpv8ag7ptJPui5Xp8", "w6Fx0fPl7rfNayZXPgQ3crIAsWaNaENmtQJZJSnGgLJtoWs1Wt")
auth.set_access_token("4178185372-Eq4HWoHZtOu1e8uizQhvEKF8ylRAqmBAf7zN2LK", "cC7RTyjoeQr68zAd1Dq6lhtnwAUO6AUQO2GUZow8EdKBC")

api = tweepy.API(auth)

first_tweet = api.user_timeline("paliourg")

retweet = first_tweet[0]
retweet_id = retweet.retweeted_status.id
original_tweet = api.get_status(retweet_id)
print original_tweet




