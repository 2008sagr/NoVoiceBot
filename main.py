
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


def main():
    token = ('e454041c2d0bc35bd37e0e8437c83e42b25742216d9c57643e18c61974f29d725c3a7bd796b73f98acd56')
    randint = random.randint(100000000, 900000000)
    vk_session = vk_api.VkApi(token=token)
    vk_session._auth_token()
    botlongpool = VkBotLongPoll(vk_session ,group_id=188220345)
    vk = vk_session.get_api()
    for event in botlongpool.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.object)
            parsing_str = str(event.object.message)
            bot_keyword = parsing_str.lower().find('пиздюк')
            if bot_keyword>-1:
                vk.messages.send(chat_id=event.chat_id,message='Чего?',random_id=randint)
            voice_msg = parsing_str.find('audio_message')
            if voice_msg > -1:
                print('Голосовое сообщение')
                msg_id_index = parsing_str.find('conversation_message_id')
                msg_id_start = parsing_str.find(':' ,msg_id_index)
                msg_id_end = parsing_str.find(',' ,msg_id_start)
                msg_id = parsing_str[(msg_id_start +2):msg_id_end]
                print(msg_id)


                vk.messages.delete(message_ids=msg_id, delete_for_all=1)  # осталось понять почему это не работает


                vk.messages.send(chat_id=event.chat_id, message='Пошли вы на хуй с вашими голосовыми '
                                                                'сообщениями', random_id=randint)



if __name__ == '__main__':
    main()

