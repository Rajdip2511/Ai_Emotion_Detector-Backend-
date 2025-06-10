"""
Basic test script for emotion detection functionality
"""

from EmotionDetection import emotion_detector

def test_basic_functionality():
    """Test basic emotion detection functionality"""
    
    # Test with a happy statement
    result = emotion_detector("I love this new technology.")
    print(f"Test 1 - Happy statement:")
    print(f"Result: {result}")
    print(f"Dominant emotion: {result.get('dominant_emotion', 'None')}")
    print()
    
    # Test with a sad statement
    result = emotion_detector("I am so sad about this.")
    print(f"Test 2 - Sad statement:")
    print(f"Result: {result}")
    print(f"Dominant emotion: {result.get('dominant_emotion', 'None')}")
    print()
    
    # Test with an angry statement
    result = emotion_detector("I am really mad about this.")
    print(f"Test 3 - Angry statement:")
    print(f"Result: {result}")
    print(f"Dominant emotion: {result.get('dominant_emotion', 'None')}")
    print()

if __name__ == "__main__":
    print("Testing Emotion Detection Package...")
    print("=" * 50)
    test_basic_functionality()
    print("Testing completed!") 