import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1
import Features
import SentimentOptions

authenticator = IAMAuthenticator('{apikey}')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('{url}')

response = natural_language_understanding.analyze(
    url='www.wsj.com/news/markets',
    features=Features(sentiment=SentimentOptions(targets=['stocks']))).get_result()

print(json.dumps(response, indent=2))
