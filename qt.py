import random


def GetTotemAnimal():
    animals = ['Ведмідь', 'Слон', 'Бобер',
               'Орел', 'Коник', 'Бик',
               'Жаба', 'Собака', "Хом'як",
               'Равлик', 'Лев',
               'Миша', 'Кіт', 'Черепаха',
               'Їжак', 'Мавпа', 'Коала',
               'Сова', 'Папуга', 'Кролик',
               'Лама']

    text = random.choice(animals)
    return text


def GetTotemAnimalWithSticker(animal):
    animals_dict = {
        'Ведмідь': '\U0001F43B',
        'Слон': '\U0001F418',
        'Бобер': '\U0001F9AB',
        'Орел': '\U0001F985',
        'Коник': '\U0001F40E',
        'Бик': '\U0001F402',
        'Жаба': '\U0001F438',
        'Собака': '\U0001F436',
        "Хом'як": '\U0001F439',
        'Равлик': '\U0001F40C',
        'Лев': '\U0001F981',
        'Миша': '\U0001F401',
        'Кіт': '\U0001F408',
        'Черепаха': '\U0001F422',
        'Їжак': '\U0001F994',
        'Мавпа': '\U0001F412',
        'Коала': '\U0001F428',
        'Сова': '\U0001F989',
        'Папуга': '\U0001F99C',
        'Кролик': '\U0001F407',
        'Лама': '\U0001F999'
    }

    unicode = animals_dict[animal]
    animal = animal + ' ' + unicode
    return animal


