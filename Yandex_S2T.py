import urllib.request
import json




def s2t(folder_id,key,data1):
    FOLDER_ID = folder_id #'b1g0g1nrj67c0se5efad'
    IAM_TOKEN = key
    #print(IAM_TOKEN)

    params = "&".join([
        "topic=general",
        "folderId=%s" % FOLDER_ID,
        "lang=ru-RU"
    ])

    try:
        url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data1)
        url.add_header("Authorization", "Bearer %s" % IAM_TOKEN)

        responseData = urllib.request.urlopen(url).read().decode('UTF-8')
        decodedData = json.loads(responseData)

        if decodedData.get("error_code") is None:
            #print(decodedData.get("result"))
            f = open('speech.ogg', 'wb')
            f.write(data1)
            f.close()
            return (decodedData.get('result'))


    except:
        print('Ошибка Yandex')

if __name__ == '__main__':
    print(s2t("b1g0g1nrj67c0se5efad", IAM_KEY.key))
