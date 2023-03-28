import datetime
import random
import threading
import time
from datetime import timedelta

import schedule
import telebot

import config
import schedule_text
from config import DB
from phrases import ListsPhrases, MountainPhrases, MinePhrases, GetTextWithLink
from qt import GetQuote, GetTotemAnimalWithSticker, GetTotemAnimal

message_count = 0

GROUP_ID = config.GROUP_ID
bot = telebot.TeleBot(config.TOKEN)

# Функція, що вираховує скільки % пройдено, та в залежності від % повертає рандомну фразу з відповідного списку
def WhatProgressInProcent(start_time, target_time, num_pair):
    start_datetime = datetime.datetime.combine(datetime.date.today(), start_time)
    target_datetime = datetime.datetime.combine(datetime.date.today(), target_time)

    if target_time < start_time:
        target_datetime += datetime.timedelta(days=1)

    time_diff = target_datetime - start_datetime
    total_seconds = time_diff.total_seconds()
    elapsed_seconds = (datetime.datetime.now() - start_datetime).total_seconds()
    percentage_elapsed = int(elapsed_seconds / total_seconds * 100)

    result = "Пройдено " + str(percentage_elapsed) + "% " + str(num_pair) + "-ї пари.\n"
    if percentage_elapsed < 20:
        result = result + ListsPhrases(20)
        return result
    elif percentage_elapsed < 25:
        result = result + ListsPhrases(2025)
        return result
    elif percentage_elapsed < 50:
        result = result + ListsPhrases(2550)
        return result
    elif percentage_elapsed < 80:
        result = result + ListsPhrases(5080)
        return result
    elif percentage_elapsed < 91:
        result = result + ListsPhrases(8090)
        return result
    elif percentage_elapsed < 100:
        result = result + ListsPhrases(90100)
        return result
    else:
        result = "XMMMM"
        return result


def WhatPair(message):
    pair_1_start = datetime.time(8 - 3, 0, 0)
    pair_1_end = datetime.time(9 - 3, 35, 0)

    pair_2_start = datetime.time(9 - 3, 50, 0)
    pair_2_end = datetime.time(11 - 3, 25, 0)

    pair_3_start = datetime.time(11 - 3, 40, 0)
    pair_3_end = datetime.time(13 - 3, 15, 0)

    pair_4_start = datetime.time(13 - 3, 30, 0)
    pair_4_end = datetime.time(15 - 3, 5, 0)

    pair_5_start = datetime.time(15 - 3, 20, 0)
    pair_5_end = datetime.time(16 - 3, 55, 0)

    now = datetime.datetime.now().time()

    if pair_1_start <= now <= pair_1_end:
        text = WhatProgressInProcent(pair_1_start, pair_1_end, 1)
        bot.send_message(message.chat.id, text)
    elif pair_2_start <= now <= pair_2_end:
        text = WhatProgressInProcent(pair_2_start, pair_2_end, 2)
        bot.send_message(message.chat.id, text)
    elif pair_3_start <= now <= pair_3_end:
        text = WhatProgressInProcent(pair_3_start, pair_3_end, 3)
        bot.send_message(message.chat.id, text)
    elif pair_4_start <= now <= pair_4_end:
        text = WhatProgressInProcent(pair_4_start, pair_4_end, 4)
        bot.send_message(message.chat.id, text)
    elif pair_5_start <= now <= pair_5_end:
        text = WhatProgressInProcent(pair_5_start, pair_5_end, 5)
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Зараз нема жодної пари, відпочиваємо 😴")


@bot.message_handler(commands=['tleft'])
def time_left(message):
    today = datetime.date.today()
    today = today.strftime('%A')
    if today == "Saturday":
        bot.send_message(message.chat.id, "Сьогодні субота, чого ти мене питаєш за пари, йди роби лаби 👮‍♂️")
    elif today == "Sunday":
        bot.send_message(message.chat.id, "Сьогодні неділя, чого ти мене питаєш за пари, йди роби лаби 👮‍♂️")
    else:
        WhatPair(message)


