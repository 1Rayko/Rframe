
from colorama import init
from SimpleQIWI import *
import os
from time import sleep
os.system('clear')


#api.pay(account="ТЕЛЕФОН ПОЛУЧАТЕЛЯ", amount=1, comment='Привет мир!')

#print(api.balance)
print("""\033[33m  ______  ______ __       __ ______         ______   ______   ______  __       __ 
 /      \/      /  |  _  /  /      |       /      \ /      \ /      \/  \     /  |
/$$$$$$  $$$$$$/$$ | / \ $$ $$$$$$/       /$$$$$$  /$$$$$$  /$$$$$$  $$  \   /$$ |
$$ |  $$ | $$ | $$ |/$  \$$ | $$ |        $$ \__$$/$$ |  $$/$$ |__$$ $$$  \ /$$$ |
$$ |  $$ | $$ | $$ /$$$  $$ | $$ |        $$      \$$ |     $$    $$ $$$$  /$$$$ |
$$ |_ $$ | $$ | $$ $$/$$ $$ | $$ |         $$$$$$  $$ |   __$$$$$$$$ $$ $$ $$/$$ |
$$ / \$$ |_$$ |_$$$$/  $$$$ |_$$ |_       /  \__$$ $$ \__/  $$ |  $$ $$ |$$$/ $$ |
$$ $$ $$</ $$   $$$/    $$$ / $$   |      $$    $$/$$    $$/$$ |  $$ $$ | $/  $$ |
 $$$$$$  $$$$$$/$$/      $$/$$$$$$/        $$$$$$/  $$$$$$/ $$/   $$/$$/      $$/ 
     $$$/                                                                         
                                                                                  
                                                                                  \033[39m""")

print("\033[34mАвтор : sudoreboot2020\033[39m")


print("""\033[33m
[1] - Баланс
[2] - Вывести
[3] - Входящие платежи
[4] - Прием платежей
[5] - Эхо
[99] -Выход\033[39m""")
while True :
    n = str(input("\033[35m[*]\033[39"))

    if n == ('1'):

        tk = str(input("\033[35mВведи токен qiwi:\033[39m"))
        ph = str(input("\033[35mВведи Телефон :\033[39m"))
        token = tk         # https://qiwi.com/api
        phone = ph
        api = QApi(token=token, phone=phone)
        print(api.balance)
    elif n == ('2'):
        tk = str(input("\033[35mВведи токен qiwi:\033[39m"))
        ph = str(input("\033[35mВведи Телефон :\033[39m"))
        pi = str(input('\033[35m'+'Телефон получателя:'+'\033[39m'))
        com = str(input('\033[35m'+'Комментариый:'+'\033[39m'))
        m = float(input('\033[35m'+'Сколько вывести:'+'\033[39m'))
        api = QApi(token=tk, phone=ph)
        token = tk         # https://qiwi.com/api
        phone = ph

        print(api.balance)

        api.pay(account=pi, amount=m, comment=com)
    elif n ==  ("3"):
        tk = str(input("\033[35mВведи токен qiwi:\033[39m"))
        ph = str(input("\033[35mВведи Телефон :\033[39m"))
        token = tk      # https://qiwi.com/api
        phone = ph

        api = QApi(token=token, phone=phone)

        print(api.payments)
    elif n == ("4"):
        tk = str(input("\033[35mВведи токен qiwi:\033[39m"))
        ph = str(input("\033[35mВведи Телефон :\033[39m"))
        token = "ВАШ ТОКЕН"         # https://qiwi.com/api
        phone = "ВАШ ТЕЛЕФОН"

        api = QApi(token=token, phone=phone)

        price = 1                   # Минимальное значение при котором счет будет считаться закрытым
        comment = api.bill(price)   # Создаем счет. Комментарий с которым должен быть платеж генерируется автоматически, но его можно задать                                 # параметром comment. Валютой по умолчанию считаются рубли, но ее можно изменить параметром currency

        print("Переведите %i рублей на счет %s с комментарием '%s'" % (price, phone, comment))

        api.start()                 # Начинаем прием платежей

        while True:
            if api.check(comment):  # Проверяем статус
                print("Платёж получен!")
                break
    
            sleep(1)

        api.stop()                  # Останавливаем прием платежей
    
    elif n ==("5"):
        tk = str(input("\033[35mВведи токен qiwi:\033[39m"))
        ph = str(input("\033[35mВведи Телефон :\033[39m"))

        token = tk       # https://qiwi.com/api
        phone = ph

        api = QApi(token=token, phone=phone)

        price = 1
        comment = api.bill(price)

        print("Pay %i rub for %s with comment '%s'" % (price, phone, comment))


        @api.bind_echo()            # Создаем эхо-функцию.  Она будет вызываться при каждом новом полученном платеже. В качестве аргументов ей
                            # передаётся информация о платеже. 
        def foo(bar):
            print("New payment!")
            print(bar)             
            api.stop()

        api.start()
    elif n == ("99") :
        print('\033[33mДо новой встречи!\033[39m')
        break

# Используйте api.full_balance чтобы получить больше информации о кошельках. 