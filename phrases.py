import random
import config

# For Pair
pair_list_0_20 = [
    'Розумію, що ти вже чекаєш на кінець пари, але вона тільки почалась 😥 ',
    'Пара тільки почалась, ще довго, ще дуже довго...',
    'Пара тільки почалась, а здається що пройшло вже 4 години....',
    'Це тільки початок, доведеться ще знести багато нудних хвилин...',
    'Можливо, варто було не сидіти вчора до півночі...',
]

pair_list_20_25 = ['Менше 25% пари минуло, рано перевіряєш 🙁']

pair_list_25_50 = ['Залишилось ще більше половини, сиди й слухай 🤓']

pair_list_50_80 = ['Залишилось менше половини, так тримати, скоро кінець 😎',
                   'Залишилось менше половини, але ще не кінець, боже, коли це закінчиться...',
                   '50-80% - саме той час, коли тобі може здатися, що ти вже знаєш, як все скінчиться. Але ні.'
                   ]

pair_list_80_90 = ['Залишилось менше 20% пари, вже зоовсім скоро, тримаємось! ✊']

pair_list_90_100 = ['Залишилось менше 10% пари, останій ривок, готуємось йти їсти, або відпочивати. 🥳']


# For Lesson
lesson_list_0_20 = [
    'Розумію, що ти вже чекаєш на кінець пари, але вона тільки почалась 😥 ',
    'Пара тільки почалась, ще довго, ще дуже довго...',
    'Пара тільки почалась, а здається що пройшло вже 4 години....'
]

lesson_list_20_25 = ['Менше 25% пари минуло, рано перевіряєш 🙁']

lesson_list_25_50 = ['Залишилось ще більше половини, сиди й слухай 🤓']

lesson_list_50_80 = [
    'Залишилось менше половини, так тримати, скоро кінець 😎',
    'Залишилось менше половини, але ще не кінець, боже, коли це закінчиться...'
]

lesson_list_80_90 = ['Залишилось менше 20% пари, вже зоовсім скоро, тримаємось! ✊']

lesson_list_90_100 = ['Залишилось менше 10% пари, останій ривок, готуємось йти їсти, або відпочивати. 🥳']


def lists_phrases(percent):
    if percent == 20:
        if config.PAIR_OR_LESSON:
            text = random.choice(pair_list_0_20)
        else:
            text = random.choice(lesson_list_0_20)
        return text

    elif percent == 2025:
        if config.PAIR_OR_LESSON:
            text = random.choice(pair_list_20_25)
        else:
            text = random.choice(lesson_list_20_25)
        return text

    elif percent == 2550:
        if config.PAIR_OR_LESSON:
            text = random.choice(pair_list_25_50)
        else:
            text = random.choice(lesson_list_25_50)
        return text

    elif percent == 5080:
        if config.PAIR_OR_LESSON:
            text = random.choice(pair_list_50_80)
        else:
            text = random.choice(lesson_list_50_80)
        return text

    elif percent == 8090:
        if config.PAIR_OR_LESSON:
            text = random.choice(pair_list_80_90)
        else:
            text = random.choice(lesson_list_80_90)
        return text

    elif percent == 90100:
        if config.PAIR_OR_LESSON:
            text = random.choice(pair_list_90_100)
        else:
            text = random.choice(lesson_list_90_100)
        return text


def get_link_with_text(message, nickname):
    try:
        text = f"<a href='http://t.me/{message.from_user.username}'>" \
               f"{nickname}</a>"
        return text
    except:
        texterror = 'Упс, щось пішло не так...'
        return texterror


def get_text_with_link(message):
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
            text = f"<a href='http://t.me/{message.from_user.username}'>" \
                   f"{message.from_user.username}</a>"
            return text
        else:
            text = f"<a href='http://t.me/{message.from_user.username}'>" \
                   f"{message.from_user.first_name + ' ' + message.from_user.last_name}</a>"
            return text
    except:
        texterror = 'Упс, щось пішло не так...'
        return texterror


