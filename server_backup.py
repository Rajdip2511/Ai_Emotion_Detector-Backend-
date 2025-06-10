"""
Flask server for Emotion Detection Application.
This module provides a web interface for emotion detection using Watson NLP.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Renders the main index page.

    Returns:
        str: Rendered HTML template
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handles emotion detection requests.

    Returns:
        str: Formatted response with emotion analysis results
    """
    # Get the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Run emotion detection
    response = emotion_detector(text_to_analyze)

    # Handle error cases where dominant_emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response as required
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )

    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) 