import tweepy

auth = tweepy.OAuthHandler('awhd0FTt5WJOY1NfckYAvqseU', 'p4mFuUK9RpfgLMZ8HYj9EnMS99oJ2WmWQpY1rkbdyIPLzIdZm1')
auth.set_access_token('1215597718413836288-0cXv5KvZJuqM8SiHKWfNobjRmvSIjb', 'MISbW379sRaCN9hjQNpUpfgKmSifzy0zh3qyarjdvGS37')

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#Trump').items(5):
    print("========================================================================")
    print('{real_name} (@{name}) said {tweet}\n\n'.format(
        real_name=tweet.author.name, name=tweet.author.screen_name,
        tweet=tweet.text))