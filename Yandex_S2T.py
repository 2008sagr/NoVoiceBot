import urllib.request
import json
import IAM_KEY

def s2t(folder_id, iam_token):

    FOLDER_ID = folder_id #'b1g0g1nrj67c0se5efad'
    IAM_TOKEN = iam_token

    with open ('speech.ogg', 'rb') as f:
        data = f.read()

    params = "&".join([
        "topic=general",
        "folderId=%s" % FOLDER_ID,
        "lang=ru-RU"
    ])

    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
    url.add_header("Authorization", "Bearer %s" % IAM_TOKEN)

    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)

    if decodedData.get("error_code") is None:
        #print(decodedData.get("result"))
        return (decodedData.get('result'))
        




if __name__ == '__main__':
    print(s2t("b1g0g1nrj67c0se5efad", IAM_KEY.key))
