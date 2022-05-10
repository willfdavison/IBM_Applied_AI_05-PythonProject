import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(authenticator=authenticator)
translator.set_service_url(url)


def englishToFrench(englishText):
    #Translate text
    translation = translator.Translate(text=englishText, model_id='en-fr').get_result()
    #Obtain string from returned list
    frenchText = translation['translations'][0]['translation']
    #Return translated string
    return frenchText

def frenchToEnglish(frenchText):
    #Translate text
    translation = translator.Translate(text=frenchText, model_id='fr-en').get_result()
    #Obtain string from returned list
    englishText = translation['translations'][0]['translation']
    #Return translated string
    return englishText
