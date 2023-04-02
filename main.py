import datetime
import random
import threading
import time
from datetime import timedelta

import schedule
import telebot

import config
import schedule_text
from config import db_connection
from phrases import mountain_phrases, mine_phrases, get_text_with_link
from what_pair_progress import what_pair
from qt import get_quote, get_sticker_for_totem, get_totem_animal

message_count = 0
to_unpin_message_id = None

GROUP_ID = config.GROUP_ID
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['tleft'])
def time_left(message):
    today = (datetime.date.today()).strftime('%A')
    if today == "Saturday":
        bot.send_message(message.chat.id, "Сьогодні субота, чого ти мене питаєш за пари, йди роби лаби 👮‍♂️")
    elif today == "Sunday":
        bot.send_message(message.chat.id, "Сьогодні неділя, чого ти мене питаєш за пари, йди роби лаби 👮‍♂️")
    else:
        bot.send_message(message.chat.id,what_pair())


def check_week():
    my_date = datetime.date(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday)
    year, week_num, day_of_week = my_date.isocalendar()
    week_shedule = week_num - 9

    if week_shedule % 2 == 0:
        schedule.clear('unpair')
        schedule.every().monday.at("04:40").do(send_message_to_group,
            f"Нагадування⚠:\nЗараз парний тиждень ({week_shedule})").tag('pair')
        schedule.every().monday.at("04:50").do(send_message_to_group_and_pin, schedule_text.monday_08_00).tag(
            'pair')  # 2-14
        schedule.every().monday.at("10:20").do(send_message_to_group_and_pin, schedule_text.monday_13_30).tag(
            'pair')  # 2-14
        schedule.every().monday.at("12:10").do(unpin_message).tag('pair')  # 2-14, unpin
        schedule.every().wednesday.at("08:30").do(unpin_message).tag('pair')  # 2-14, unpin
        schedule.every().thursday.at("08:30").do(send_message_to_group_and_pin, schedule_text.thursday_11_40_2).tag(
            'pair')  # 2-14
        schedule.every().thursday.at("12:10").do(send_message_to_group_and_pin, schedule_text.thursday_15_20_2).tag(
            'pair')  # 2-14


    elif week_shedule % 2 != 0:
        schedule.clear('pair')
        schedule.every().monday.at("04:40").do(send_message_to_group,
            f"Нагадування⚠:\nЗараз НЕпарний тиждень ({week_shedule})").tag('unpair')
        schedule.every().monday.at("10:20").do(unpin_message).tag('unpair')  # 1-15, unpin
        schedule.every().wednesday.at("08:30").do(send_message_to_group_and_pin, schedule_text.wednesday_11_40).tag(
            'unpair')  # 1-15
        schedule.every().wednesday.at("10:20").do(send_message_to_group_and_pin, schedule_text.wednesday_13_30).tag(
            'unpair')  # 1-15
        schedule.every().wednesday.at("12:10").do(unpin_message).tag('unpair')  # 1-15, unpin
        schedule.every().thursday.at("08:30").do(send_message_to_group_and_pin, schedule_text.thursday_11_40_1).tag(
            'unpair')  # 1-15
        schedule.every().thursday.at("12:10").do(send_message_to_group_and_pin, schedule_text.thursday_15_20_1).tag(
            'unpair')



def send_message_to_group(message):
    bot.send_message(GROUP_ID, message, parse_mode="HTML", disable_web_page_preview=True)


def send_message_to_group_and_pin(message):
    unpin_message()
    last_message = bot.send_message(GROUP_ID, message)
    bot.pin_chat_message(GROUP_ID, last_message.message_id)
    global to_unpin_message_id
    to_unpin_message_id = last_message.message_id


def unpin_message():
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
schedule.every().tuesday.at("10:40").do(unpin_message)  # unpin

# Wednesday
schedule.every().wednesday.at("06:40").do(send_message_to_group_and_pin, schedule_text.wednesday_09_50)

# Thursday
schedule.every().thursday.at("04:50").do(send_message_to_group_and_pin, schedule_text.thursday_08_00)
schedule.every().thursday.at("06:40").do(send_message_to_group_and_pin, schedule_text.thursday_09_50)
schedule.every().thursday.at("14:00").do(unpin_message)  # unpin

# Friday
schedule.every().friday.at("04:50").do(send_message_to_group_and_pin, schedule_text.friday_08_00)
schedule.every().friday.at("06:40").do(send_message_to_group_and_pin, schedule_text.friday_09_50)
schedule.every().friday.at("08:30").do(unpin_message)  # unpin


########################################################################################
schedule.every().day.at("04:00").do(check_week)
check_week()