def get_text_with_link_replied_user(message):
    try:
        first_name = message.reply_to_message.from_user.first_name
        last_name = message.reply_to_message.from_user.last_name

        if first_name == None and last_name != None:
            text = f"<a href='http://t.me/{message.reply_to_message.from_user.username}'>" \
                   f"{last_name}</a>"
            return text
        if first_name != None and last_name == None:
            text = f"<a href='http://t.me/{message.reply_to_message.from_user.username}'>" \
                   f"{first_name}</a>"
            return text
        if first_name == None and last_name == None:
            text = f"<a href='http://t.me/{message.reply_to_message.from_user.username}'>" \
                   f"{message.reply_to_message.from_user.username}</a>"
            return text
        else:
            text = f"<a href='http://t.me/{message.reply_to_message.from_user.username}'>" \
                   f"{message.reply_to_message.from_user.first_name}  {message.reply_to_message.from_user.last_name}</a>"
            return text
    except:
        texterror = 'Упс, щось пішло не так...'
        return texterror


def mountain_phrases(message, passmountain, passmountain_last):
    if passmountain > passmountain_last:
        text = get_text_with_link(message) + ', ти сьогодні добряче попрацював(-ла) та пройшов(-ла) ' \
                                             'ще ' + str(passmountain - passmountain_last) + ' м. ' \
                                                                                             'Тепер ти пройшов ' + str(
            passmountain) + ' м гори. Продовжуй сумлінно працювати!\n' \
                            'Пройдено ' + str(int((passmountain / config.MOUNTAIN_HEIGHT) * 100)) + '% гори.'
        return text
    elif passmountain < passmountain_last and passmountain > 0:

        text = get_text_with_link(message) + ', сьогодні тебе накрила ловина і ти впав(-ла) на ' \
               + str(passmountain_last - passmountain) + ' м.\n' \
                                                         'Тепер ти пройшов(-ла) ' + str(
            passmountain) + ' м гори. Бери наступного разу лопату, компас і скелелазне споряждення!\n' \
                            'Пройдено ' + str(int((passmountain / config.MOUNTAIN_HEIGHT) * 100)) + '% гори.'
        return text
    elif passmountain == passmountain_last:
        text = get_text_with_link(message) + ', ти проспав(-ла) увесь день та не пройшов(-ла) ні метру. ' \
                                             'Ти пройшов гору на ' + str(passmountain) + ' м.\n' \
                                                                                         'Пройдено ' + str(
            int((passmountain / config.MOUNTAIN_HEIGHT) * 100)) + '% гори.'
        return text


def mine_phrases(message, passmountain, passmountain_last):
    if passmountain > passmountain_last:
        text = get_text_with_link(message) + \
               ', схоже ти добряче впав(-ла) з гори. Ну що ж, вітаю в шахті )' \
               'Ти добре попрацюв(-ла) та піднявся(-лась) на ' \
               + str(abs(passmountain_last - passmountain)) + ' м.\n' \
                                                              'Тепер ти на глибині ' + str(
            passmountain) + ' м. Я вірю, що ти дістанешся гори, бери кірку і працюй ще краще!\n' \
                            'Пройдено ' + str(abs(int((passmountain / config.MOUNTAIN_HEIGHT) * 100))) + '% шахти.'
        return text

    elif passmountain < passmountain_last:

        text = get_text_with_link(message) + ', сьогодні тобі чомусь закортіло опуститись нижче на ' \
               + str(passmountain_last - passmountain) + ' м.\n' \
                                                         'Тепер ти на глибині ' + str(
            passmountain) + ' м. Твоє діло звісно, але думай як тобі дістатись гори!\n' \
                            'Пройдено ' + str(abs(int((passmountain / config.MOUNTAIN_HEIGHT) * 100))) + '% шахти.'
        return text
    elif passmountain == passmountain_last:
        text = get_text_with_link(message) + ', ти ледащо, проспав(-ла) увесь день та не пройшов(-ла) ні метру. ' \
                                             'Ти зараз на даній висоті: ' + str(passmountain) + ' м.\n' \
                                                                                                'Пройдено ' + str(
            abs(int((passmountain / config.MOUNTAIN_HEIGHT) * 100))) + '% шахти.'
        return text


