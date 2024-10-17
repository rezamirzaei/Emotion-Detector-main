import os
from dotenv import load_dotenv
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

def emotion_detector(text):
    """
    Sends text to the Watson Emotion Detection API using IBM Watson SDK.
    """
    load_dotenv('passwords.env')
    api_key = os.getenv('API_KEY')
    url = os.getenv('SERVICE_URL')

    if not api_key or not url:
        raise ValueError("API Key or URL is missing from the environment variables")

    # Replace {apikey} and {service_url} with your actual IBM Cloud API key and service URL
    authenticator = IAMAuthenticator(api_key)  # Your actual API key
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(url)

    # Analyze the emotions in the text
    try:
        response = natural_language_understanding.analyze(
            text=text,
            features=Features(emotion=EmotionOptions(document=True))
        ).get_result()

        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def extract_emotion(emotion_data):
    """
    Processes the API response and extracts emotions from it.
    """
    if not emotion_data:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotions = emotion_data['emotion']['document']['emotion']

    # Extract individual emotions
    anger = emotions.get('anger', 0)
    disgust = emotions.get('disgust', 0)
    fear = emotions.get('fear', 0)
    joy = emotions.get('joy', 0)
    sadness = emotions.get('sadness', 0)

    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
