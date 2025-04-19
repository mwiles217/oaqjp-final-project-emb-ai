""" 
    Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app=Flask(__name__)
@app.route("/emotionDetector")
def emotion_analyzer():
    """
        Emotion Analyzer texts text as input and finds scored for a range of emotions
        anger,disgust,fear,sadness 
        and returns the dominant emotion
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['anger'] is None:
        return "Invalid text! Please try again!"

    fs=f"For the given statement, the system response is 'anger':  {response['anger']}"  + \
    f" 'disgust': {response['disgust']}, 'fear': {response['fear']}" + \
    f", 'joy': {response['joy']} and 'sadness': {response['sadness']}." + \
    f" The dominant emotion is <b>{response['dominant_emotion']}</b>."
    return fs
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