def CheckWeek():
    Time = time.localtime()
    my_date = datetime.date(Time.tm_year, Time.tm_mon, Time.tm_mday)

    year, week_num, day_of_week = my_date.isocalendar()
    week_shedule = week_num - 9

    if week_shedule % 2 == 0:
        # print("Парна неділя")
        schedule.clear('unpair')
        schedule.every().monday.at("04:50").do(send_message_to_group_and_pin, schedule_text.monday_08_00).tag(
            'pair')  # 2-14
        schedule.every().monday.at("10:20").do(send_message_to_group_and_pin, schedule_text.monday_13_30).tag(
            'pair')  # 2-14
        schedule.every().monday.at("12:10").do(UnpinMessage).tag('pair')  # 2-14, unpin
        schedule.every().wednesday.at("08:30").do(UnpinMessage).tag('pair')  # 2-14, unpin
        schedule.every().thursday.at("08:30").do(send_message_to_group_and_pin, schedule_text.thursday_11_40_2).tag(
            'pair')  # 2-14
        schedule.every().thursday.at("12:10").do(send_message_to_group_and_pin, schedule_text.thursday_15_20_2).tag(
            'pair')  # 2-14


    elif week_shedule % 2 != 0:
        schedule.clear('pair')
        schedule.every().monday.at("10:20").do(UnpinMessage).tag('unpair')  # 1-15, unpin
        schedule.every().wednesday.at("08:30").do(send_message_to_group_and_pin, schedule_text.wednesday_11_40).tag(
            'unpair')  # 1-15
        schedule.every().wednesday.at("10:20").do(send_message_to_group_and_pin, schedule_text.wednesday_13_30).tag(
            'unpair')  # 1-15
        schedule.every().wednesday.at("12:10").do(UnpinMessage).tag('unpair')  # 1-15, unpin
        schedule.every().thursday.at("08:30").do(send_message_to_group_and_pin, schedule_text.thursday_11_40_1).tag(
            'unpair')  # 1-15
        schedule.every().thursday.at("12:10").do(send_message_to_group_and_pin, schedule_text.thursday_15_20_1).tag(
            'unpair')


to_unpin_message_id = None


def send_message_to_group(message):
    bot.send_message(GROUP_ID, message, parse_mode="HTML", disable_web_page_preview=True)


def send_message_to_group_and_pin(message):
    UnpinMessage()
    sent_message = bot.send_message(GROUP_ID, message)
    bot.pin_chat_message(GROUP_ID, sent_message.message_id)
    global to_unpin_message_id
    to_unpin_message_id = sent_message.message_id


def UnpinMessage():
    if to_unpin_message_id is None:
        pass
    else:
        bot.unpin_chat_message(GROUP_ID, to_unpin_message_id)


# Define a function that schedules a message to be sent to the group
def schedule_message_to_group(message, send_time):
    schedule.every().day.at(send_time).do(send_message_to_group, message)


# день_недели____номер_пары____нечет_или_чет

# Monday
# mon_1_2 = schedule.every().monday.at("07:50").do(send_message_to_group_and_pin, monday_08_00)# 2-14
schedule.every().monday.at("06:40").do(send_message_to_group_and_pin, schedule_text.monday_09_50)
schedule.every().monday.at("08:30").do(send_message_to_group_and_pin, schedule_text.monday_11_40)
# mon_4_2 = schedule.every().monday.at("13:20").do(send_message_to_group_and_pin, monday_13_30)# 2-14

# Tuesday
schedule.every().tuesday.at("04:50").do(send_message_to_group_and_pin, schedule_text.tuesday_08_00)
# schedule.every().tuesday.at("07:40").do(send_message_to_group_and_pin, tuesday_09_50)# vubor, не буде пари
schedule.every().tuesday.at("08:30").do(send_message_to_group_and_pin, schedule_text.tuesday_11_40)
schedule.every().tuesday.at("10:20").do(send_message_to_group_and_pin, schedule_text.tuesday_13_30)
schedule.every().tuesday.at("10:10").do(UnpinMessage)  # unpin

# Wednesday
# schedule.every().wednesday.at("05:50").do(send_message_to_group, wednesday_08_00)# vubor, не буде пари
schedule.every().wednesday.at("06:40").do(send_message_to_group_and_pin, schedule_text.wednesday_09_50)
# wed_3_1 = schedule.every().wednesday.at("11:30").do(send_message_to_group_and_pin, wednesday_11_40) #1-15
# wed_4_1 =schedule.every().wednesday.at("13:20").do(send_message_to_group_and_pin, wednesday_13_30) #1-15