# =============================================================================================================


def db_connect():
    try:
        mydb = db_connection()
        mycursor = mydb.cursor(buffered=True)
        return [mydb, mycursor]
    except:
        send_message_to_group("Упс, щось пішло не так...\n"
                              "(З'єднання з БД)")


def check_timer(message, user_id, size, stop_timer, what_timer):
    try:
        now = datetime.datetime.now()
        if now < stop_timer:
            stop_timer_str = str(stop_timer + timedelta(hours=3))[:19]
            # stop_timer_str = stop_timer_str[:19]
            text = get_text_with_link(message) + \
                ", ти рано зайшов(-ла), зможеш спробувати знов після " + stop_timer_str
            return text
        elif now >= stop_timer:
            if what_timer == 0:
                new_try_qt(user_id)
                repeat_timer(user_id, what_timer)
            if what_timer == 1:
                new_try_bayraktar(user_id, size)
                repeat_timer(user_id, what_timer)
                return 10
            if what_timer == 2:
                new_try_mountain(user_id, size)
                repeat_timer(user_id, what_timer)
                return 20
    except:
        send_message_to_group("Упс, щось пішло не так...\n"
                              "(Перевірка таймеру)")


def new_try_mountain(user_id, passmountain):
    try:
        res = db_connect()
        cursor = res[1]
        db = res[0]

        new_passmountain = random.randint(0, 10)
        status = random.randint(0, 100)

        if 30 >= status >= 0:
            new_passmountain = passmountain + new_passmountain
        if 31 <= status <= 40:
            new_passmountain = passmountain
        if 41 <= status <= 99:
            # if passmountain < new_passmountain:
            #     new_passmountain = 0
            # if passmountain >= new_passmountain:
            new_passmountain = passmountain - new_passmountain
        if status == 100:
            new_passmountain = 0

        query = "UPDATE Users SET passmountain = %s WHERE user_id = %s"
        values = (str(new_passmountain), user_id)

        cursor.execute(query, values)
        db.commit()

        cursor.close()
        db.close()
    except:
        send_message_to_group("Упс, щось пішло не так...\n"
                              "(Нова спроба у скелелазах)")


def new_try_qt(user_id):
    try:
        res = db_connect()
        cursor = res[1]
        db = res[0]

        new_quote = get_quote()
        new_totem = get_totem_animal()

        query = "UPDATE Users SET totem = %s WHERE user_id = %s"
        values = (new_totem, user_id)

        cursor.execute(query, values)
        db.commit()

        if cursor.rowcount > 0:
            text = f"Твоя тотемна тварина на наступні 12 годин : {get_sticker_for_totem(new_totem)}\n" \
                   f"Твоя цитата дня : {new_quote}"
            send_message_to_group(text)
        else:
            pass
        cursor.close()
        db.close()
    except:
        send_message_to_group("Упс, щось пішло не так...\n"
                              "(Нова спроба у цитаті та тотемі)")


def new_try_bayraktar(user_id, size):
    try:
        res = db_connect()
        cursor = res[1]
        db = res[0]

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

        cursor.execute(query, values)
        db.commit()

        cursor.close()
        db.close()
    except:
        send_message_to_group("Упс, щось пішло не так...\n"
                              "(Нова спроба у байрактарах)")


def repeat_timer(user_id, what_timer):
    try:
        res = db_connect()
        cursor = res[1]
        db = res[0]

        now = datetime.datetime.now()
        date_time_stop_str = str(now + timedelta(hours=12))

        if what_timer == 0:
            query = "UPDATE Users SET stop_timer_qt = %s WHERE user_id = %s"
            values = (date_time_stop_str, user_id)
            cursor.execute(query, values)
            db.commit()

        elif what_timer == 1:
            query = "UPDATE Users SET stop_timer = %s WHERE user_id = %s"
            values = (date_time_stop_str, user_id)
            cursor.execute(query, values)
            db.commit()

        elif what_timer == 2:
            query = "UPDATE Users SET stop_timer_mountain = %s WHERE user_id = %s"
            values = (date_time_stop_str, user_id)
            cursor.execute(query, values)
            db.commit()

        cursor.close()
        db.close()
    except:
        send_message_to_group("Упс, щось пішло не так...\n"
                              "(Оновлення таймеру)")


def get_data_from_table(user_id):
    try:
        res = db_connect()
        cursor = res[1]

        query = "SELECT * FROM Users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        row = cursor.fetchone()

        if row:
            user_id, size, start_timer_qt, stop_timer, totem, passmountain, stop_timer_mountain = row
            data_arr = [user_id, size, start_timer_qt, stop_timer, totem, passmountain, stop_timer_mountain]
            return data_arr
        else:
            return 0
    except:
        send_message_to_group("Упс, щось пішло не так...\n"
                              "Отримання даних з таблиці")


