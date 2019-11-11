
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import urllib.request
from Yandex_S2T import s2t
import iam_request
import threading
import time


def randint():
    randint = random.randint(100000000, 900000000)
    return (randint)


def iam_timer():
    global key
    key = iam_request.get_iam()
    print(time.ctime())
    threading.Timer(3600, iam_timer).start()

def parse_str(string,word):
    id_index = string.find(word)
    id_start = string.find(':', id_index)
    id_end = string.find(',', id_start)
    id = string[(id_start + 2):id_end]
    return (id)


def main():
    token = ('e454041c2d0bc35bd37e0e8437c83e42b25742216d9c57643e18c61974f29d725c3a7bd796b73f98acd56')
    vk_session = vk_api.VkApi(token=token)
    vk_session._auth_token()
    botlongpool = VkBotLongPoll(vk_session ,group_id=188220345)
    vk = vk_session.get_api()
    print('Бот запущен.')
    iam_timer()
    for event in botlongpool.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            parsing_str = str(event.object.message)
            msg_id_index = parsing_str.find('conversation_message_id')
            msg_id_start = parsing_str.find(':', msg_id_index)
            msg_id_end = parsing_str.find(',', msg_id_start)
            msg_id = parsing_str[(msg_id_start + 2):msg_id_end]

            usr_id_start = parsing_str.find("from_id': ")
            usr_id_end = parsing_str.find(',', usr_id_start)
            usr_id = parsing_str[(usr_id_start+10):usr_id_end]

            vk_user = vk.users.get(user_ids=usr_id, fields='', name_case='Nom')
            first_name_start = str(vk_user).find('first_name')
            first_name_end = str(vk_user).find(',', first_name_start)
            first_name = str(vk_user)[(first_name_start + 14):first_name_end - 1]

            last_name_start = str(vk_user).find('last_name')
            last_name_end = str(vk_user).find(',', last_name_start)
            last_name = str(vk_user)[(last_name_start + 13):(last_name_end - 1)]

            print(msg_id)

            kai_keyword = parsing_str.lower().find('кай ')
            if kai_keyword>-1:
                vk.messages.send(chat_id=event.chat_id,message='Пошел нахуй этот двоичный пидор!',random_id=randint())

            bot_pi_keyword = parsing_str.lower().find('бот пиздюк')
            if bot_pi_keyword>-1:
                vk.messages.send(chat_id=event.chat_id, message='Я не пиздюк!', random_id=randint())

            voice_msg = parsing_str.find('audio_message')
            fwd_msg = parsing_str.find("fwd_messages': []")
            if fwd_msg > -1:
                if voice_msg > -1:
                    print('Голосовое сообщение')
                    voice_index = parsing_str.find('link_ogg')
                    voice_start = parsing_str.find(':',voice_index)
                    voice_end = parsing_str.find(',', voice_start)
                    voice_url = parsing_str[(voice_start + 3):(voice_end - 1)]
                    #print(voice_url)
                    voice = urllib.request.urlopen (voice_url).read()
                    v2t = s2t('b1g0g1nrj67c0se5efad',key, voice)
                    try:
                        message = ('[' + first_name + ' ' + last_name + ']:\n' + v2t)
                        print(v2t)
                        vk.messages.send(chat_id=event.chat_id, message=message, random_id=randint())
                    except:
                        print('Ошибка отправки текста госового сообщения')


if __name__ == '__main__':
    main()

