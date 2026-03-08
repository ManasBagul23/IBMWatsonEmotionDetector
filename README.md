# IBM Watson Emotion Detector

A Python application that uses IBM Watson Natural Language Processing (NLP) API to detect emotions in text. The application analyzes text and identifies five emotions: anger, disgust, fear, joy, and sadness, along with determining the dominant emotion.

## Project Description

This project implements an Emotion Detection system using the IBM Watson NLP Emotion Predict API. It includes:

- **EmotionDetection Package**: A Python package containing the core emotion detection functionality
- **Flask Web Server**: A REST API server that provides an endpoint for emotion analysis
- **Web Interface**: A simple HTML interface for users to input text and view results
- **Unit Tests**: Comprehensive test cases for the emotion detection functionality

### Features

- Detect five emotions: anger, disgust, fear, joy, and sadness
- Identify the dominant emotion in the text
- RESTful API endpoint for integration with other applications
- User-friendly web interface
- Error handling for invalid inputs and API failures

## Project Structure

```
├── EmotionDetection/
│   ├── __init__.py           # Package initialization
│   └── emotion_detection.py  # Core emotion detection logic
├── server.py                 # Flask web server
├── test_emotion_detection.py # Unit tests
└── README.md                 # Project documentation
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone or download this project to your local machine

2. Navigate to the project directory:
   ```bash
   cd "Python Project for AI & Application Development"
   ```

3. Install required dependencies:
   ```bash
   pip install flask requests
   ```

## Running the Flask Server

1. Start the server:
   ```bash
   python server.py
   ```

2. The server will start on `http://localhost:5000`

3. Open your web browser and navigate to `http://localhost:5000` to access the web interface

## API Endpoint

### Emotion Detector

**Endpoint:** `/emotionDetector`

**Method:** GET

**Query Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| textToAnalyze | string | The text to analyze for emotions |

**Example Request:**
```
GET /emotionDetector?textToAnalyze=I%20am%20so%20happy%20today!
```

**Example Response:**
```
For the given statement, the system response is:
anger: 0.006456153
disgust: 0.0022938042
fear: 0.009445951
joy: 0.9726568
sadness: 0.053292502
The dominant emotion is joy
```

### Using cURL

```bash
curl "http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20so%20happy%20today!"
```

### Using Python requests

```python
import requests

url = "http://localhost:5000/emotionDetector"
params = {"textToAnalyze": "I am so happy today!"}
response = requests.get(url, params=params)
print(response.text)
```

## Running Tests

Run the unit tests using the following command:

```bash
python -m unittest test_emotion_detection.py
```

Or with verbose output:

```bash
python -m unittest test_emotion_detection.py -v
```

### Test Cases

The test suite includes the following test cases:

| Test | Description |
|------|-------------|
| `test_joy` | Tests detection of joy emotion |
| `test_anger` | Tests detection of anger emotion |
| `test_sadness` | Tests detection of sadness emotion |
| `test_fear` | Tests detection of fear emotion |
| `test_disgust` | Tests detection of disgust emotion |
| `test_empty_input` | Tests handling of empty input |
| `test_blank_input` | Tests handling of whitespace-only input |
| `test_response_structure` | Validates response dictionary structure |
| `test_emotion_scores_are_numbers` | Validates emotion scores are numeric |

## Using the EmotionDetection Package Directly

You can also use the EmotionDetection package directly in your Python code:

```python
from EmotionDetection import emotion_detector

# Analyze text
result = emotion_detector("I am feeling great today!")

# Access individual emotion scores
print(f"Joy: {result['joy']}")
print(f"Anger: {result['anger']}")
print(f"Sadness: {result['sadness']}")
print(f"Fear: {result['fear']}")
print(f"Disgust: {result['disgust']}")
print(f"Dominant Emotion: {result['dominant_emotion']}")
```

## Error Handling

The application handles the following error scenarios:

1. **Empty or blank input**: Returns `None` for all emotion values
2. **API errors**: Returns `None` for all emotion values when API returns non-200 status
3. **Network errors**: Returns `None` for all emotion values on connection failures

## IBM Watson NLP API

This application uses the IBM Watson NLP Emotion Predict API:

- **Endpoint**: `https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict`
- **Model**: `emotion_aggregated-workflow_lang_en_stock`

## License

This project is created for educational purposes as part of the IBM Full Stack Development course.

## Acknowledgments

- IBM Watson NLP Services
- IBM Skills Network Labs
