import requests,json  # Import the requests library to handle HTTP requests
def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)    
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response=json.loads(response.text)
    if response.status_code ==500 or response.status_code==400:
        return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
        }

    em=formatted_response["emotionPredictions"][0]["emotion"]
    dom:str=""
    dv:float=0
    for k,v in em.items():
        if len(dom)==0:
            dom=k
            dv=float(v)
            continue
        if float(v)>float(dv):
            dom=k
            dv=float(v)
    em["dominant_emotion"]=dom

    return em

    # return response.text  # Return the response text from the API


    