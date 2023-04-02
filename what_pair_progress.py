import datetime
from phrases import lists_phrases


# Функція, що вираховує скільки % пройдено, та в залежності від % повертає рандомну фразу з відповідного списку
def what_progress_in_percent(start_time, target_time, num_pair):
    start_datetime = datetime.datetime.combine(datetime.date.today(), start_time)
    target_datetime = datetime.datetime.combine(datetime.date.today(), target_time)

    if target_time < start_time:
        target_datetime += datetime.timedelta(days=1)

    time_diff = target_datetime - start_datetime
    total_seconds = time_diff.total_seconds()
    elapsed_seconds = (datetime.datetime.now() - start_datetime).total_seconds()
    percentage_elapsed = int(elapsed_seconds / total_seconds * 100)

    result = "Пройдено " + str(percentage_elapsed) + "% " + str(num_pair) + "-ї пари.\n"
    if 0 <= percentage_elapsed < 20:
        result = result + lists_phrases(20)
        return result
    elif 20 <= percentage_elapsed < 25:
        result = result + lists_phrases(2025)
        return result
    elif 25 <= percentage_elapsed < 50:
        result = result + lists_phrases(2550)
        return result
    elif 50 <= percentage_elapsed < 80:
        result = result + lists_phrases(5080)
        return result
    elif 80 <= percentage_elapsed <= 90:
        result = result + lists_phrases(8090)
        return result
    elif percentage_elapsed < 100:
        result = result + lists_phrases(90100)
        return result


def what_pair():
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
        text = what_progress_in_percent(pair_1_start, pair_1_end, 1)
        return text
    elif pair_2_start <= now <= pair_2_end:
        text = what_progress_in_percent(pair_2_start, pair_2_end, 2)
        return text
    elif pair_3_start <= now <= pair_3_end:
        text = what_progress_in_percent(pair_3_start, pair_3_end, 3)
        return text
    elif pair_4_start <= now <= pair_4_end:
        text = what_progress_in_percent(pair_4_start, pair_4_end, 4)
        return text
    elif pair_5_start <= now <= pair_5_end:
        text = what_progress_in_percent(pair_5_start, pair_5_end, 5)
        return text
    else:
        text = "Зараз нема жодної пари, відпочиваємо 😴"
        return text
