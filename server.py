from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, extract_emotion

app = Flask(__name__)

@app.route("/")
def index():
    """
    Renders the homepage where the user can input text for emotion detection.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyzes the user-provided text for emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')
    if not text_to_analyze:
        return "Please provide text for emotion analysis."

    response = emotion_detector(text_to_analyze)
    formatted_response = extract_emotion(response)

    if formatted_response['dominant_emotion'] is None:
        return "No valid emotion detected. Please try again."

    return (
        f"Detected emotions: Anger: {formatted_response['anger']}, "
        f"Disgust: {formatted_response['disgust']}, Fear: {formatted_response['fear']}, "
        f"Joy: {formatted_response['joy']}, Sadness: {formatted_response['sadness']}. "
        f"Dominant emotion: {formatted_response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)