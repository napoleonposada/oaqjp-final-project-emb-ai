'''
This module do emotion detection using Watson NLP
2024-08-18
'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''
    This function do emotion detection using Watson NLP
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header, timeout=180)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        dict_response = formatted_response['emotionPredictions']
        dict_emotions = dict_response[0]['emotion']
        emotion = None
        score_emotion = 0.0
        for key, value in dict_emotions.items():
            if value > score_emotion:
                score_emotion = value
                emotion = key 
        dict_emotions['dominant_emotion'] = emotion 
    elif response.status_code == 400:
        dict_emotions = {'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}
    else:
        dict_emotions = None

    return dict_emotions

