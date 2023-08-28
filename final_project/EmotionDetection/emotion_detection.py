"""
This module contains the function that detects the emotion of a given text using the Watson NLP API.
"""

import json

import requests


def emotion_detector(text_to_analyse: str) -> dict | None:
    """
    Detects the emotion of a given text using the Watson NLP API.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    if not text_to_analyse.strip():
        return None

    data = {"raw_document": {"text": text_to_analyse}}
    response_data = requests.post(url, headers=headers, data=json.dumps(data), timeout=10)
    json_resonse = response_data.json()
    emotions = json_resonse["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion

    # sourcery skip: assign-if-exp, reintroduce-else
    if response_data.status_code == 400:
        return None
    return emotions


if __name__ == "__main__":
    response = emotion_detector("I am so happy")
    print(response)
