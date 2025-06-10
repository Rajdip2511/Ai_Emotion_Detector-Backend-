import requests
import json
from .emotion_detection_mock import emotion_detector_mock

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP API.
    Falls back to mock function if API is not accessible.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion
    """
    # Handle potential errors
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    try:
        # URL for Watson NLP Emotion Predict function
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        
        # Headers required for the API
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        
        # Input json format
        myobj = {"raw_document": {"text": text_to_analyze}}
        
        # Make the POST request with short timeout
        response = requests.post(url, json=myobj, headers=headers, timeout=3)
        
        # Handle potential errors
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        
        # Parse the JSON response
        response_dict = json.loads(response.text)
        
        # Extract emotions from the response
        emotions = response_dict['emotionPredictions'][0]['emotion']
        
        # Extract individual emotion scores
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        
        # Find the dominant emotion (emotion with highest score)
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return the formatted output
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    except (requests.exceptions.RequestException, requests.exceptions.Timeout, 
            KeyError, json.JSONDecodeError, Exception):
        # If Watson API fails, use mock function for demonstration
        print("Watson API not accessible, using mock function for demonstration...")
        return emotion_detector_mock(text_to_analyze) 