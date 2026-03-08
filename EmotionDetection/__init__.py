"""
EmotionDetection package for IBM Watson NLP Emotion Analysis.

This package provides functionality to detect emotions in text using
the IBM Watson NLP Emotion Predict API.
"""

from .emotion_detection import emotion_detector

__all__ = ['emotion_detector']
__version__ = '1.0.0'
