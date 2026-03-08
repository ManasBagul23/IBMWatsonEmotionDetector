"""
Flask web server for Emotion Detection application.

This server provides a REST API endpoint to analyze text for emotions
using the IBM Watson NLP Emotion Predict API.
"""

from flask import Flask, request, render_template_string
from EmotionDetection import emotion_detector

app = Flask(__name__)


# HTML template for the home page
HOME_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Emotion Detector</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        textarea {
            width: 100%;
            height: 100px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
            resize: vertical;
        }
        button {
            background-color: #0062ff;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }
        button:hover {
            background-color: #0043ce;
        }
        #result {
            margin-top: 20px;
            padding: 15px;
            background-color: #f0f0f0;
            border-radius: 5px;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>IBM Watson Emotion Detector</h1>
        <p>Enter text below to analyze its emotional content:</p>
        <textarea id="textToAnalyze" placeholder="Enter your text here..."></textarea>
        <br>
        <button onclick="analyzeEmotion()">Analyze Emotion</button>
        <div id="result"></div>
    </div>

    <script>
        function analyzeEmotion() {
            const text = document.getElementById('textToAnalyze').value;
            const resultDiv = document.getElementById('result');
            
            if (!text.trim()) {
                resultDiv.innerHTML = 'Please enter some text to analyze.';
                return;
            }
            
            resultDiv.innerHTML = 'Analyzing...';
            
            fetch('/emotionDetector?textToAnalyze=' + encodeURIComponent(text))
                .then(response => response.text())
                .then(data => {
                    resultDiv.innerHTML = data;
                })
                .catch(error => {
                    resultDiv.innerHTML = 'Error: ' + error.message;
                });
        }
    </script>
</body>
</html>
"""


@app.route('/')
def home():
    """Render the home page with the emotion detector form."""
    return render_template_string(HOME_PAGE)


@app.route('/emotionDetector')
def emotion_detector_endpoint():
    """
    Endpoint to analyze text for emotions.

    Query Parameters:
        textToAnalyze (str): The text to analyze for emotions.

    Returns:
        str: A formatted string containing emotion scores and dominant emotion,
             or an error message if the input is invalid.
    """
    # Get the text to analyze from query parameters
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None (invalid input or API error)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Format the response string
    response_text = (
        f"For the given statement, the system response is:\n"
        f"anger: {result['anger']}\n"
        f"disgust: {result['disgust']}\n"
        f"fear: {result['fear']}\n"
        f"joy: {result['joy']}\n"
        f"sadness: {result['sadness']}\n"
        f"The dominant emotion is {result['dominant_emotion']}"
    )

    return response_text


if __name__ == '__main__':
    # Run the Flask development server
    app.run(host='0.0.0.0', port=5000, debug=True)
