from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    if request.method == 'POST':
        text = request.form['text']
    else:  # GET method
        text = request.args.get('textToAnalyze')
    result = emotion_detector(text)

    if 'error' in result:
        return jsonify({'error': result['error']}), 500
    
    response_string = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}.")

    return response_string

if __name__ == '__main__':
    app.run(debug=True)