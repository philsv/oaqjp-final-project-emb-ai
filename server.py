"""
This module contains the server for the Emotion Detector application.
"""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector() -> str:
    """
    Detects the emotion of a given text using the Watson NLP API.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_dict = emotion_detector(text_to_analyze)

    # sourcery skip: assign-if-exp, reintroduce-else
    if not emotion_dict:
        return "Invalid text! Please try again!"
    return emotion_dict


@app.route("/")
def render_index_page():
    """
    Renders the index.html page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