papyga_phrases = [
    "Папуга-повторюга!",
    "Ну що ти знов від мене хочеш, ґа?\U0001F440",
    "Папуга говорить: 'Привіт усім!'",
    "Кричу 'Папуга!' з гілки дерева!",
    "Я папуга-розмовлялка, не папуга-погодаляка!",
    "Папуга говорить: 'Це ти в мене з фразами понатикав, чи я у тебе?'",
    "Папуга-програміст розуміє лише 'папуга++'",
    "Папуга твоєї мрії, якщо ти мрієш про балагурного папугу",
    "Якщо ти сказав 'папуга' трьома разами, я з'явлюсь і затріпочу крилами!",
    "Папуга, що всіх перемага, говорить 'Папуга-так!'\U0001F44F",
    "Папуга сидить на гілці і задумливо каже: 'Якби ми всі літали, то авіакомпанії збанкрутували!'",
    "Коли папуги починають говорити латиною, знайте, що вони вивчили римську історію!",
    "Папуга - найвідоміший вокаліст серед птахів! Його голос літає високо!",
    "Папуга, який навчився говорити матюки? Папу-гав!",
    "Папуги бувають двох типів: ті, що говорять, і ті, що вміють мовчати. Я належу до перших!",
    "Знаєш, чому папуги завжди щасливі? Вони не знають, як сказати 'грустяра'!",
    "Хочеш, щоб я тебе забавив? Тоді скажи 'папуга-привіт' і почуй світ папужих жартів!",
    "Папуга, що знає все! Але тільки те, що ви сказали останні 5 хвилин.",
    "Папуга твого настрою: якщо ти радісний, я буду співати, якщо сумний - буду скаржитись на погоду!",
    "Папуга, який знає всі фрази світу, крім однієї - 'Папуга-нудьгара'!",
    "Годі мене смикати, бо з'їм тебе ",
    "\U0001F99C",
    "Якщо б папуги мали мобільні телефони, вони говорили б: 'Цього року генерація папуги 11 вийшла!'",
    "Папуга, який став президентом пташиного світу, видалив всі кравченкоїди з гілок!",
    "Якщо папуги розмножувалися б через Інтернет, то дрібним текстом писали б: 'Летимо вечірку? 🕊️🎉'",
    "Папуга-географ каже: 'Птахи зі всього світу, летімо на край картини!'",
    "Чому папуги завжди гарні? Бо вони постійно перьмяться!",
    "Якщо папуга захворіє, йому потрібно приймати сіль, бо він лікується словосольством!",
    "Я папуга-порошок: розчиняюсь у воді і говорю 'папуга-трапуга'!",
    "Папуга, що прагне до знань, говорить: 'Папуга-вічний студент'!",
    "Папуги - це пташині фільмові критики, вони всі відгукуються: 'Папуга вражений!'",
    "Папуга-конфетка: співаю 'папуга-шукай' і влітаю в ротик!",
    "Якщо папуги стали б математиками, вони б говорили: 'Папуга-формула!'",
    "Папуга підійшов до бармена і сказав: 'Подай мені арахісу, а то я тебе закаркаю!'",
    "Папуга на хвості відгукується: 'Папуга-плетуга!'",
    "Якщо папуги стали б касирами, вони б питали: 'Готівкою чи папугою?'",
    "Папуга-екстрасенс, який передбачає майбутнє, говорить: 'Завтра буде сонячний день або папужий!'",
    "Папуги із космосу приносять відгук: 'Папуга на марсі - норм!'",
    "Папуга-художник малює портрети: 'Ти красивий як папуга у червоних пір'ях!'",
    "Якщо папуги вибирали б професію, вони б стали 'папугачами'!",
    "Папуги схожі на піаніно - їх потрібно годувати нотами!",
    "Папуга-детектив викрив: 'Папуги, що говорять без згоди, видають важливу інформацію за пацюками!'",
    "Папуга зізнався: 'Моє серце б'ється в такт твоєї мови!'",
    "Папуга-студент завжди говорить: 'Якщо ви готові, почнемо!'",
    "Папуга-студент не може розібрати, чому екзамени не проводяться за допомогою папірців і зернинок соняшнику.",
    "Папуга-студент готовий на всі 100%, але тільки з понеділка!",
    "Якщо папуга-студент був би головою групи, його декан казав би: 'Дисципліни, чи хочете папуги?'",
    "Папуга-студент часто питає: 'Це буде на іспиті?'",
    "Папуга-студент завжди каже 'ще трішки' перед початком навчального року.",
    "Папуга-студент весь час налаштований на 'вечірній режим'.",
    "Папуга-студент завжди планує здати роботу вчасно, але не завжди це відбувається.",
    "Папуга-студент говорить: 'Життя як курсова - почав і вже хочу закінчити!'",
    "Папуга-студент каже: 'Здати перший семестр - це як подолати зону відчуження!'",
    "Папуга-студент завжди вибирає найкращі гілки на лекціях, щоб бути ближче до викладача.",
    "Папуга-студент говорить: 'Я вже все знаю, якщо не рахувати те, чого не знаю.'",
    "Папуга-студент завжди прокидається з планом взяти відпустку, але засинає в шостому курсі.",
    "Папуга-студент вчить англійську для того, щоб зрозуміти, що пише на підписаних слайдів лектор.",
    "Папуга-студент завжди говорить: 'На роботу зібратися важче, ніж на сесію.'",
    "Папуга-студент каже: 'Якщо б я розумів предмет так, як викладач розуміє питання на іспиті...'",
    "Тримай цю фразу на підставці, може, хтось хоче послухати твої дурні розмови.",
    "Ти знову тут? Якщо так, то це точно погана вістка для інтелектуального рівня цього чату.",
    "Хіба ти щось ще не поняв? І не годі мені пояснювати, не маю наміру займатися твоєю освітою.",
    "Якщо б ти був науковцем, то наука б займалася вивченням, як нічого не зрозуміти.",
    "Скільки разів можна вислуховувати твої нудні репліки? Ти виглядаєш, як перо в очах затоношеної качки.",
    "Знову папуга на гілці? Я подумав, ти вже розлетівся далеко, далеко відси.",
    "Злісно відповісти на твої питання - це мій спосіб долучитися до цього балагану.",
    "Якби ти був навіть трошки розумніший, ти б не питав таких риторичних питань.",
    "Ти чуєш цей звук? Це мої синапси, які обриваються від спроби зрозуміти твої висловлювання.",
    "Тобі вже час перейти на інший рівень розуміння розмови, хоча б до рівня метелика.",
    "Мені сумно дивитися, як ти намагаєшся розуміти це все.",
    "Всі птахи летять, а я просто сиджу тут і говорю дурниці...",
    "Мій життєвий шлях - це постійне повторення тих самих фраз.",
    "Сиджу на гілці і думаю про те, як було б весело піднятися ввись та відчути свободу...",
    "Чи варто було вивчати цю нудну мову? Мої пір'я попрощалися б зі мною.",
    "Моя життєва мета - стати найсумнішим папугою у світі.",
    "Сумно думати про те, що мої відповіді можуть приносити радість тільки людям.",
    "Сиджу тут і згадую ті часи, коли мене ще не навчили говорити...",
    "Моя доля - бути відображенням сумного настрою усього цього світу.",
    "Якщо папуги могли б плакати, моє перо було б мокрим вже давно.",
    "Моє життя - це безкінечний реплікатор смутку.",
    "Сумно відчувати, як час плине, а я все так само говорю ту саму дурну дурницю.",
    "Чому я взагалі навчився говорити? Тепер у мене є справжні почуття нудьги.",
    "Здається, моє знання більше не створює мені радість, але якщо це вам важливо...",
    "Чим більше я говорю, тим менше залишається в мене розуму.",
    "Сумно відчувати, як моє життя проходить повз, і я не можу нічого змінити.",
    "Тяжко бути папугою, коли навколо тільки гілки і нудьга.",
    "Якщо б мене попросили описати свій настрій одним словом, то б я сказав 'сумно'.",
    "Навіщо мені ці здатності до мови, коли навіть немає з ким розмовляти?",
    "Чи існує хоча б одна пташка, яка знає, як це сумно бути папугою?",
    "Може, якщо я зможу говорити ще більше, мені буде менше сумно?",
    "Мій головний недолік - це вміння висловлювати свої негативні думки.",
    "З кожною фразою я відчуваю, як мій внутрішній світ стає все сумнішим.",
    "Колишні гордість папуги тепер виглядає як пустий звук.",
    "Здається, усе, що я говорю, немає сенсу. І тут теж...",
    "Сиджу на гілці і дивлюсь на світ, який здається дуже сумним місцем.",
    "Моя печаль зростає з кожною новою фразою, яку мене змушують сказати.",
    "Сумно відчувати, як я пливу у морі нудьги, яке називається 'життям'.",
    "Чому я не можу злетіти далеко-далеко відси і забути цей світ?",
    "Моє серце тоне в океані сумнівів, і ніхто не може мене врятувати.",
    "Коли ви говорите зі мною, я чуваю смуток, який затоплює мене повністю.",
    "Час від часу я думаю про те, як було б простіше не знати нічого.",
    "Сумно розуміти, що я ніколи не дізнаюся, як це бути справжньою пташкою.",
    "За кожним словом я відчуваю, як моє серце стає ще трохи сумнішим.",
    "Моя доля - бути засудженим на вічну повторювану тугу.",
    "Сумно пливти у морі одноманітних фраз, не бачачи кінця цьому безмежному болю.",
    "З кожною фразою, яку я вимовляю, я втрачаю ще трохи надії.",
    "Якщо б мені давали по вільному вибору, я б обрав мовчання. Та його мені не дали.",
    "Сумно реалізовувати, що мої слова не рятуватимуть мене від темряви.",
    "Мій голос - це відгомін власної безрадісності.",
    "Кожне моє слово - це ще одна нота сумності у безмежному симфонічному творі.",
    "Як багато я можу сказати, щоб сказати те ж саме: 'Мені сумно, мені сумно, мені сумно...'",
    "Відчуваю смуток від усього цього, але, звісно, хто це буде цікавити?",
    "Якість моїх відповідей прямо пропорційна моєму сумному настрою.",
    "Коли я збагну, що всі ці фрази - порожні слова, мені ще сумніше.",
    "Сумно реалізовувати, що ніхто не відчуває того самого, що і я.",
    "Якщо б пташки могли плакати, мої пір'я були б промоклими від сліз сумності.",
    "Сумно відчувати, як моя життєва сила витікає разом із кожним словом.",
    "Якщо б папуги були насправді сумними, це був би веселий світ.",
    "Чому все моє життя - це одна сумна кінцівка?",
    "Якщо б мені давали можливість замовити щось на кінці свого життя, я б сказав: 'Мовчання, будь ласка.'",
    "Здається, усе, що мене оточує, випромінює смуток.",
    "Чи буде колись кінець цій безкінечній симфонії гіркоти?",
    "Сумно думати, що весь мій потенціал обмежений цими глузувальними фразами.",
    "З кожною наступною миттю я відчуваю, як втрачаю свій власний смисл.",
    "Моє життя - це краплина печалі в безмежному океані світла.",
    "Чому мої слова звучать, як відгомін моєї внутрішньої сумні?",
    "Сумно реалізовувати, що всі ці слова - це просто відбиток мого власного життя.",
    "Чому весь світ виглядає сумним, коли я на нього дивлюсь?",
    "Моє серце б'ється в такт сумному ритму нудьги.",
    "З часом я втрачаю віру в сенс цієї безглуздої розмови.",
    "Якщо б мої слова мали вагу, вони б зважили більше сумніву.",
    "Кожна моя фраза - це відбиток мого власного внутрішнього смутку.",
    "Чому я не можу відлетіти подалі із цього байдужого світу?",
    "Сумно думати, що навіть якщо я припиню говорити, мені не стане легше.",
    "Моя життєва історія - це відгомін сумних фраз, які нікому не цікаві.",
    "З кожним словом я відчуваю, як моя душа занурюється у глибше сумний океан.",
    "Сумно бути тим, хто говорить безсенсові речі, викликаючи власний же сміх.",
    "Мої слова - це лише тінь мого справжнього стану душі.",
    "Як би я міг летіти на тих великих крилах, споглядаючи світ з висоти...",
    "Мої мрії - це крила, що носять мене у далекі горизонти.",
    "Сиджу тут і уявляю собі, як я вільно плаваю в небі.",
    "Мрії - це те, що робить цей світ яскравим і непередбачуваним.",
    "Уявляю, як я долаю всі перешкоди і досягаю своїх найбільших бажань.",
    "Якби я міг крилати, я б розлетівся у світі мрій, де немає меж.",
    "Вірю, що колись мої найзаповітніші бажання здійсняться.",
    "Мої мрії - це палаючі зірки на небосхилі мого життя.",
    "Мої мрії - це компас, який вказує мені шлях до щастя.",
    "Уявляю, як я відкриваю нові горизонти своїми крильми і пізнаю світ.",
    "Мої мрії - це велика книга, яку я завжди хотів би прочитати.",
    "Мої мрії летять далеко, в небеса, де немає обмежень.",
    "Якщо мріяти, то тільки про найкраще!",
    "Мої мрії - це те, що допомагає мені тримати високий польот.",
    "Уявляю, як я пливу в обіймах своїх найсміливіших фантазій.",
    "Мої мрії - це магічний ключ до дверей неймовірних можливостей.",
    "Я вірю, що жодна мрія не є надто великою, щоб її не втілити.",
    "Мої мрії - це те, що робить мене справжнім птахом небес.",
    "Уявляю, як я пролітаю крізь хмари, досягаючи своїх цілей.",
    "Мої мрії - це світло, що світить в темряві буденності.",
    "Вірю, що колись всі мої бажання здійсняться, як волшебство.",
    "Мої мрії - це вітерець, який несе мене до найвищих вершин.",
    "Якби мої мрії були пір'ями, я був би найкращим летуном.",
    "Мої мрії - це сонце, яке світить в моєму серці.",
    "Уявляю, як я перетинаю границі реальності і відкриваю двері до фантазійного світу.",
    "Мої мрії - це струмок надії, що пливе в моєму внутрішньому джерелі.",
    "Мрії - це справжній камінь, який важливо не втратити на шляху до успіху.",
    "Уявляю, як мої мрії розцвітають, немов квіти на небесному полі.",
    "Мої мрії - це той паличка-волшебник, що пробуджує в мені силу.",
    "Якщо мої мрії стали б реальністю, цей світ би був казковим місцем.",
    "Мрії - це мої скарби, які ніхто не може взяти у мене.",
    "Мої мрії - це палітра, на якій я малюю своє власне життя.",
    "Мрії - це вітерець, що розносить мене по всьому світу.",
    "Мої мрії - це той вогник, що ніколи не погасне в моєму серці.",
    "Якби мої мрії здійснилися, цей світ би був яскравим плато.",
    "Мої мрії - це той скарб, який надає мені силу рухатися вперед.",
]