def GetQuote():
    for_students_quotes = [
        '“There are no shortcuts to any place worth going.” – Beverly Sills',
        '“Be a student as long as you still have something to learn, '
        'and this will mean all your life.” — Henry L. Doherty',
        '“All progress takes place outside the comfort zone.” – Michael John Bobak',
        '“The man who moves a mountain begins by carrying away small stones..” – Confucius',
        '“Nothing can dim the light which shines from within.” – Maya Angelou',
        '“Believe in yourself and all that you are. Know that there is something inside '
        'you that is greater than any obstacle.” – Christian D. Larson',
        '“Though no one can go back and make a brand-new start, anyone can start from now and '
        'make a brand-new ending.” – Carl Bard',
        '“You’ve got to get up every morning with determination if you’re going to go to bed with '
        'satisfaction.” – George Lorimer',
        '“Whatever you can do, or dream you can do, begin it. Boldness has genius, power, '
        'and magic in it. Begin it now.”— Goethe',
        '“If you don’t go after what you want, you’ll never have it. If you don’t ask, '
        'the answer is always no. If you don’t step forward, you’re always in the same place.” – Nora Roberts',
        '“So many of our dreams at first seem impossible, then they seem improbable, and '
        'then, when we summon the will, they soon become inevitable.” – Christopher Reeve',
        '“Shoot for the moon. Even if you miss, you’ll land among the stars.” – Les Brown',
        '“There are two kinds of people in this world: those who want to get '
        'things done and those who don’t want to make mistakes.” – John Maxwell',
        '“Develop success from failures. Discouragement and failure are two of the '
        'surest stepping stones to success.” – Dale Carnegie',
        '“Challenges are what make life interesting. '
        'Overcoming them is what makes life meaningful.” – Joshua J. Marine',
        '“By perseverance, the snail reached the ark.” – Charles Spurgeon',
        '“A winner is just a loser who tried one more time.” – George Augustus Moore',
        '“Persist and persevere, and you will find most things that are attainable, possible.” – Lord Chesterfield',
        '“Perseverance is not a long race; it is many short races one after another.” – Walter Elliott',
        '“Perseverance is a great element of success. If you only knock long enough and '
        'loud enough at the gate, you are sure to wake up somebody.” – Henry Wadsworth Longfellow',
        '“Success doesn’t come to you, you’ve got to go to it.” – Marva Collins',
        '“Successful and unsuccessful people do not vary greatly in their abilities. '
        'They vary in their desires to reach their potential.” – John Maxwell',
        '“Success means having the courage, the determination, and the will to become '
        'the person you believe you were meant to be.” – George Sheehan',
        '“The secret of your success is determined by your daily agenda.” – John C. Maxwell',
        '“Action is the foundational key to all success.” – Pablo Picasso',
        '“However difficult life may seem, there is always something '
        'you can do and succeed at.” – Stephen Hawking',
        "Only put off until tomorrow what you are willing to die having left undone.” – Pablo Picasso",
        "Do not wait to strike till the iron is hot; but make it hot by striking.” — William Butler Yeats",
        "Know the true value of time; snatch, seize, and enjoy every moment of it. No idleness, no laziness, "
        "no procrastination: never put off till tomorrow what you can do today.” – Philip Stanhope",
        "If you put off everything till you’re sure of it, you’ll never get anything done.” – Norman Vincent Peale",
        "You don’t have to see the whole staircase, just take the first step.” – Martin Luther King, Jr.",
        "Procrastination is the thief of time.” – Edward Young",
        "You may delay, but time will not.” – Benjamin Franklin",
        "I don’t wait for moods. You accomplish nothing if you do that. Your mind must know it has got to "
        "get down to work.” – Pearl S. Buck",
        "Do you know what happens when you give a procrastinator a good idea? Nothing!” – Donald Gardner",
        "Begin while others are procrastinating. Work while others are wishing.” – William Arthur Ward",
        "Procrastination usually results in sorrowful regret. Today’s duties put off until tomorrow give "
        "us a double burden to bear; the best way is to do them in their proper time.” – Ida Scott Taylor",
        "Procrastination makes easy things hard, hard things harder.” – Mason CooleyIf you’re enjoying "
        "these quotes, make sure to read our collection of procrastination quotes "
        "that will help you steal your time back.",
        "The only difference between success and failure is the ability to take action.” – Alexander Graham Bell",
        "Preparation is the key to success.” – Alexander Graham Bell",
        "Reading is to the mind, as exercise is to the body.” – Brian Tracy",
        "There are no traffic jams on the extra mile.” – Zig Ziglar",
        "Learning is like rowing upstream, not to advance is to drop back.” — Chinese Proverb",
        "It is wiser to find out than to suppose.” — Mark Twain",
        "Education is what survives when what has been learned has been forgotten.” — B. F. Skinner",
        "Acquiring knowledge is the most fruitful effort.” ― Eraldo Banovac",
        "What seems to us as bitter trials are often blessings in disguise.” – Oscar Wilde",
        "To acquire knowledge, one must study; but to acquire wisdom, one must observe.”―  Marilyn Vos Savant",
        "The purpose of learning is growth, and our minds, unlike our bodies, "
        "can continue growing as long as we live.” — Mortimer Adler",
        "What really matters is what you do with what you have.” – H. G. Wells",
        "Your life does not get better by chance, it gets better by change.” – Jim Rohn",
        "Nothing worthwhile comes easily. Work, continuous work and hard work, "
        "is the only way to accomplish results that last.” – Hamilton Holt",
        "Goals are not only absolutely necessary to motivate us. They are essential "
        "to really keep us alive.” – Robert H. Schuller",
        "One important key to success is self-confidence. An important key "
        "to self-confidence is preparation.” – Arthur Ashe",
        "Success consists of going from failure to "
        "failure without loss of enthusiasm.” – Winston Churchill",
        "No matter what happens, or how bad it seems today, life does go on, "
        "and it will be better tomorrow. - Maya Angelou",
        "It’s not what we do once in a while that shapes our lives. It’s what we do consistently. - Tony Robbins",
        "We would accomplish many more things if we did not think of them as impossible. - Vince Lombardi",
        "Education is the passport to the future, for tomorrow belongs "
        "to those who prepare for it today. - Malcolm X",
        "A little progress each day adds up to big results. - Satya Nani",
        "There are no secrets to success. It is dedication, hard work and learning from failure. - Collin Powell",
        "If you want to achieve excellence, you can get there today. "
        "As of this second, quit doing less-than-excellent work. - Thomas J. Watson",
        "To be successful you must accept all challenges that come your way. "
        "You can’t just accept the ones you like. - Mike Gafka",
        "Don’t let what you cannot do interfere with what you can do. - John Wooden",
        "Knowing is not enough; we must apply. Wishing is not enough; we must do. - Johann Wolfgang von Goethe",
        "Procrastination is the art of keeping up with yesterday. - Don Marquis",
        "Many of life’s failures are people who did not realize how close they were "
        "to success when they gave up. - Thomas A. Edison",
        "It’s not about perfect. It’s about effort. - Jillian Michaels",
        "Excellence is not a skill. It is an attitude. - Ralph Marston",
        "You don’t get what you wish for. You get what you work for. - Daniel Milstein",
        "Everything you’ve ever wanted is on the other side of fear. - George Addair",
        "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
        "You can’t use up creativity. The more you use, the more you have. - Maya Angelou",
        "‘The best way to gain self-confidence is to do what you are afraid to do.” – Swati Sharma",
        "If you hear a voice within you say ‘you cannot paint,’ then by all means paint, "
        "and that voice will be silenced. - Vincent Van Gogh",
        "Courage doesn’t always roar. Sometimes courage is the quiet voice at the e"
        "nd of the day saying ‘I will try again tomorrow’. - Mary Anne Radmacher",
        "Skill is only developed by hours and hours of work. - Usain Bolt",
        "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice "
        "and most of all, love of what you are doing or learning to do. - Pelé",
        "There are no secrets to success. It is the result of preparation, hard work, "
        "and learning from failure. - General Colin Powell",
        "People always say that I didn’t give up my seat because I was tired, but "
        "that isn’t true. I was not tired physically… No, the only tired I was, was tired of giving in. - Rosa Parks",
        "Striving for success without hard work is like trying to harvest where you haven’t planted. - David Bly",
        "Success is the sum of small efforts, repeated day in and day out. - Robert Collier",
        "Success isn’t overnight. It’s when every day you get a little better than "
        "the day before. It all adds up. - Dwayne Johnson",
        "Recipe for success: Study while others are sleeping; work while others are loafing; "
        "prepare while others are playing; and dream while others are wishing.” ― William A. Ward",
        "Success is the progressive realization of a worthy goal.” ― Earl Nightingale",
        "Power’s not given to you. You have to take it.” ― Beyoncé",
        "You may encounter many defeats but you must not be defeated. In fact, it may be necessary to "
        "encounter the defeats, so you can know who you are, what you can rise from, "
        "how you can still come out of it.” ― Maya Angelou",
        "All our dreams can come true if we have the courage to pursue them.” — Walt Disney",
        "To accomplish great things, we must not only act, but also dream, not only plan, "
        "but also believe.” — Anatole France",
        "Follow your passion. It will lead you to your purpose.” — Oprah",
        "Through hard work, perseverance and a faith in God, you can live your dreams.” — Ben Carson",
        "I find that the harder I work, the more luck I seem to have.” — Thomas Jefferson",
        "Self-belief and hard work will always earn you success.” — Virat Kohli",
        "An investment in knowledge pays the best interest.” — Benjamin Franklin",
        "Motivation is what gets you started. Habit is what keeps you going.” — Jim Ryun",
        "The most successful people are those who are good at plan B.” — James Yorke",
        "If you don’t build your dreams, someone will hire you to help build theirs.” — Tony Gaskin",
        "If you think education is expensive, try ignorance.” — Andy McIntyre",
        "The man who does not read books has no advantage over the one who cannot read them.” — Mark Twain",
        "The beautiful thing about learning is that no one can take it away from you.” — B.B. King",
        "Education is the most powerful weapon you can use to change the world.” — BB King",
        "The more that you read, the more things you will know, the more that you learn, "
        "the more places you’ll go.” — Dr. Seuss",
        "Education is something we have to keep pursuing day after day.” — Premier Brian Gallant",
        "Education is the most powerful weapon which you can use to change the world.” — Nelson Mandela",
        "The whole purpose of education is to turn mirrors into windows.” — Sydney J. Harris",
        "He who opens a school door closes a prison.” — Victor Hugo",
        "Learning is the only thing the mind never exhausts, never fears, and never regrets.” — Leonardo da Vinci",
        "Life is your teacher, and you are in a state of constant learning.” ― Bruce Lee",
        "Luck is a dividend of sweat. The more you sweat, the luckier you get.” ― Ray Kroc",
        "When life stresses you, step back and look for the positive, "
        "keep an optimistic attitude.” ― Catherine Pulsifer",
        "You cannot soar with the eagles as long as you hang out with the turkeys.” ― Joel Osteen",
        "The adventure of life is to learn. The purpose of life is to grow. The nature of life is to change. "
        "The challenge of life is to overcome. The essence of life is to care. The opportunity of "
        "life is to serve.” ― William Arthur Ward",
        "Enjoy all you have while pursuing all you want.” ― Jim Rohn",
        "Even if you are on the right track, you will get run over if you just sit there.” ― Will Rogers",
        "No one starts out on top. You have to work your way up.” ― Muhammad Ali",
        "Doing nothing is very hard to do…you never know when you’re finished.” ― Leslie Nielsen",
        "Choose your friends and mates, not by the money in their bank account, creed, ethnicity, or color;"
        " instead, choose character, actions, heart, and soul.” ― Ana Monnar",
        '"“The secret of success is to do the common things uncommonly well.” – John D. Rockefeller']

    programming_quotes = [
        'Programmer: A machine that turns coffee into code.',
        'Computers are fast; programmers keep it slow.',
        'When I wrote this code, only God and I understood what I did. Now only God knows.',
        'A son asked his father (a programmer) why the sun rises in the east, and sets in the west.'
        ' His response? It works, don’t touch!',
        'How many programmers does it take to change a light bulb? None, that’s a hardware problem.',
        'Programming is like sex: One mistake and you have to support it for the rest of your life.',
        'Programming can be fun, and so can cryptography; however, they should not be combined.',
        'Copy-and-Paste was programmed by programmers for programmers actually.',
        'Always code as if the person who ends up maintaining your code will be a '
        'violent psychopath who knows where you live.',
        'Debugging is twice as hard as writing the code in the first place. '
        'Therefore, if you write the code as cleverly as possible, you are, by definition, '
        'not smart enough to debug it.',
        'Algorithm: Word used by programmers when they don’t want to explain what they did.',
        'Software and cathedrals are much the same — first we build them, then we pray.',
        'There are two ways to write error-free programs; only the third works.',
        'If debugging is the process of removing bugs, then programming must be the process of putting them in.',
        '99 little bugs in the code. 99 little bugs in the code. '
        'Take one down, patch it around. 127 little bugs in the code …',
        'Remember that there is no code faster than no code.',
        'One man’s crappy software is another man’s full-time job.',
        'No code has zero defects.',
        'A good programmer is someone who always looks both ways before crossing a one-way street.',
        'Deleted code is debugged code.',
        'Don’t worry if it doesn’t work right. If everything did, you’d be out of a job.',
        'It’s not a bug — it’s an undocumented feature.',
        'It works on my machine.',
        'It compiles; ship it.',
        'Measuring programming progress by lines of code is like measuring aircraft building progress by weight.',
        'In a room full of top software designers, if two agree on the same thing, that’s a majority.',
        'One: Demonstrations always crash. And two: '
        'The probability of them crashing goes up exponentially with the number of people watching.',
        'A program is never less than 90% complete and never more than 95% complete.',
        'In a software project team of ten, there are probably three people '
        'who produce enough defects to make them net-negative producers.',
        'Most of you are familiar with the virtues of a programmer. '
        'There are three, of course: laziness, impatience, and hubris.',
        'I’ve finally learned what upward compatible means. It means we get to keep all our old mistakes.',
        'Walking on water and developing software from a specification are easy if both are frozen.',
        'Documentation is like sex: When it is bad, it is better than nothing. '
        'When it is good, it is really, really good.',
        'Software undergoes beta testing shortly before it’s released. Beta is Latin for still doesn’t work.',
        'There are only two kinds of programming languages out there. '
        'The ones people complain about and the ones no one uses.',
        'Programming made the impossible possible. You can have a null object and a constant variable.',
        'C makes it easy to shoot yourself in the foot; '
        'C++ makes it harder, but when you do, it blows your whole leg off.',
        'The evolution of languages: FORTRAN is a nontyped language. C is a weakly typed language. '
        'Ada is a strongly typed language. C++ is a strongly hyped language.',
        'C++: An octopus made by nailing extra legs onto a dog.',
        'When your hammer is C++, everything begins to look like a thumb.',
        'C programmers never die. They are just cast into void.',
        'Without C we only have Obol, Pasal, and BASI.',
        'One of the main causes of the fall of the Roman Empire was that lacking zero, '
        'they had no way to indicate successful termination of their C programs.',
        'In C we had to code our own bugs. In C++ we can inherit them.',
        'Q: How different are C and C++? A: 1. Because C — C++ = 1.',
        'What’s the object-oriented way to get wealthy? Inheritance.',
        'C++: Where your friends have access to your private members.',
        'Why do Java programmers have to wear glasses? Because they don’t C#.',
        'Q: What did the Java code say to the C code? A: You’ve got no class.',
        'If you put a million monkeys at a million keyboards, one of them will eventually write a Java program. '
        'The rest of them will write Perl programs.',
        'You’ll surely have fun when programming Kotlin, promised.',
        'If Java had true garbage collection, most programs would delete themselves upon execution.',
        'JavaScript logic: 0 == "0" and 0 == []; therefore, "0" != []',
        'Python: Executable pseudocode. Perl: Executable line noise.',
        'Should one learn Advanced BASIC programming language?',
        'Saying that Java is good because it works on all platforms '
        'is like saying anal sex is good because it works on all genders.',
        'Knock, knock … Who’s there? … *very long pause* … Java.',
        'God is real … unless declared integer.',
        'COBOL programmers understand why women hate periods.',
        'A SQL query goes into a bar, walks up to two tables, and asks, ‘Can I join you?',
        'To understand what recursion is, you must first understand recursion.',
        'The best thing about a boolean is even if you are wrong, you are only off by a bit.',
        'Two bytes meet. The first byte asks, ‘Are you ill?’ The second byte replies, ‘No, just feeling a bit off.',
        'There are 10 kinds of people in the world: Those who know binary and those who don’t',
        'William Shakespeare’s question 2B OR NOT 2B = FF.',
        'Q: If 1 is true and 0 is false? A: 1.',
        'Programmer’s partner: ‘Are you going to sit and type '
        'in front of that thing all day, or are you going out with me?’ Programmer: ‘Yes.',
        'There are only two hard things in computer science: cache invalidation and naming things.',
        'UNIX is simple. It just takes a genius to understand its simplicity.',
        'UNIX is user friendly. It’s just very particular about who its friends are.',
        'Linux is only free if your time has no value.',
        'A system administrator has two problems: 1. Dumb users. 2. Smart users.',
        'Potential partners are like internet domain names — the ones I like are already taken.',
        'Keyboard Failure. Press F1 to continue.',
        'If the box says, ‘This software requires Windows XP or better,’ does that mean it’ll run on Linux?',
        '.NET is called .NET so that it wouldn’t show up in a UNIX directory listing.',
        'ASCII stupid question, get a stupid ANSI.',
        'Hardware is made to last. Software is made to change. Change is the only thing that lasts. Software wins.',
        'There’s no place like 127.0.0.1.',
        'I have not failed. I’ve just found 10,000 ways that won’t work.',
        'I have always wished that my computer would be as easy to use as my telephone. '
        'My wish has come true. I no longer know how to use my telephone.',
        'When we had no computers, we had no programming problems either.',
        'There is an easy way and a hard way. The hard part is finding the easy way.',
        'Computers are good at following instructions but not at reading your mind.',
        'The best way to get accurate information on Usenet is to post something wrong and wait for corrections.',
        'The computer was born to solve problems that did not exist before.',
        'In theory, there ought to be no difference between theory and practice. In practice, there is.',
        'There is no Ctrl-Z in life.',
        'Whitespace is never white.',
        'When all else fails … reboot.']

    ukrainian_writers_quotes = [
        'Мужність не дається напрокат - Ліна Костенко',
        'Терпи, терпи — терпець тебе шліфує. - Василь Стус',
        'Лиш боротись — значить жить!',
        'Мова росте елементарно, разом з душею народу.',
        'Як ліки не завжди приємні, так і істина буває сувора',
        'Світ ловив мене, та не спіймав - Григорій Сковорода',
        'В обіймах з радістю журба. Одна летить, друга спиня… '
        'І йде між ними боротьба, і дужчий хто — не знаю я…',
        'Орлині крила маєм за плечима, самі ж кайданами прикуті до землі.',
        'Двоє дивляться вниз. Один бачить калюжу, другий — зорі. Що кому.',
        'Ліпше вмерти біжучи, ніж жити гниючи',
        'Тяжко, тяжко в світі жить І нікого не любить.',
        'Мрія дає нуль, якщо її не зробити життям.',
        'Людям не те що позакладало вуха – людям позакладало душі. - Ліна Костенко',
        'Коли пролітала комета Галлея – мені здалося, що вона озирнулася на нас, і зареготала. - Ліна Костенко',
        '…жінка — як музика, її можна любити, навіть не дуже розуміючи. - Ліна Костенко',
        'У кожної нації свої хвороби. У Росії — невиліковна. - Ліна Костенко',
        'У кожної влади в генах — знищити журналіста, придушити письменника,'
        ' перехапати всіх, хто бачить її наскрізь. - Ліна Костенко',
        'А ви думали, що Україна так просто. Україна — це супер.'
        ' Україна — це ексклюзив. По ній пройшли всі катки історії. '
        'На ній відпрацьовані всі види випробувань. Вона загартована найвищим гартом. '
        'В умовах сучасного світу їй немає ціни. - Ліна Костенко',
        'Люди не знають, кого вибирати, бо не можна ж вибрати когось з нікого. - Ліна Костенко',
        'Мабуть, у всіх родинах буває оце переродження в побут. Будні роблять людей буденними. - Ліна Костенко',
        'І жах не в тому, що щось зміниться, — жах у тому, що все може залишитися так само. - Ліна Костенко',
        'Ми унікальна нація. У нас хліборобів морили голодом. Режисери ставили спектаклі у концтаборах. '
        'Поетів закопували у вічну мерзлоту. У кого ще є атомний саркофаг? А у нас є. - Ліна Костенко',
        'А секунди летять. Отак можна вмерти й нічого не встигнути. Встигаєш тільки втомитися. - Ліна Костенко',
        'Кожен кат любить червоне вино, нагріте до 36 градусів. - Василь Стус',
        'Лиш мати вміє жити, аби світитися, немов зоря. - Василь Стус',
        'Народ ще тільки осмислює конституційні простори своєї свободи, а уряд уже стріляє. - Василь Стус',
        'Немає нічого страшнішого за необмежену владу в руках обмеженої людини. - Василь Симоненко',
        'Вірнішого і сердечнішого побратима, ніж папір, я не знаю. - Василь Симоненко',
        'Живе той, хто не живе для себе, хто для других виборює життя. - Василь Симоненко',
        'На світі той намудріший, хто найдужче любить життя. - Василь Симоненко',
        'На цвинтарі розстріляних ілюзій уже немає місця для могил. - Василь Симоненко',
        'Не все те отрута, що неприємне на смак. - Григорій Сковорода',
        'Скільки зла таїться всередині за гарною подобою: гадюка ховається в траві. - Григорій Сковорода',
        'З видимого пізнавай невидиме. - Григорій Сковорода',
        'Виховуючи свою дитину, ти виховуєш себе. - Василь Сухомлинський',
        'Закоханий у себе не може бути здатний на справжню любов. - Василь Сухомлинський',
        'Любов – це насамперед відповідальність, а потім уже насолода, радість. - Василь Сухомлинський',
        'Любов шляхетна тільки тоді, коли вона сором’язлива. - Василь Сухомлинський',
        'Людина лише тоді по-справжньому дорожить життям, '
        'коли в неї є щось несумірно дорожче за власне життя. - Василь Сухомлинський',
        'Перш ніж полюбити в дівчині жінку, полюби в ній людину. - Василь Сухомлинський',
        'Не завидуй багатому: багатий не знає ні приязні, ні любові… - Тарас Шевченко',
        'Як не мудруй, а правди ніде діти - Леонід Глібов',
        'Якщо ти за все життя не посадив жодного дерева – плати за чисте повітря - О. Довженко'
        ]

    ukrainian_quotes_1 = [
        'Іноді дуже хочеться відправитися туди, де ніхто не знає твоє ім’я.',
        'За одну ніч не можна змінити життя. '
        'Але за одну ніч можна змінити думки, які назавжди змінять твоє життя.',
        'Я не художник, але малюю свої мрії. Я не письменник, але пишу свою книгу життя.',
        'Іноді достатньо всього одного теплого слова від дорогого тобі людини, '
        'щоб потім весь день ходити з посмішкою на обличчі.',
        'Щастя — це коли очі блищать, але не від сліз, а від любові.',
        'Три речі ніколи не повертаються назад — Час, Слово, Можливість.'
        ' Тому Не втрачай часу, Вибирай слова, Не випускай можливість.',
        'Все завжди закінчується добре. Якщо все закінчилося погано, значить це ще не кінець.',
        'Завжди говори те, що відчуваєш, і роби те, що думаєш. Мовчання ламає долі.',
        'Я досі мрію залишитися непоміченим у супермаркеті і всю ніч жерти вкусняшки.',
        '7 чудес світу – 1 — бачити, 2 — чути, 3 — відчувати, 4 — говорити, 5 — думати, 6 — радіти, 7 – любити.',
        'Робота над собою змінює відносини, змінює долю, змінює життя.',
        'Ми любимо казки, але не віримо в них.',
        'Кожен може любити, коли все добре. Але лише одиниці, не дивлячись не на що.',
        'одії, які ми притягуємо в наше життя, якими б неприємними для нас вони не були,'
        ' необхідні для того, щоб ми навчилися того, чого повинні навчитися.',
        'Світ цікавий. Скажеш «спасибі» ти — скажуть «спасибі тобі. '
        'Посміхнешся ти — тобі посміхнуться. Усе хороше починається з тебе.',
        'Любов, яка пережила розставання, винагороджується вічністю.',
        'Між питанням і моєю відповіддю міг пройти рік.',
        'Оточуй себе тільки тими людьми, які будуть тягнути тебе вище. '
        'Життя вже і так сповнена тими, хто хоче тягнути тебе вниз.',
        'Як буває красиво, коли розпускається душа. Коли ти і світ стаєте одним цілим, і ти відчуваєш гармонію.',
        'Кішка ніколи не подружиться з тим, хто не здатний полюбити її. Кішки ніколи не помиляються в людях.',
        'Треба вміти йти вчасно. Щоб після твого відходу зітхнули не з полегшенням, а з жалем.',
        'Заздрість — це печаль про успіхи інших.',
        'Першим на примирення йде той, кому це потрібніше.',
        'Насправді, життя просте, але ми наполегливо її ускладнюємо.',
        'Може стала розумнішою, може стало цинічний, але на багатьох людей мені тепер байдуже…',
        'Болісно було дивитися йому в очі і бачити там вирок.',
        'Тримати себе в руках — доля чоловіків, А мені не варто так морочитися; '
        'Я — жінка! Є мільйон причин, Щоб бути завжди такою, як серцю хочеться!',
        'Я не думаю про минуле. Значення має лише вічне сьогодні.',
        'Закоханої шалено і пристрасно, ласкавою, боязкою і владної.',
        'Кожна дрібниця може послужити твоєму натхненню.',
        'Забудь про те, хто ти є зараз і стань тим, ким хочеш бути.',
        'Друзів ніколи не буває достатньо, але іноді їх буває по горло.',
        'Крізь сльози вміти сміятися і ніколи не здаватися!',
        'Гроші теж страждають, тому, що у них немає мене.',
        'Життя триває, з тобою чи без тебе.',
        'Людина живе, що б боротися, а не що б здаватися.',
        'Той, хто шукає свою дорогу, повинен розуміти, що на початку, завжди буде роздоріжжі…',
        'Чим холодніше і безпросвітніші темрява зовні, '
        'тим затишніше здається теплий м’який світло в квартирі. '
        'І якщо літо — це час тікати з дому назустріч нездійсненним мріям '
        'підліткової душі, то осінь — час повертатися.',
        'Коли я вам буду потрібний, шукайте мене там, де були ви, коли я у вас потребувала.',
        'Надто багато в світі людей, яким ніхто не допоміг пробудитися.',
        'Краще любити і бути одного разу розлюбленим, ніж ніколи не любити і не розлюбити.',
        'Знайти себе неможливо — себе можна тільки створити.',
        'Набагато легше пробачити людей за те, що вони не праві, ніж за правоту.',
        'За любов доводиться розплачуватися в розстрочку, та й то здебільшого,'
        ' коли любов вже, на жаль, закінчилася.',
        'А вона лише розсміється, кинувши хижий погляд у відповідь,'
        ' їй, як нікому відомо, в житті кішки правил немає.',
        'Серце дівчини ніколи не буває порожньо…Або закохана, або не може забути.',
        'Не бійтеся когось втратити. Люди, призначені долею, не губляться. '
        'Ті, які втрачаються, призначені для досвіду.',
        'Крикни — почує кожен, прошепчи — почує найближчий, і тільки люблячий почує про що ти мовчиш…',
        'Хто мало хоче, той дешево коштує.',
        'Я схожа на кактус. Квіти розкриваються дуже рідко і для обраних, а колючки видно всім.',
        'Ти уявити собі не можеш, на що здатна людина, який нарешті зрозумів, що у нього немає іншого виходу.',
        'Люди повинні знати: в театрі життя тільки Богу і ангелам дозволено бути глядачами.',
        'Більше всього мені хотілося б залізти тобі в голову і дізнатися, хто я для тебе насправді.',
        'Плювати я хотіла на чорні і білі смуги життя. Я іду по своїй. Фіолетовій!',
        'Мені з одного боку все одно, а з іншого боку все одно болить.',
        'Життя – занадто складна штука, щоб про неї міркувати на повному серйозі.',
        'Власне те, що твоє.',
        'Я не в активному пошуку — у мене все є. А чого немає — значить поки не треба.',
        'Гнів і лють закоханих — це відновлення любові.',
        'Я найщасливіша людина на світі. Ні, я не закохалася… я виспалася!',
        'Живи, як хочеш, роби, як знаєш, це твоє право, ти сам все вирішуєш.',
        'Ніхто не показує людям, хто він такий насправді.',
        'Я в захваті від факту власного існування!',
        'Цінуйте сьогодні! Тому що сьогодні, обміну та поверненню не підлягає!',
        'Сумнівайтеся в кого завгодно, тільки не в собі.',
        'Якщо є світло у вашому серці, ви знайдете свій шлях додому.',
        'Ми живемо лише для того, щоб пізнавати красу. Все інше – очікування. Халіль Джебран',
        'Посміхайся сьогодні, плач завтра. Читай це кожен день.',
        'Мудрий цінує всіх, тому у кожному помічає хороше.',
        'Буває день дорожче року. Буває, рік не варто дня.'
        ]

    ukrainian_quotes_2 =[
        'Я — людина, яка весь час у дорозі з нізвідки в бік щастя',
        'Ніхто не може бути в точності схожий на мене. Навіть мені це не завжди вдається.',
        'Є речі важливіші за гроші, але без грошей ці речі не купиш.',
        'Ми вмираємо кожну секунду, «я» секунду назад уже ніколи не повернеться.',
        'Чоловік зіпсував собі шлунок і скаржиться на обід. Те ж і з людьми, незадоволеними життям.',
        'Будь собою. Інші ролі вже зайняті.',
        'Єдине час, що є у вас зараз; єдине місце — тут.',
        'От би мені хто-небудь сказав, чого я хочу.',
        'Все, що приносить радість, має право на вхід у моє життя без черги!',
        'Цінуйте моменти до того, як вони стануть спогадами.',
        'Наше життя завжди являє собою результат переважаючих у нас думок.',
        'Хотів би я купити собі трошки щастя, якщо його де небудь продають.',
        'Той, хто хвалить тебе за те, чого у тебе немає, хоче отримати від тебе, що в тебе є.',
        'Кожна людина носить в глибині свого «я» маленьке кладовище, де поховані ті, кого він любив.',
        'У світі так багато прекрасного, що деколи думаю, що я не звідси.',
        'Жити весело — це справжнє мистецтво!',
        'Я можу встояти перед чим завгодно, крім спокуси.',
        'Я любив, і мене любили, але це ніколи не співпадало за часом.',
        'Як нерозумно, що з очей тече вода, коли серцю боляче.',
        'Немає шляху до свободи, бо свобода і є шлях.',
        'Може, я не помер сьогодні, щоб зрозуміти, навіщо я живий…',
        'Тільки коли ти когось любиш так сильно, ти можеш його ненавидіти з такою ж силою.',
        'Не кидайте фрази зопалу — є слова сильніше урагану. Заживають рани від ножа, а від слів не загоюються рани.',
        'Я боюся, що, коли мрія стане дійсністю, мені більше нема чого буде жити на світі.',
        'Прощати більш мужньо, ніж карати. Слабкий не може прощати. Прощення — властивість сильного.',
        'Мрію стати бумерангом. Тебе кидають, а ти їм — назад, в морду.',
        'Я не можу запам’ятати, що тебе забув.',
        'Доглянутий вигляд, грамотна мова і книги — ось, що завжди буде в моді.',
        'І зустрінеш ти, коли не чекаєш. І знайдеш не там, де шукаєш.',
        'Я не люблю битися, я люблю перемагати.',
        'Секрет успіху в житті – бути завжди в хорошому настрої, '
        'найголовніший крок до невдачі – бути заручником свого поганого настрою.',
        'Я не настільки тобі довіряю, щоб заподіяти біль.',
        'З собою завжди можна домовитися.',
        'Любов — це сміх і радість, а не докори, і не клітка, і не бажання володіти.',
        'Зроби крок, і дорога з’явиться сама собою.',
        'Твоє оголене тіло повинно належати тому, хто полюбить твою оголену душу.',
        'Істина — не те, що доказово, істина — це простота.',
        'Якщо у тебе є людина, якій можна розповісти сни, ти не маєш права вважати себе самотнім…',
        'Іноді потрібно обійти весь світ, щоб зрозуміти, що скарб заритий у твого власного будинку.',
        'Усмішка — єдиний тренд в моді, який актуальний завжди.',
        'Закохатися можна в красу, але полюбити лише тільки душу!',
        'У людини немає можливості всім робити добро, але у нього є можливість нікому не чинити зла.',
        'Якщо хворий дуже хоче жити, лікарі безсилі.',
        'Дружба, як діамант. Зустрічається рідко, коштує дорого, а підробок дуже багато…',
        'Жити треба так, щоб тебе пам’ятали і сволоти.',
        'Незалежно від того, що ви робите в житті, переконайтеся, що це те, що робить вас щасливими.',
        'Після фільмів про катастрофи всі чекають від природи дуже багато.',
        'Вранці, тільки одна гарна думка змінює сенс цілого дня.',
        'Коли тобі погано — прислухайся до природи. Тиша світу заспокоює краще, ніж мільйони непотрібних слів.',
        'Першим на примирення йде той, кому це потрібніше.',
        'Природа — це єдина книга з великим змістом на кожному аркуші.',
        'Одна справа — брехати, інше — помилятися в промовах і відступати від '
        'правди в словах в силу помилки, а не злого умислу.',
        'Коли людина самотня, він починає придивлятися до природи і любити її.',
        'іщо не відбувається в протиріччі з природою, тільки в протиріччі з тим, що ми знаємо.',
        'Усмішка — найкраще, що є в людині. Ти не зовсім людина, поки не вмієш посміхатися.',
        'Якщо ти здатен завжди посміхатися життю, життя завжди посміхнеться тобі.',
        'Справжній друг з тобою, коли ти не правий. Коли ти маєш рацію, кожен буде з тобою.',
        'Знайти кращого друга — найбільша удача в житті…',
        'Будь-яку депресію треба зустрічати з посмішкою. Депресія подумає, що ви ідіот і втече.',
        'Не суди про людину по її друзях. У Іуди вони були бездоганні.',
        'Про що ти мовчиш? Про щось важливе або про дрібниці?',
        'Життя – це стійке прагнення до чогось нового, кращого, прекрасного.',
        'Людина сама будує жорсткий паркан з «можна», '
        '«не можу», «не положено». А потім визирає і заздрить тим, хто живе на волі.',
        'Бувають люди Душею глибокі, як океан, — в яких хочеться зануритися. '
        'Та бувають люди, як калюжі, яких треба обходити, — щоб не забруднитися.',
        'Якщо ти щиро щасливий, без різниці, що люди думають',
        'Є порожнеча в серці, яку ви заповнили',
        'Життя не проблема, яку потрібно вирішувати, а реальність, бути досвідченим.',
        'З тобою я забуваю всі мої проблеми. З Тобою, Час, Завмирає.',
        'Я не знаю, що міцніше, наші джинси або наша дружба!',
        'Я не ідеальний, але я вірний.',
        'Хороші Часи + Божевільні Друзі = Хороші Спогади!'
        ]

    quotes = [programming_quotes,
              for_students_quotes,
              ukrainian_writers_quotes,
              ukrainian_quotes_1,
              ukrainian_quotes_2,
              ]
    quote = random.choice(quotes)

    text = '" ' + random.choice(quote) + ' "'
    return text





















