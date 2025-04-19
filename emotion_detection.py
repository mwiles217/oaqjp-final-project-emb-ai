import requests,json  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    # url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL of the sentiment analysis service
    # myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    # header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Set the headers required for the API request
    
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    header= { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    formatted_response=json.loads(response.text)
    if response.status_code == 200:
        label=formatted_response["documentSentiment"]["label"]
        score=formatted_response["documentSentiment"]["score"]
    elif response.status_code ==500 or response.status_code==400:
        label=None
        score=None
    return {"label": label, "score": score}
    # return response.text  # Return the response text from the API


    