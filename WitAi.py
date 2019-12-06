import urllib.request
import json


def recognize(data):
    api = 'https://api.wit.ai/speech'
    api_key = 'PS7JLNHQ22G3IPWIQYZ7BQ6LHZ3WFRTV'
    headers = {
                'Accept': 'audio/x-mpeg-3',
                'Authorization': 'Bearer '  + api_key,
                'Content-Type': 'audio/mpeg3',
                'Transfer-Encoding': 'chunked'
             }

    url = urllib.request.Request(api,data=data,headers=headers)
    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)
    print(decodedData['_text'])
    return (decodedData['_text'])

if __name__ == ('__main__'):
    with open('speech.mp3','rb') as f:
        data = f.read()
    recognize(data)