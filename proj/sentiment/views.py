import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions


from django.shortcuts import render
from django.http import HttpResponse
import tweepy
import re



def home(request):
    return  render(request, 'index.html')

def result(request):
    auth = tweepy.OAuthHandler('', '')
    auth.set_access_token('', '')
    api = tweepy.API(auth)
    query = request.GET['query']
    data = ''
    for tweet in tweepy.Cursor(api.search, q=query).items(1):
        data=data+tweet.text
        print(tweet.text)
    authenticator = IAMAuthenticator('')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
    )

    natural_language_understanding.set_service_url('')
    data = re.sub(
    r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', data)
    data = re.sub('[^A-Za-z0-9\s]+', '', data)
    data = re.sub('@', '', data)
    data = data.lower()
    print(data)
    response = natural_language_understanding.analyze(
    text=data,
    features=Features(emotion=EmotionOptions()),language='en').get_result()
    s=response['emotion']['document']['emotion']
    for i in s:
        s[i]="{:.2f}".format(abs(float(s[i])*100))
    return render(request,'result.html',s)


