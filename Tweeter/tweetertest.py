import tweepy

auth = tweepy.OAuthHandler('', ')
auth.set_access_token('', '')

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#Trump').items(5):
    print("========================================================================")
    print('{real_name} (@{name}) said {tweet}\n\n'.format(
        real_name=tweet.author.name, name=tweet.author.screen_name,
        tweet=tweet.text))
