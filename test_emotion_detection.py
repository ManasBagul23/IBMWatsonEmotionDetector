"""
Unit tests for the Emotion Detection module.

This module contains test cases for testing the emotion_detector function
with various input sentences that trigger different emotions.
"""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test class for emotion_detector function."""

    def test_joy(self):
        """
        Test that a joyful statement returns 'joy' as dominant emotion.
        """
        result = emotion_detector("I am so happy and excited about this wonderful day!")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """
        Test that an angry statement returns 'anger' as dominant emotion.
        """
        result = emotion_detector("I am really furious about this terrible situation!")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_sadness(self):
        """
        Test that a sad statement returns 'sadness' as dominant emotion.
        """
        result = emotion_detector("I am so sad and heartbroken about losing my friend.")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """
        Test that a fearful statement returns 'fear' as dominant emotion.
        """
        result = emotion_detector("I am terrified and scared of the dark shadows.")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_disgust(self):
        """
        Test that a disgusted statement returns 'disgust' as dominant emotion.
        """
        result = emotion_detector("I feel disgusted and nauseated by this repulsive behavior.")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_empty_input(self):
        """
        Test that empty input returns None for all emotions.
        """
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])

    def test_blank_input(self):
        """
        Test that blank/whitespace input returns None for all emotions.
        """
        result = emotion_detector("   ")
        self.assertIsNone(result['dominant_emotion'])

    def test_response_structure(self):
        """
        Test that the response contains all required keys.
        """
        result = emotion_detector("This is a test sentence.")
        required_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)

    def test_emotion_scores_are_numbers(self):
        """
        Test that emotion scores are numeric values when valid input is provided.
        """
        result = emotion_detector("I love this beautiful sunny day!")
        if result['dominant_emotion'] is not None:
            self.assertIsInstance(result['anger'], (int, float))
            self.assertIsInstance(result['disgust'], (int, float))
            self.assertIsInstance(result['fear'], (int, float))
            self.assertIsInstance(result['joy'], (int, float))
            self.assertIsInstance(result['sadness'], (int, float))


if __name__ == '__main__':
    unittest.main()
