# https://viettelgroup.ai/dashboard/service/texttospeech

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import the json library
import json
import requests
import urllib

url = "https://viettelgroup.ai/voice/api/tts/v1/rest/syn"
data = {"text": "xin chào cô chú, xin chào các bạn", 
        "voice": "hcm-minhquan", 
        "id": "2", 
        "without_filter": False, 
        "speed": 1.0, 
        "tts_return_option": 2}
headers = {'Content-type': 'application/json', 
           'token': '4l-KaeR8YpTRGWQc2nFIOGOlAdeQN38JDCcesCjCmB9-3C1FlHaKuYGQgrpvvfGu'}
response = requests.post(url, data=json.dumps(data), headers=headers)
#if encounter SSL error because of https certificate, please comment out above line and use the line below to  make insecure connections   (this will expose your application to security risks, such as man-in-the-middle attacks.)
#response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
# Headers is a dictionary
print(response.headers)
# Get status_code.
print(response.status_code)
# Get the response data as a python object.
data = response.content
f = open("ViettelAPI_output/tanpk.wav", "wb")
f.write(data)
f.close()