def get_text_with_link_for_top5(user_id):
    try:
        chat_member = bot.get_chat_member(chat_id=GROUP_ID, user_id=user_id)
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
    if message.chat.id == GROUP_ID:
        try:
            res = db_connect()
            cursor = res[1]
            db = res[0]

            data_arr = get_data_from_table(message.from_user.id)
            if data_arr == 0:

                text = f'{get_text_with_link(message)}, я Папуга 2.0, дивлюсь ти вперше тут.\n' \
                       f'Тут ти можеш кожні 12 годин отримувати цитату дня и дізнаватись, ' \
                       f'яка твоя тотемна тварина на наступні 12 годин.'
                send_message_to_group(text)
                try:
                    new_totem = get_totem_animal()
                    new_quote = get_quote()
                    now = datetime.datetime.now()
                    date_time_stop_str = str(now + timedelta(hours=12))

                    text = f"{get_text_with_link(message)}, " \
                           f"твоя тотемна тварина на наступні 12 годин : {get_sticker_for_totem(new_totem)}\n" \
                           f"Твоя цитата дня : {new_quote}"
                    send_message_to_group(text)

                    sql = "INSERT INTO Users (user_id,stop_timer_qt,totem) VALUES (%s,%s,%s)"
                    val = (message.from_user.id, date_time_stop_str, new_totem)
                    cursor.execute(sql, val)
                    db.commit()
                    cursor.close()
                    db.close()
                except:
                    pass

            elif data_arr[4] == None:
                text = f'{get_text_with_link(message)}, я Папуга 2.0, дивлюсь ти вперше тут.\n' \
                       f'Тут ти можеш кожні 12 годин отримувати цитату дня и дізнаватись, ' \
                       f'яка твоя тотемна тварина на наступні 12 годин.'
                send_message_to_group(text)
                try:
                    new_totem = get_totem_animal()
                    new_quote = get_quote()
                    now = datetime.datetime.now()
                    date_time_stop_str = str(now + timedelta(hours=12))

                    text = f"{get_text_with_link(message)}, " \
                           f"твоя тотемна тварина на наступні 12 годин : {get_sticker_for_totem(new_totem)}\n" \
                           f"Твоя цитата дня : {new_quote}"
                    send_message_to_group(text)

                    query = "UPDATE Users SET stop_timer_qt= %s, totem = %s WHERE user_id = %s"
                    values = (date_time_stop_str, new_totem, message.from_user.id)
                    cursor.execute(query, values)
                    db.commit()
                    cursor.close()
                    db.close()
                except:
                    pass
            else:
                data_arr = get_data_from_table(message.from_user.id)
                size = data_arr[1]
                stop_timer_qt = data_arr[2]
                totem = data_arr[4]
                passmountain = data_arr[5]

                text_from_timer = check_timer(message, message.from_user.id, size, stop_timer_qt, 0)

                data_arr = get_data_from_table(message.from_user.id)
                size = data_arr[1]
                stop_timer_qt = data_arr[2]
                totem = data_arr[4]

                if text_from_timer is None:
                    pass
                    cursor.close()
                    db.close()

                else:

                    if passmountain >= 0:

                        text = 'ТВІЙ ПРОФІЛЬ\n' \
                               f'||\U000026F0СКЕЛЕЛАЗ||\n' \
                               f'ФІО : {get_text_with_link(message)}\n' \
                               f'Розмір причандала : {size} cм\n' \
                               f'Тотемна тварина : {get_sticker_for_totem(totem)}\n' \
                               f'Пройдено гори\U000026F0 : {passmountain} м\n' \
                               f'\nP.S. : {text_from_timer}'
                    elif passmountain < 0:
                        text = 'ТВІЙ ПРОФІЛЬ\n' \
                               '||\U000026CFШАХТАР||\n' \
                               f'ФІО : {get_text_with_link(message)}\n' \
                               f'Розмір причандала : {size} cм\n' \
                               f'Тотемна тварина : {get_sticker_for_totem(totem)}\n' \
                               f'Пройдено шахти\U000026CF : {abs(passmountain)} м\n' \
                               f'\nP.S. : {text_from_timer}'

                    send_message_to_group(text)
                    cursor.close()
                    db.close()
        except:
            send_message_to_group("Упс, щось пішло не так...")
    else:
        bot.send_message(message.chat.id, "Ця команда працює лише у груповому чаті.")