# Thursday
schedule.every().thursday.at("04:50").do(send_message_to_group_and_pin, schedule_text.thursday_08_00)
schedule.every().thursday.at("06:40").do(send_message_to_group_and_pin, schedule_text.thursday_09_50)
# thu_3_1 = schedule.every().thursday.at("11:30").do(send_message_to_group_and_pin, thursday_11_40_1)# 1-15
# thu_3_2 = schedule.every().thursday.at("11:30").do(send_message_to_group_and_pin, thursday_11_40_2)# 2-14
# schedule.every().thursday.at("11:20").do(send_message_to_group_and_pin, thursday_13_30)
schedule.every().thursday.at("14:00").do(UnpinMessage)  # unpin

# Friday
schedule.every().friday.at("04:50").do(send_message_to_group_and_pin, schedule_text.friday_08_00)
schedule.every().friday.at("06:40").do(send_message_to_group_and_pin, schedule_text.friday_09_50)
schedule.every().friday.at("08:30").do(UnpinMessage)  # unpin
# schedule.every().friday.at("09:30").do(send_message_to_group_and_pin, friday_11_40)
# schedule.every().friday.at("11:20").do(send_message_to_group_and_pin, friday_13_30)


########################################################################################
schedule.every().day.at("05:00").do(CheckWeek)
CheckWeek()


# =============================================================================================================


def DBConnect():
    try:
        mydb = DB()
        mycursor = mydb.cursor(buffered=True)
        return [mydb, mycursor]
    except:
        send_message_to_group("Упс, щось пішло не так...")


def CheckTimer(message, user_id, size, stop_timer, what_timer):
    try:
        now = datetime.datetime.now()
        if now < stop_timer:

            stop_timer_str = str(stop_timer + timedelta(hours=3))
            stop_timer_str = stop_timer_str[:19]
            text = GetTextWithLink(message) + ", ти рано зайшов, зможеш спробувати знов після " + stop_timer_str
            return text
        elif now >= stop_timer:
            if what_timer == 0:
                NewTryQT(user_id)
                RepeatTimer(user_id, what_timer)
            if what_timer == 1:
                NewTry(user_id, size)
                RepeatTimer(user_id, what_timer)
                return 10
            if what_timer == 2:
                NewTryMountain(user_id, size)
                RepeatTimer(user_id, what_timer)
                return 20

    except:
        send_message_to_group("Упс, щось пішло не так...")


def NewTryMountain(user_id, passmountain):
    try:
        res = DBConnect()
        mycursor = res[1]
        mydb = res[0]

        new_passmountain = random.randint(0, 10)
        status = random.randint(0, 100)

        if 30 >= status >= 0:
            # print("Status: 0 ≤ х ≤ 46:")
            new_passmountain = passmountain + new_passmountain
        if 31 <= status <= 40:
            # print("Status: 47 ≤ х ≤ 52 ")
            new_passmountain = passmountain
        if 41 <= status <= 99:
            # print("Status: 53 ≤ х ≤ 99 ")
            # if passmountain < new_passmountain:
            #     new_passmountain = 0
            # if passmountain >= new_passmountain:
            new_passmountain = passmountain - new_passmountain
        if status == 100:
            # print("Рівно 100:")
            new_passmountain = 0

        query = "UPDATE Users SET passmountain = %s WHERE user_id = %s"
        values = (str(new_passmountain), user_id)

        mycursor.execute(query, values)
        mydb.commit()

        # Print a message indicating that the row was updated
        if mycursor.rowcount > 0:
            pass
        else:
            pass

        mycursor.close()
        mydb.close()
    except:
        send_message_to_group("Упс, щось пішло не так...")


def NewTryQT(user_id):
    try:
        res = DBConnect()
        mycursor = res[1]
        mydb = res[0]

        new_quote = GetQuote()
        new_totem = GetTotemAnimal()

        query = "UPDATE Users SET totem = %s WHERE user_id = %s"
        values = (new_totem, user_id)

        mycursor.execute(query, values)
        mydb.commit()

        if mycursor.rowcount > 0:
            # print("Row updated")
            text = f"Твоя тотемна тварина на наступні 12 годин : {GetTotemAnimalWithSticker(new_totem)}\n" \
                   f"Твоя цитата дня : {new_quote}"
            send_message_to_group(text)
        else:
            pass
        mycursor.close()
        mydb.close()
    except:
        send_message_to_group("Упс, щось пішло не так...")


