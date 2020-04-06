import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

authenticator = IAMAuthenticator('hANWVCyOmDNr7XZbEioKCrj8xv_PrtnPQfNpGRV35oQJ')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.kr-seo.natural-language-understanding.watson.cloud.ibm.com/instances/38a87585-1f8c-480c-a039-09390e1a9750')

response = natural_language_understanding.analyze(
    html="<html><head><title>Fruits</title></head><body><h1>Apples and Oranges</h1><p>I love apples! I don't like oranges.</p></body></html>",
    features=Features(emotion=EmotionOptions(targets=['apples','oranges']))).get_result()

print(json.dumps(response, indent=2))
