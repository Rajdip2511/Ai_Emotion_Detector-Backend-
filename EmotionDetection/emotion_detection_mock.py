import json
import random

def emotion_detector_mock(text_to_analyze):
    """
    Mock emotion detector for demonstration purposes.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion
    """
    
    # Handle empty or None input
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Predefined responses for specific test cases
    test_responses = {
        "I am glad this happened": {
            'anger': 0.002,
            'disgust': 0.001,
            'fear': 0.003,
            'joy': 0.89,
            'sadness': 0.104,
            'dominant_emotion': 'joy'
        },
        "I am really mad about this": {
            'anger': 0.91,
            'disgust': 0.02,
            'fear': 0.01,
            'joy': 0.03,
            'sadness': 0.03,
            'dominant_emotion': 'anger'
        },
        "I feel disgusted just hearing about this": {
            'anger': 0.15,
            'disgust': 0.78,
            'fear': 0.02,
            'joy': 0.01,
            'sadness': 0.04,
            'dominant_emotion': 'disgust'
        },
        "I am so sad about this": {
            'anger': 0.02,
            'disgust': 0.01,
            'fear': 0.05,
            'joy': 0.02,
            'sadness': 0.90,
            'dominant_emotion': 'sadness'
        },
        "I am really afraid that this will happen": {
            'anger': 0.01,
            'disgust': 0.02,
            'fear': 0.88,
            'joy': 0.01,
            'sadness': 0.08,
            'dominant_emotion': 'fear'
        },
        "I love this new technology.": {
            'anger': 0.006274985,
            'disgust': 0.0025598293,
            'fear': 0.009251528,
            'joy': 0.9680386,
            'sadness': 0.049744144,
            'dominant_emotion': 'joy'
        },
        "I am so happy I am doing this.": {
            'anger': 0.001,
            'disgust': 0.001,
            'fear': 0.002,
            'joy': 0.985,
            'sadness': 0.011,
            'dominant_emotion': 'joy'
        },
        "I hate working long hours.": {
            'anger': 0.75,
            'disgust': 0.15,
            'fear': 0.02,
            'joy': 0.01,
            'sadness': 0.07,
            'dominant_emotion': 'anger'
        },
        "I think I am having fun": {
            'anger': 0.01,
            'disgust': 0.01,
            'fear': 0.02,
            'joy': 0.92,
            'sadness': 0.04,
            'dominant_emotion': 'joy'
        }
    }
    
    # Check if we have a predefined response
    if text_to_analyze in test_responses:
        return test_responses[text_to_analyze]
    
    # Generate semi-realistic random emotions based on keywords
    emotions = {
        'anger': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'joy': 0.0,
        'sadness': 0.0
    }
    
    text_lower = text_to_analyze.lower()
    
    # Simple keyword-based emotion detection
    if any(word in text_lower for word in ['happy', 'joy', 'love', 'great', 'awesome', 'wonderful', 'amazing', 'excellent', 'fantastic', 'fun']):
        emotions['joy'] = random.uniform(0.7, 0.95)
        emotions['anger'] = random.uniform(0.001, 0.05)
        emotions['sadness'] = random.uniform(0.001, 0.05)
        emotions['fear'] = random.uniform(0.001, 0.05)
        emotions['disgust'] = random.uniform(0.001, 0.05)
    elif any(word in text_lower for word in ['angry', 'mad', 'hate', 'furious', 'annoyed', 'irritated']):
        emotions['anger'] = random.uniform(0.7, 0.95)
        emotions['joy'] = random.uniform(0.001, 0.05)
        emotions['sadness'] = random.uniform(0.001, 0.1)
        emotions['fear'] = random.uniform(0.001, 0.05)
        emotions['disgust'] = random.uniform(0.001, 0.1)
    elif any(word in text_lower for word in ['sad', 'depressed', 'unhappy', 'miserable', 'disappointed']):
        emotions['sadness'] = random.uniform(0.7, 0.95)
        emotions['joy'] = random.uniform(0.001, 0.05)
        emotions['anger'] = random.uniform(0.001, 0.05)
        emotions['fear'] = random.uniform(0.001, 0.1)
        emotions['disgust'] = random.uniform(0.001, 0.05)
    elif any(word in text_lower for word in ['afraid', 'scared', 'fearful', 'terrified', 'worried', 'anxious']):
        emotions['fear'] = random.uniform(0.7, 0.95)
        emotions['joy'] = random.uniform(0.001, 0.05)
        emotions['anger'] = random.uniform(0.001, 0.05)
        emotions['sadness'] = random.uniform(0.001, 0.1)
        emotions['disgust'] = random.uniform(0.001, 0.05)
    elif any(word in text_lower for word in ['disgusted', 'disgusting', 'gross', 'revolting', 'repulsive']):
        emotions['disgust'] = random.uniform(0.7, 0.95)
        emotions['joy'] = random.uniform(0.001, 0.05)
        emotions['anger'] = random.uniform(0.001, 0.1)
        emotions['sadness'] = random.uniform(0.001, 0.05)
        emotions['fear'] = random.uniform(0.001, 0.05)
    else:
        # Neutral text - distribute emotions more evenly
        emotions['joy'] = random.uniform(0.2, 0.4)
        emotions['anger'] = random.uniform(0.1, 0.2)
        emotions['sadness'] = random.uniform(0.1, 0.2)
        emotions['fear'] = random.uniform(0.1, 0.2)
        emotions['disgust'] = random.uniform(0.1, 0.2)
    
    # Normalize emotions to sum to approximately 1
    total = sum(emotions.values())
    for emotion in emotions:
        emotions[emotion] = emotions[emotion] / total
    
    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    } 