def NewTry(user_id, size):
    try:
        res = DBConnect()
        mycursor = res[1]
        mydb = res[0]

        new_size = random.randint(0, 17)
        status = random.randint(0, 100)

        if 60 >= status >= 0:
            new_size = size + new_size
        if 61 <= status <= 65:
            new_size = size
        if 66 <= status <= 99:
            if size < new_size:
                new_size = 0
            if size >= new_size:
                new_size = size - new_size
        if status == 100:
            new_size = size * 2

        query = "UPDATE Users SET size = %s WHERE user_id = %s"
        values = (str(new_size), user_id)

        mycursor.execute(query, values)
        mydb.commit()

        # Print a message indicating that the row was updated
        if mycursor.rowcount > 0:
            # print("Row updated")
            pass
        else:
            # print("Row not found")
            pass

        mycursor.close()
        mydb.close()
    except:
        send_message_to_group("Упс, щось пішло не так...")


def RepeatTimer(user_id, what_timer):
    try:
        res = DBConnect()
        mycursor = res[1]
        mydb = res[0]

        now = datetime.datetime.now()
        date_time_stop_str = str(now + timedelta(hours=12))

        if what_timer == 0:
            query = "UPDATE Users SET stop_timer_qt = %s WHERE user_id = %s"
            values = (date_time_stop_str, user_id)
            mycursor.execute(query, values)
            mydb.commit()

        if what_timer == 1:
            query = "UPDATE Users SET stop_timer = %s WHERE user_id = %s"
            values = (date_time_stop_str, user_id)
            mycursor.execute(query, values)
            mydb.commit()
        if what_timer == 2:
            query = "UPDATE Users SET stop_timer_mountain = %s WHERE user_id = %s"
            values = (date_time_stop_str, user_id)
            mycursor.execute(query, values)
            mydb.commit()

        mycursor.close()
        mydb.close()
    except:
        send_message_to_group("Упс, щось пішло не так...")


def GetDataFromTable(user_id):
    try:
        res = DBConnect()
        mycursor = res[1]
        mydb = res[0]

        query = "SELECT * FROM Users WHERE user_id = %s"
        mycursor.execute(query, (user_id,))
        row = mycursor.fetchone()

        if row:
            # Тут start_timer_qt и stop_timer уже по типу данных - даты, а не строки
            user_id, size, start_timer_qt, stop_timer, totem, passmountain, stop_timer_mountain = row
            data_arr = [user_id, size, start_timer_qt, stop_timer, totem, passmountain, stop_timer_mountain]
            return data_arr
        else:
            return 0
    except:
        send_message_to_group("Упс, щось пішло не так...")


def GetTextWithLinkForTop5(id):
    try:
        chat_member = bot.get_chat_member(chat_id=GROUP_ID, user_id=id)
        username = chat_member.user.username
        first_name = chat_member.user.first_name
        last_name = chat_member.user.last_name

        if first_name is None and last_name is not None:
            text = f"<a href='http://t.me/{username}'>" \
                   f"{last_name}</a>"
            return text
        if first_name is not None and last_name is None:
            text = f"<a href='http://t.me/{username}'>" \
                   f"{first_name}</a>"
            return text
        if first_name is None and last_name is None:
            text = f"<a href='http://t.me/{username}'>" \
                   f"{username}</a>"
            return text
        else:
            text = f"<a href='http://t.me/{username}'>" \
                   f"{first_name + ' ' + last_name}</a>"
            return text
    except:
        send_message_to_group("Упс, щось пішло не так...")


