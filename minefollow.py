   
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

#Get the retweeted screen_names
retweet_ids = api.retweets(original_tweet.id)
for i in retweet_ids:
    
    retweeters = i.author.screen_name
    print retweeters
    users_ids = api.get_user(screen_name=retweeters)
    print users_ids.id
    #Check in retweeters for followers
    
    followers = api.followers(screen_name=retweeters)
    status = followers[0]
    
    follower_ids = status[u'id']
    follower_ids.encode('utf-8')
    follower_ids.decode('unicode')
    print follower_ids
    """for j in followers:
        if followers.id==users_ids.id:
            print "its a match"
        else:
            print "no match" """

        



