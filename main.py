
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import urllib.request
from Yandex_S2T import s2t
import iam_request
import threading
import time
import  ast
import Wit_ai

usr_dict = {1:1}


def randint():
    randint = random.randint(100000000, 900000000)
    return (randint)


def iam_timer():
    global key
    key = iam_request.get_iam2()
    print(time.ctime())
    threading.Timer(3600, iam_timer).start()
    global usr_dict
    usr_dict = {1: 1}


def main():
    token = ('e454041c2d0bc35bd37e0e8437c83e42b25742216d9c57643e18c61974f29d725c3a7bd796b73f98acd56')
    vk_session = vk_api.VkApi(token=token)
    vk_session._auth_token()
    botlongpool = VkBotLongPoll(vk_session ,group_id=188220345)
    vk = vk_session.get_api()
    print('Бот запущен.')
    iam_timer()
    global usr_dict
    kick_msg = False
    for event in botlongpool.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            parsing_str = str(event.object.message)
            parsed_str = ast.literal_eval(parsing_str)
            msg_id = parsed_str['conversation_message_id']
            usr_id = parsed_str['from_id']
            #print(parsing_str)
            if event.chat_id == 2:
                print('Тестовый чат')
            if event.chat_id == 3:
                print('Пошлый Чат')
            if event.chat_id == 4:
                print('Ламповый Чат')
            print( msg_id)

            bot_pi_keyword = parsing_str.lower().find('бот пиздюк')
            if bot_pi_keyword>-1:
                vk.messages.send(chat_id=event.chat_id, message='Я не пиздюк!', random_id=randint())

            voice_msg = parsing_str.find('audio_message')
            fwd_msg = parsing_str.find('reply_message')
            if fwd_msg < 0:
                if voice_msg > -1:
                    if event.chat_id <4:
                        d = usr_dict.get(usr_id)
                        if d is not None:
                            if int(d) > 4:
                                print('Превышен лимит')
                                kick_msg = True
                            else:
                               usr_dict[usr_id] = int(d) + 1
                        else:
                            usr_dict[usr_id] = 1
                            print('Первое предупреждение')

                    try:
                        vk_user = vk.users.get(user_ids=usr_id, fields='', name_case='Nom')
                        len_str = len(str(vk_user))
                        vk_user_str = (str(vk_user)[1:(len_str-1)])
                        vk_user_parsed = ast.literal_eval(vk_user_str)
                        first_name = vk_user_parsed['first_name']
                        last_name = vk_user_parsed['last_name']

                    except:
                        first_name = ''
                        last_name = ''
                        print('Не смог получить имя')
                    print('Голосовое сообщение')
                    voice_index = parsing_str.find('link_ogg')
                    voice_start = parsing_str.find(':',voice_index)
                    voice_end = parsing_str.find(',', voice_start)
                    voice_url = parsing_str[(voice_start + 3):(voice_end - 1)]
                    voice = urllib.request.urlopen (voice_url).read()
                    v2t = s2t('b1g0g1nrj67c0se5efad',key, voice)
                    try:
                        if first_name != '':
                            if kick_msg == True:
                                message = ('[' + first_name + ' ' + last_name + ']:\n' +
                                           'Напоминаю о лимите в 5 сообщений в час\n'
                                           'Скоро за превышение будет пред.\n' +
                                           'Текст сообщения:\n'+ v2t)
                                kick_msg = False
                            else:
                                message = ('[' + first_name + ' ' + last_name + ']:\n' + v2t)
                            print(message)
                        else:
                            message = v2t
                        vk.messages.send(chat_id=event.chat_id, message=message, random_id=randint())
                    except:
                        print('Ошибка отправки текста госового сообщения')


if __name__ == '__main__':
    main()