@bot.message_handler(commands=['whoi'])
def whoi(message):
    try:
        res = DBConnect()
        mycursor = res[1]
        mydb = res[0]

        data_arr = GetDataFromTable(message.from_user.id)
        if data_arr == 0:

            text = f'{GetTextWithLink(message)}, я Папуга 2.0, дивлюсь ти вперше тут.\n' \
                   f'Тут ти можеш кожні 12 годин отримувати цитату дня и дізнаватись, ' \
                   f'яка твоя тотемна тварина на наступні 12 годин.'
            send_message_to_group(text)
            try:
                new_totem = GetTotemAnimal()
                new_quote = GetQuote()
                now = datetime.datetime.now()
                date_time_stop_str = str(now + timedelta(hours=12))

                text = f"{GetTextWithLink(message)}, " \
                       f"твоя тотемна тварина на наступні 12 годин : {GetTotemAnimalWithSticker(new_totem)}\n" \
                       f"Твоя цитата дня : {new_quote}"
                send_message_to_group(text)

                sql = "INSERT INTO Users (user_id,stop_timer_qt,totem) VALUES (%s,%s,%s)"
                val = (message.from_user.id, date_time_stop_str, new_totem)
                mycursor.execute(sql, val)
                mydb.commit()
                mycursor.close()
                mydb.close()
            except:
                # print("Ты уже есть в базе")
                pass

            # NewTryQT(message.from_user.id)
        elif data_arr[4] == None:
            text = f'{GetTextWithLink(message)}, я Папуга 2.0, дивлюсь ти вперше тут.\n' \
                   f'Тут ти можеш кожні 12 годин отримувати цитату дня и дізнаватись, ' \
                   f'яка твоя тотемна тварина на наступні 12 годин.'
            send_message_to_group(text)
            try:
                new_totem = GetTotemAnimal()
                new_quote = GetQuote()
                now = datetime.datetime.now()
                date_time_stop_str = str(now + timedelta(hours=12))

                text = f"{GetTextWithLink(message)}, " \
                       f"твоя тотемна тварина на наступні 12 годин : {GetTotemAnimalWithSticker(new_totem)}\n" \
                       f"Твоя цитата дня : {new_quote}"
                send_message_to_group(text)

                query = "UPDATE Users SET stop_timer_qt= %s, totem = %s WHERE user_id = %s"
                values = (date_time_stop_str, new_totem, message.from_user.id)
                mycursor.execute(query, values)
                mydb.commit()
                mycursor.close()
                mydb.close()
            except:
                # print("Ты уже есть в базе")
                pass
        else:
            data_arr = GetDataFromTable(message.from_user.id)
            size = data_arr[1]
            stop_timer_qt = data_arr[2]
            totem = data_arr[4]
            passmountain = data_arr[5]

            text_from_timer = CheckTimer(message, message.from_user.id, size, stop_timer_qt, 0)

            data_arr = GetDataFromTable(message.from_user.id)
            size = data_arr[1]
            stop_timer_qt = data_arr[2]
            totem = data_arr[4]

            if text_from_timer is None:
                pass
                mycursor.close()
                mydb.close()

            else:

                if passmountain >= 0:

                    text = 'ТВІЙ ПРОФІЛЬ\n' \
                           f'||\U000026F0СКЕЛЕЛАЗ||\n' \
                           f'ФІО : {GetTextWithLink(message)}\n' \
                           f'Розмір причандала : {size} cм\n' \
                           f'Тотемна тварина : {GetTotemAnimalWithSticker(totem)}\n' \
                           f'Пройдено гори\U000026F0 : {passmountain} м\n' \
                           f'\nP.S. : {text_from_timer}'
                elif passmountain < 0:
                    text = 'ТВІЙ ПРОФІЛЬ\n' \
                           '||\U000026CFШАХТАР||\n' \
                           f'ФІО : {GetTextWithLink(message)}\n' \
                           f'Розмір причандала : {size} cм\n' \
                           f'Тотемна тварина : {GetTotemAnimalWithSticker(totem)}\n' \
                           f'Пройдено шахти\U000026CF : {abs(passmountain)} м\n' \
                           f'\nP.S. : {text_from_timer}'

                send_message_to_group(text)
                mycursor.close()
                mydb.close()
    except:
        send_message_to_group("Упс, щось пішло не так...")