@bot.message_handler(commands=['upgrade'])
def upgrade(message):
    if message.chat.id == GROUP_ID:
        try:
            user_id = message.from_user.id
            res = db_connect()
            cursor = res[1]
            db = res[0]

            query = "SELECT * FROM Users WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            row = cursor.fetchone()
            if row:
                # Тут stop_timer_qt и stop_timer уже по типу данных - даты, а не строки
                user_id, size_last, start_timer_last, stop_timer_last, totem, passmountain, stop_timer_mountain = row

                if size_last == None:
                    now = datetime.datetime.now()

                    size = str(random.randint(1, 17))

                    date_time_stop = str(now + timedelta(hours=12))[:19]
                    # date_time_stop = date_time_stop[:19]

                    send_message_to_group(
                        "Привіт, " + get_text_with_link(message) +
                        ", я Папуга 2.0, ти тільки-но зайшов(-ла) у режим, "
                        "де справжні хлопці та дівчата міряються своєю зброєю."
                    )

                    send_message_to_group(get_text_with_link(message) + ", твій байрактар : " + size + " см")
                    try:
                        query = "UPDATE Users SET size = %s, stop_timer = %s WHERE user_id = %s"
                        values = (size, date_time_stop, user_id)
                        cursor.execute(query, values)

                        db.commit()
                    except:
                        pass
                else:
                    status = check_timer(message, user_id, size_last, stop_timer_last, 1)

                    data_arr = get_data_from_table(user_id)
                    size = data_arr[1]

                    if len(str(status)) > 15:
                        send_message_to_group(status)

                    if status == 10:
                        if size > size_last:
                            text = get_text_with_link(message) + \
                                   ', ти сьогодні добряче попрацював руками та отримав ' \
                                   'свої ' + str(size - size_last) + ' cм. ' \
                                                                     'Тепер твій байрактар ' + str(
                                size) + ' см. Продовжуй сумлінно працювати!'
                            send_message_to_group(text)
                        elif size < size_last:
                            text = get_text_with_link(message) + ', сьогодні папуга віддзьобала ' + str(
                                size_last - size) + ' cм твого ' \
                                                    'причандала. ' \
                                                    'Тепер твій байрактар ' + str(
                                size) + ' см. ЗСУ помстить найближчим часом!'
                            send_message_to_group(text)
                        elif size == size_last:
                            text = get_text_with_link(message) + ', твій байрактар мов камінь. Не зрушився ні на см і ' \
                                                              'складає ' + str(size) + ' см.'
                            send_message_to_group(text)

            else:
                now = datetime.datetime.now()
                size = str(random.randint(1, 17))
                date_time_stop = str(now + timedelta(hours=12))[:19]

                send_message_to_group("Привіт, " + get_text_with_link(message) +
                                      ", ти тільки-но зайшов(-ла) у режим, "
                                      "де справжні хлопці та дівцата міряються своєю зброєю."
                                      )

                send_message_to_group(get_text_with_link(message) + ", твій байрактар : " + size + " см")
                try:
                    sql = "INSERT INTO Users (user_id,size,stop_timer) VALUES (%s, %s,%s)"
                    val = (user_id, size, date_time_stop)
                    cursor.execute(sql, val)

                    db.commit()
                except:
                    pass

            db.commit()
            cursor.close()
            db.close()
        except:
            send_message_to_group("Упс, щось пішло не так...\n"
                                  "(upgrade)")
    else:
        bot.send_message(message.chat.id, "Ця команда працює лише у груповому чаті.")


