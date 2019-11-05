import requests


def get_iam():
    url = 'https://iam.api.cloud.yandex.net/iam/v1/tokens'
    data = ({'yandexPassportOauthToken':'AgAAAAAQWYPqAATuwdP2CpbVsUPOu0sQ8Fht7sE'})
    res = requests.post(url, json=data)
    index = res.text.find('iamToken')
    start = res.text.find(':', index)
    end = res.text.find(',',start)

    iam_key = res.text[(start+2):(end)]
    f = open('IAM_KEY.py','w')
    f.write('key= ' + iam_key)
    f.close()
    print('Ключ обновлен')

if __name__ == ('__main__'):
    get_iam()

