import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

#this function converts english text to french
def english_to_french(englishText):
    #write the code here
    translation_fr = language_translator.translate(text= englishText, model_id='en-fr').get_result()
    frenchText =translation_fr['translations'][0]['translation']
    return frenchText

#this function conversts french text from the previous function to english
def french_to_english(frenchText):
    #write the code here
    translation_eng = language_translator.translate(text=frenchText ,model_id='fr-en').get_result()
    englishText = translation_eng['translations'][0]['translation']
    return englishText
