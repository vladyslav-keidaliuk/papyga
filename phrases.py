import random

def ListsPhrases(percent):

    if percent == 20 :
        list_0_20 = ['Розумію, що ти вже чекаєш на кінець пари, але вона тільки почалась 😥 ',
                     'Пара тільки почалась, ще довго, ще дуже довго...',
                     'Пара тільки почалась, а здається що пройшло вже 4 години, краще би ти поступив у БУРСУ',
                     'Пара лише почалась, а ти вже хочеш померти, страждай далі']
        text = random.choice(list_0_20)
        return text

    elif percent == 2025 :
        list_20_25 = ['Менше 25% пари минуло, рано перевіряєш 🙁']
        text = random.choice(list_20_25)
        return text

    elif percent == 2550 :
        list_25_50 = ['Залишилось ще більше половини, сиди й слухай 🤓']
        text = random.choice(list_25_50)
        return text

    elif percent == 5080 :
        list_50_80 = ['Залишилось менше половини, так тримати, скоро кінець 😎',
                     'Залишилось менше половини, але ще не кінець, боже, коли це закінчиться...',
                      'Залишилось менше половини, але ти не доживеш до кінця...']
        text = random.choice(list_50_80)
        return text

    elif percent == 8090 :
        list_80_90 = ['Залишилось менше 20% пари, вже зоовсім скоро, тримаємось! ✊']
        text = random.choice(list_80_90)
        return text

    elif percent == 90100 :
        list_90_100 = ['Залишилось менше 10% пари, останій ривок, готуємось йти їсти, або відпочивати. 🥳']
        text = random.choice(list_90_100)
        return text

def GetTextWithLink(message):
    try:
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name

        if first_name == None and last_name != None:
            text = f"<a href='http://t.me/{message.from_user.username}'>" \
                   f"{last_name}</a>"
            return text
        if first_name != None and last_name == None:
            text = f"<a href='http://t.me/{message.from_user.username}'>" \
                   f"{first_name}</a>"
            return text
        if first_name == None and last_name == None:
            text =  f"<a href='http://t.me/{message.from_user.username}'>" \
               f"{message.from_user.username}</a>"
            return text
        else:
            text = f"<a href='http://t.me/{message.from_user.username}'>" \
                   f"{message.from_user.first_name + ' ' + message.from_user.last_name}</a>"
            return text
    except:
        texterror = 'Упс, щось пішло не так...'
        return texterror

def MountainPhrases(message,passmountain,passmountain_last):
    if passmountain > passmountain_last:
        text = GetTextWithLink(message) + ', ти сьогодні добряче попрацював(-ла) та пройшов(-ла) ' \
                                          'ще ' + str(passmountain - passmountain_last) + ' м. ' \
                                                                                          'Тепер ти пройшов ' + str(
            passmountain) + ' м гори. Продовжуй сумлінно працювати!\n' \
                            'Пройдено ' + str(int((passmountain / 300) * 100)) + '% гори.'
        return text
    elif passmountain < passmountain_last and passmountain > 0:

        text = GetTextWithLink(message) + ', сьогодні тебе накрила ловина і ти впав(-ла) на ' \
               + str(passmountain_last - passmountain) + ' м.\n' \
                                                         'Тепер ти пройшов(-ла) ' + str(
            passmountain) + ' м гори. Бери наступного разу лопату, компас і скелелазне споряждення!\n' \
                            'Пройдено ' + str(int((passmountain / 300) * 100)) + '% гори.'
        return text
    elif passmountain == passmountain_last:
        text = GetTextWithLink(message) + ', ти проспав(-ла) увесь день та не пройшов(-ла) ні метру. ' \
                                          'Ти пройшов гору на ' + str(passmountain) + ' м.\n' \
                                                                                      'Пройдено ' + str(
            int((passmountain / 300) * 100)) + '% гори.'
        return text



def MinePhrases(message,passmountain,passmountain_last):

    if passmountain > passmountain_last:
        text = GetTextWithLink(message) + \
               ', схоже ти добряче впав(-ла) з гори. Ну що ж, вітаю в шахті )' \
               'Ти добре попрацюв(-ла) та піднявся(-лась) на ' \
               + str(abs(passmountain_last - passmountain)) + ' м.\n' \
                                                              'Тепер ти на глибині ' + str(
            passmountain) + ' м. Я вірю, що ти дістанешся гори, бери кірку і працюй ще краще!\n' \
                            'Пройдено ' + str(abs(int((passmountain / 300) * 100))) + '% шахти.'
        return text

    elif passmountain < passmountain_last:

        text = GetTextWithLink(message) + ', сьогодні тобі чомусь закортіло опуститись нижче на ' \
               + str(passmountain_last - passmountain) + ' м.\n' \
                                                         'Тепер ти на глибині ' + str(
            passmountain) + ' м. Твоє діло звісно, але думай як тобі дістатись гори!\n' \
                            'Пройдено ' + str(abs(int((passmountain / 300) * 100))) + '% шахти.'
        return text
    elif passmountain == passmountain_last:
        text = GetTextWithLink(message) + ', ти ледащо, проспав(-ла) увесь день та не пройшов(-ла) ні метру. ' \
                                          'Ти зараз на даній висоті: ' + str(passmountain) + ' м.\n' \
                                                                                             'Пройдено ' + str(
            abs(int((passmountain / 300) * 100))) + '% шахти.'
        return text