@bot.message_handler(commands=['upgrade'])
def upgrade(message):
    try:
        user_id = message.from_user.id
        res = DBConnect()
        mycursor = res[1]
        mydb = res[0]

        query = "SELECT * FROM Users WHERE user_id = %s"
        mycursor.execute(query, (user_id,))
        row = mycursor.fetchone()
        if row:
            # Тут stop_timer_qt и stop_timer уже по типу данных - даты, а не строки
            user_id, size_last, start_timer_last, stop_timer_last, totem, passmountain, stop_timer_mountain = row

            if size_last == None:
                now = datetime.datetime.now()

                size = str(random.randint(1, 12))

                date_time_stop = str(now + timedelta(hours=12))
                date_time_stop = date_time_stop[:19]

                send_message_to_group(
                    "Привіт, " + GetTextWithLink(message) +
                    ", я Папуга 2.0, ти тільки-но зайшов(-ла) у режим, "
                    "де справжні хлопці та дівчата міряються своєю зброєю."
                )

                send_message_to_group(GetTextWithLink(message) + ", твій байрактар : " + size + " см")
                try:
                    query = "UPDATE Users SET size = %s, stop_timer = %s WHERE user_id = %s"
                    values = (size, date_time_stop, user_id)
                    mycursor.execute(query, values)

                    mydb.commit()
                except:
                    # print("Ты уже есть в базе")
                    pass
            else:
                status = CheckTimer(message, user_id, size_last, stop_timer_last, 1)

                data_arr = GetDataFromTable(user_id)
                size = data_arr[1]
                stop_timer_qt = data_arr[2]
                stop_timer = data_arr[3]
                totem = data_arr[4]

                if len(str(status)) > 15:
                    send_message_to_group(status)

                if status == 10:
                    if size > size_last:
                        text = GetTextWithLink(message) + \
                               ', ти сьогодні добряче попрацював руками та отримав ' \
                               'свої ' + str(size - size_last) + ' cм. ' \
                               'Тепер твій байрактар ' + str(
                            size) + ' см. Продовжуй сумлінно працювати!'
                        send_message_to_group(text)
                    elif size < size_last:
                        text = GetTextWithLink(message) + ', сьогодні папуга віддзьобала ' + str(
                            size_last - size) + ' cм твого ' \
                                                'причандала. ' \
                                                'Тепер твій байрактар ' + str(
                            size) + ' см. ЗСУ помстить найближчим часом!'
                        send_message_to_group(text)
                    elif size == size_last:
                        text = GetTextWithLink(message) + ', твій хєр мов камінь. Не зрушився ні на см і ' \
                                                          'складає ' + str(size) + ' см.'
                        send_message_to_group(text)

        else:
            now = datetime.datetime.now()
            size = str(random.randint(1, 12))

            date_time_stop = str(now + timedelta(hours=12))
            date_time_stop = date_time_stop[:19]

            send_message_to_group("Привіт, " + GetTextWithLink(message) +
                                  ", ти тільки-но зайшов(-ла) у режим, "
                                  "де справжні хлопці та дівцата міряються своєю зброєю."
                                  )

            send_message_to_group(GetTextWithLink(message) + ", твій байрактар : " + size + " см")
            try:
                sql = "INSERT INTO Users (user_id,size,stop_timer) VALUES (%s, %s,%s)"
                val = (user_id, size, date_time_stop)
                mycursor.execute(sql, val)

                mydb.commit()
            except:
                # print("Ты уже есть в базе")
                pass

        mydb.commit()
        mycursor.close()
        mydb.close()
    except Exception as e:
        # print(e)
        send_message_to_group("Упс, щось пішло не так...")


@bot.message_handler(commands=['iwannadie'])
def send_top_users(message):
    try:
        user_id = message.from_user.id
        # print(user_id)
        user_name_surname = str(message.from_user.first_name) + " " + str(message.from_user.last_name)

        res = DBConnect()
        mycursor = res[1]
        mydb = res[0]

        query = "SELECT * FROM Users WHERE user_id = %s"
        mycursor.execute(query, (user_id,))
        row = mycursor.fetchone()
        if row:
            # Тут stop_timer_qt и stop_timer уже по типу данных - даты, а не строки
            user_id, size_last, start_timer_qt, stop_timer_last, totem, passmountain_last, stop_timer_mountain_last = row

            if passmountain_last == None:
                now = datetime.datetime.now()

                passmountain = str(random.randint(1, 12))

                date_time_stop = str(now + timedelta(hours=12))
                date_time_stop = date_time_stop[:19]

                send_message_to_group(
                    "Привіт, " + GetTextWithLink(message) +
                    ", я Папуга 3.0, ти тільки-но зайшов(-ла) у режим, "
                    "де справжні скелелази-самогубці намагаються подолати гору Еверест."
                )

                send_message_to_group(GetTextWithLink(message) + " ти подолав гору на : " + passmountain + " м")
                try:
                    query = "UPDATE Users SET passmountain = %s, stop_timer_mountain = %s WHERE user_id = %s"
                    values = (passmountain, date_time_stop, user_id)
                    mycursor.execute(query, values)

                    mydb.commit()
                except:
                    # print("Ты уже есть в базе")
                    pass
            else:
                status = CheckTimer(message, user_id, passmountain_last, stop_timer_mountain_last, 2)

                data_arr = GetDataFromTable(user_id)
                passmountain = data_arr[5]
                if len(str(status)) > 15:
                    send_message_to_group(status)

                if status == 20:
                    if passmountain >= 0:
                        send_message_to_group(MountainPhrases(message, passmountain, passmountain_last))

                    elif passmountain < 0:
                        send_message_to_group(MinePhrases(message, passmountain, passmountain_last))

        else:
            now = datetime.datetime.now()
            passmountain = str(random.randint(1, 12))

            date_time_stop = str(now + timedelta(hours=12))
            date_time_stop = date_time_stop[:19]

            send_message_to_group(
                "Привіт, " + GetTextWithLink(message) +
                ", я Папуга 3.0, ти тільки-но зайшов(-ла) у режим, "
                "де справжні скелелази-самогубці намагаються подолати гору Еверест."
            )
            send_message_to_group(GetTextWithLink(message) + " ти подолав гору на : " + passmountain + " м")
            try:
                sql = "INSERT INTO Users (user_id,passmountain,stop_timer_mountain) VALUES (%s, %s,%s)"
                val = (user_id, passmountain, date_time_stop)
                mycursor.execute(sql, val)

                mydb.commit()
            except:
                # print("Ты уже есть в базе")
                pass

        mydb.commit()
        mycursor.close()
        mydb.close()
    except:
        send_message_to_group("Упс, щось пішло не так...")