@bot.message_handler(commands=['iwannadie'])
def iwannadie(message):
    if message.chat.id == GROUP_ID:
        try:
            user_id = message.from_user.id

            res = db_connect()
            cursor = res[1]
            db = res[0]

            query = "SELECT * FROM Users WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            row = cursor.fetchone()
            if row:
                # Тут stop_timer_qt и stop_timer уже по типу данных - даты, а не строки
                user_id, size_last, start_timer_qt, stop_timer_last, totem, passmountain_last, stop_timer_mountain_last = row

                if passmountain_last is None:
                    now = datetime.datetime.now()

                    passmountain = str(random.randint(1, 12))

                    date_time_stop = str(now + timedelta(hours=12))[:19]
                    # date_time_stop = date_time_stop[:19]

                    send_message_to_group(
                        "Привіт, " + get_text_with_link(message) +
                        ", я Папуга 3.0, ти тільки-но зайшов(-ла) у режим, "
                        "де справжні скелелази-самогубці намагаються подолати гору Еверест."
                    )

                    send_message_to_group(get_text_with_link(message) + " ти подолав гору на : " + passmountain + " м")
                    try:
                        query = "UPDATE Users SET passmountain = %s, stop_timer_mountain = %s WHERE user_id = %s"
                        values = (passmountain, date_time_stop, user_id)
                        cursor.execute(query, values)

                        db.commit()
                    except:
                        pass

                else:
                    status = check_timer(message, user_id, passmountain_last, stop_timer_mountain_last, 2)

                    data_arr = get_data_from_table(user_id)
                    passmountain = data_arr[5]
                    if len(str(status)) > 15:
                        send_message_to_group(status)

                    if status == 20:
                        if passmountain >= 0:
                            send_message_to_group(mountain_phrases(message, passmountain, passmountain_last))

                        elif passmountain < 0:
                            send_message_to_group(mine_phrases(message, passmountain, passmountain_last))

            else:
                now = datetime.datetime.now()
                passmountain = str(random.randint(1, 12))

                date_time_stop = str(now + timedelta(hours=12))[:19]
                # date_time_stop = date_time_stop[:19]

                send_message_to_group(
                    "Привіт, " + get_text_with_link(message) +
                    ", я Папуга 3.0, ти тільки-но зайшов(-ла) у режим, "
                    "де справжні скелелази-самогубці намагаються подолати гору Еверест."
                )
                send_message_to_group(get_text_with_link(message) + " ти подолав гору на : " + passmountain + " м")
                try:
                    sql = "INSERT INTO Users (user_id,passmountain,stop_timer_mountain) VALUES (%s, %s,%s)"
                    val = (user_id, passmountain, date_time_stop)
                    cursor.execute(sql, val)

                    db.commit()
                except:
                    pass

            db.commit()
            cursor.close()
            db.close()
        except:
            send_message_to_group("Упс, щось пішло не так...")
    else:
        bot.send_message(message.chat.id, "Ця команда працює лише у груповому чаті.")


@bot.message_handler(commands=['top'])
def top(message):
    if message.chat.id == GROUP_ID:
        try:
            res = db_connect()
            mycursor = res[1]
            mydb = res[0]

            mycursor.execute("SELECT user_id, size FROM Users ORDER BY size DESC LIMIT 5")
            mydb.commit()
            top_users = mycursor.fetchall()

            # Format top users as string
            top_users_str = "TОП 5 БАЙРАКТАРІВ ЧАТУ:\n\n"
            for i, user in enumerate(top_users):
                top_users_str += f"{i + 1}. {get_text_with_link_for_top5(user[0])} -> {user[1]} см\n"

            send_message_to_group(top_users_str)

            mycursor.close()
            mydb.close()
        except:
            send_message_to_group("Упс, щось пішло не так...")
    else:
        bot.send_message(message.chat.id, "Ця команда працює лише у груповому чаті.")


@bot.message_handler(commands=['topm'])
def top_mountain(message):
    if message.chat.id == GROUP_ID:
        try:
            # Retrieve top 5 users from MySQL database
            res = db_connect()
            mycursor = res[1]
            mydb = res[0]

            mycursor.execute(
                "SELECT user_id, passmountain FROM Users WHERE passmountain >= 0 ORDER BY passmountain DESC LIMIT 5")
            mydb.commit()
            top_users = mycursor.fetchall()

            # Format top users as string
            top_users_str = "TОП 5 \U000026F0СКЕЛЕЛАЗІВ ЧАТУ:\n\n"
            for i, user in enumerate(top_users):
                top_users_str += f"{i + 1}. {get_text_with_link_for_top5(user[0])} >> {user[1]} м ^\n"

            mycursor.execute("SELECT user_id, passmountain FROM Users WHERE passmountain < 0 ORDER BY passmountain LIMIT 5")
            mydb.commit()
            top_negative_users = mycursor.fetchall()

            # Format top negative users as string and append to top_users_str
            tmp_arr_str = []
            top_users_str += "\n\nТОП 5 \U000026CFШАХТАРІВ ЧАТУ :\n\n"
            for i, user in enumerate(top_negative_users):
                tmp_arr_str.append(f"{i + 1}. {get_text_with_link_for_top5(user[0])} >> {user[1]} м ^(-1)\n")
                # top_users_str += f"{i + 1}. {GetTextWithLinkForTop5(user[0])} >> {user[1]} м ^(-1)\n"
            for i in reversed(tmp_arr_str):
                top_users_str += i
            # Send top users to Telegram group
            send_message_to_group(top_users_str)

            mycursor.close()
            mydb.close()
        except :
            send_message_to_group("Упс, щось пішло не так...")
    else:
        bot.send_message(message.chat.id, "Ця команда працює лише у груповому чаті.")



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
