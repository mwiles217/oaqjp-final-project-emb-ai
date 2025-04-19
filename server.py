''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request #from the flask pramework package : TODO
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app=Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    if label is None:
        return "Invalid text! Please Try Again!"
    else:
        # Return a formatted string with the sentiment label and score
        return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
