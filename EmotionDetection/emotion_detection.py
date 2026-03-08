"""
Emotion Detection module using IBM Watson NLP API.

This module provides functionality to analyze text and detect emotions
including anger, disgust, fear, joy, and sadness.
"""

import requests


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the given text using IBM Watson NLP API.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores (anger, disgust, fear,
              joy, sadness) and the dominant_emotion. Returns None values
              for all keys if the input is blank or API returns an error.
    """
    # Handle empty or blank input
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # IBM Watson NLP API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Required headers for the API
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Request payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Make POST request to the API
        response = requests.post(url, headers=headers, json=payload, timeout=30)

        # Handle non-200 response codes
        if response.status_code != 200:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        # Parse the JSON response
        response_json = response.json()

        # Extract emotion predictions from the response
        # The API returns emotions in emotionPredictions[0].emotion
        emotions = response_json.get('emotionPredictions', [{}])[0].get('emotion', {})

        # Extract individual emotion scores
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)

        # Create emotion dictionary for finding dominant emotion
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }

        # Find the dominant emotion (the one with highest score)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return the result dictionary
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

    except requests.exceptions.RequestException:
        # Handle any request exceptions
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
