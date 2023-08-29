"""
Pytest file for testing the emotion_detection.py file.
"""

import pytest
from EmotionDetection.emotion_detection import emotion_detector


@pytest.mark.parametrize(
    "text, expected",
    [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear"),
    ],
)
def test_emotion_detector(text, expected):
    """
    Tests the emotion_detector function.
    """
    result = emotion_detector(text)
    assert result["dominant_emotion"] == expected
