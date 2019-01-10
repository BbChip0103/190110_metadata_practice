import requests
import json

import sys
sys.path.append('../../METADATA')
import METADATA

params = {
    'visualFeatures': 'Description',
    'language': 'en'
}
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': METADATA.VISION_KEY
}
data = {
    'url':'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Classroom.jpeg/350px-Classroom.jpeg'
}

res = requests.post('https://koreacentral.api.cognitive.microsoft.com/vision/v1.0/analyze',
                        params=params, headers=headers, json=data)

res_dict = json.loads(res.text)
subscribed_text = res_dict['description']['captions'][0]['text']

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': 'ko'
}
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': METADATA.TRANSLATE_KEY
}
data = [{
    'text':subscribed_text
}]

res = requests.post('https://api.cognitive.microsofttranslator.com/translate',
                        params=params, headers=headers, json=data)

res_dict = json.loads(res.text)
result = res_dict[0]['translations'][0]['text']
print(result)