@bot.message_handler(commands=['top'])
def send_top_users(message):
    try:
        res = DBConnect()
        mycursor = res[1]
        mydb = res[0]

        mycursor.execute("SELECT user_id, size FROM Users ORDER BY size DESC LIMIT 5")
        mydb.commit()
        top_users = mycursor.fetchall()

        # Format top users as string
        top_users_str = "TОП 5 БАЙРАКТАРІВ ЧАТУ:\n\n"
        for i, user in enumerate(top_users):
            top_users_str += f"{i + 1}. {GetTextWithLinkForTop5(user[0])} -> {user[1]} см\n"

        send_message_to_group(top_users_str)

        mycursor.close()
        mydb.close()
    except:
        send_message_to_group("Упс, щось пішло не так...")


@bot.message_handler(commands=['topm'])
def send_top_users(message):
    try:
        # Retrieve top 5 users from MySQL database
        res = DBConnect()
        mycursor = res[1]
        mydb = res[0]

        mycursor.execute(
            "SELECT user_id, passmountain FROM Users WHERE passmountain >= 0 ORDER BY passmountain DESC LIMIT 5")
        mydb.commit()
        top_users = mycursor.fetchall()

        # Format top users as string
        top_users_str = "TОП 5 \U000026F0СКЕЛЕЛАЗІВ ЧАТУ:\n\n"
        for i, user in enumerate(top_users):
            top_users_str += f"{i + 1}. {GetTextWithLinkForTop5(user[0])} >> {user[1]} м ^\n"

        mycursor.execute("SELECT user_id, passmountain FROM Users WHERE passmountain < 0 ORDER BY passmountain LIMIT 5")
        mydb.commit()
        top_negative_users = mycursor.fetchall()

        # Format top negative users as string and append to top_users_str
        top_users_str += "\n\nТОП 5 \U000026CFШАХТАРІВ ЧАТУ :\n\n"
        for i, user in enumerate(top_negative_users):
            top_users_str += f"{i + 1}. {GetTextWithLinkForTop5(user[0])} >> {user[1]} м ^(-1)\n"

        # Send top users to Telegram group
        send_message_to_group(top_users_str)

        mycursor.close()
        mydb.close()
    except Exception as e:
        # print(e)
        send_message_to_group("Упс, щось пішло не так...")


@bot.message_handler(content_types=['text', 'photo', 'video', 'document',
                                    'audio', 'voice', 'sticker', 'video_note', 'animation'])
def reaction_message(message):
    reactions = ['🤓', '🔥', '🤡', '💀']
    if message.chat.id == GROUP_ID:
        global message_count
        message_count += 1
        if message_count % 100 == 0:
            reaction = random.choice(reactions)
            bot.reply_to(message, reaction)


def start_polling():
    updates = bot.get_updates()
    last_update_id = updates[-1].update_id if updates else None
    bot.get_updates(offset=last_update_id)
    bot.polling(none_stop=True)
    time.sleep(60)


# Start the bot polling in a separate thread
polling_thread = threading.Thread(target=start_polling)
polling_thread.start()

# Main loop to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)
