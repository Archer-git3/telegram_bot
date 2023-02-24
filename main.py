import telebot
from telebot import types
import random
from random import choice
from datetime import *
import celery

bot = telebot.TeleBot('6271434191:AAE0_SRVFyTKAbhw78JiBMMG9dB8TbkaL6Q')

compliments = ['Ти чарівна!',
    'Ти ніби зійшла зі сторінок гарної казки!',
    'Ти – мій ідеал!',
    'Ти красива, як богиня!',
    'Ти – витвір мистецтва!',
    'Ти легка, як весняний ранковий вітерець.',
    'З тобою добре і легко, ніби я сам наодинці з собою.',
    'Твої очі – два бездонних океану, в яких я готовий потонути прямо в цю хвилину!',
    'Ти розумна і красива, хіба так може бути це одночасно?',
    'Ти так доглянута і приваблива!',
    'В тобі стільки ніжності, це мене приваблює і робить тебе неймовірно жіночною!',
    'Ти – скарб, який мені пощастило знайти!',
    'Коли ти поруч, я забуваю про всі свої проблеми і причина тому ця неймовірна легкість!',
    'Ти справжня муза, яка дає сили і натхнення для шедеврів!',
    'Ні в якому разі нічого не міняй в собі, ти просто божественні!',
    'Про такої красуні, як ти, я навіть і не мріяв!',
    'Я справжній везунчик, адже мені пощастило зустріти саме тебе!',
    'У тебе сама приваблива і мила усмішка на світі!',
    'Ти так мене розумієш, ніби читаєш мої думки і це зводить мене з розуму!',
    'Твої риси списані з найкращих картин художників!',
    'Ти свіжа і гарна, як рожевий бутон!',
    'Жодна квітка в світі не зрівняється з твоєю красою.',
    'Ти – пісня!',
    'Коли ти дивишся на мене, я забуваю про все на світі!',
    'Не можу відвести очей від твоєї краси!',
    'Ти така уточенная, така витончена і красива, я не можу тобою не захоплюватися!',
    'Бути красивою – це злочин!',
    'Боюся, що тебе можуть просто вкрасти з-за твоєї краси!',
    'Не можу підібрати слів, що уособлюють твою красу, адже у словнику їх просто не вистачає!',
    'Від твоєї краси темніють очі!',
    'З роками твоя краса не меркне, а лише знаходить нові фарби!',
    'Твоя краса змушує мене відчувати на вершині світу!',
    'Твоя краса змушує відчувати мене пяним',
    'Твої очі – справжній магніт і я не можу не дивитися в них!',
    'Не переставай посміхатися, твоя усмішка чарівна!',
    'Ти справжній скарб!',
    'Ти навіть без будь-якої косметики виглядаєш чудово!',
    'Ти не злодійка? Адже абсолютно безсоромно ти вкрала всі мої думки та серце!',
    'Коли я дивлюся на тебе, я просто втрачаю реальність!',
    'У тебе космічна, неймовірна і просто казкова краса!',
    'Ти така красива, що я боюся розплакатися від щастя!',
    'Ти зірка, що впала з неба на землю!',
    'Як досконала і бездоганна твоя краса!',
    'Твоя краса, так само свіжа і необхідна мені, як ковток повітря!',
    'Часом мені здається, що кращого тебе немає нікого на білому світі!',
    'Спасибі, що дозволяєш бути поруч з тобою і насолоджуватися твоєю красою!',
    'Мені здається, що всі гарні вірші і пісні складені тільки про твою лише красі.',
    'Ніколи не сумнівайся у своїй привабливості, адже твоїй красі можна заздрити!',
    'Я впевнений, що сотні жінок не сплять ночами і тільки й мріють мати хоч тінь твоєї краси!',
    'Якби ти брала участь у конкурсах краси, вони б втратили свою значущість, адже перемога завжди була б твоєю!',
    'Твій голос-наче музика, а риси обличчя, як пейзажі красот природи!',
    'Твої риси виточені найдосвідченішими ювелірами на світі!',
    'Навіть найбільший і найглибший океан не зрівнятися з величиною твоєї краси!',
    'Як же мені пощастило, адже ти даруєш свою красу тільки мені.',
    'Від такої краси можуть незадоволений розбиватися дзеркала, гніваючись на твою бездоганність і ідеальність!',
    'Ти – справжня красуня і просто прелесть!',
    'Завжди будь впевнена в собі, адже такої краси я не зустрічав раніше!',
    'Немов діамант, твоя краса унікальна і дорога!',
    'Твоя шкіра така білосніжна, такі мякі губи, очі такі яскраві, що я не можу відвести від тебе очей!',
    'Якщо б я був поетом, я б склав цілу збірку віршів про твою красу!',
    'Ти – подарунок життя, дуже красивий і найкращий!',
    'У житті не бачив таких красивих довгих волосся чистою, сяючою шкіри і тонких рис обличчя!',
    'Не хочу навіть моргати, щоб не пропустити і секунди, спостерігаючи за твоїми гарними рисами!',
    'Можна зберігати твою фотографію на столику біля ліжка, щоб милуватися прекрасними рисами цілодобово?',
    'Як майстерно ти підбираєш гардероб, ти виглядаєш чудово!',
    'Ніжніше і красивіше пальців, ніж у тебе, я не бачив!',
    'Ні, я не знаю слів, що могли б описати твої прекрасні риси!',
    'Ти – втілення мрії!',
    'Твоя краса змушує сяяти сонце!',
    'Очі твої яскравіше всіх зірок на нічному небі!',
    'Ти володієш небесною красою і тонким розумом!',
    'Навіть сліпому не потрібні окуляри, щоб розгледіти твою красу!',
    'Немає тебе прекрасніше, ти як сонце ясна!',
    'Посміхайся частіше, адже небо хмуриться тільки від того, що не бачить твою посмішку!',
    'Найкрасивіша музика в світі складена тільки про тебе і твою красу.',
    'Дивлячись на тебе, по тілу біжать мурашки від твоєї краси!',
    'Твоя краса обеззброює!',
    'Де ж твій німб? Ти ангел, не інакше! Звичайні жінки не бувають такими красивими!',
    'Спасибі тобі за таку досконалу красу!',
    'Я хочу милуватися тобою 24 години в добу! Ти прекрасна!',
    'Мама казала мені, що в світі існують красиві жінки, але мовчала про те, що вони можуть бути прекрасними!',
    'Вас звуть не Афродіта?',
    'Мені соромно стояти поруч з тобою, адже я блекну в порівнянні з твоєю красою!',
    'Неймовірно! Твоя краса дарована Богом, ти знала про те, що ти його улюблениця?',
    'Все б віддав, щоб бути таким красивим, як ти, незважаючи на те, що я чоловік!',
    'Твоїх чорт мені не забути ніколи! Ти просто незабутня!',
    'Навіть ангели заздрісно дивляться на тебе з небес, милуючись неземною красою!',
    'Ти прекрасніше вогню, води, неба, природи!',
    'Е знаю, що саме мене так захоплює тебе, але я готовий пащу до твоїх ніг і стати вічним рабом твоєї краси.',
    'Будь ласка, скажи мені, що я зможу милуватися твоєю красою вічно!',
    'Ти так красива! З тебе тільки картини писати!',
    'Будь краса солодкою на смак, я б вже давно захворів на цукровий діабет поряд з тобою!',
    'Я неодмінно повинен подякувати твоїх батьків, за те, що вони справили на світло таку красу!',
    'Будь я журі на конкурсі краси, я б був необєктивний, адже інші жінки порівняно з тобою, просто потворні!',
    'Як витончений весь твій образ і як досконалі твої риси, немов ти божество, яке отримало фізичне тіло!',
    'Ти знаєш, чому я весь час посміхаюся? Я просто не можу приховати захоплення, дивлячись на тебе!',
    'Ні, тобі подібних точно немає в цьому світі. Ти найкраща і найкрасивіша. Однозначно!',
    'Безсумнівно, ти народилася тільки для того, щоб дарувати красу цього світу!',
    'В тобі немає вад і навіть те, що ти вважаєш недоліками – гідності в очах інших людей!',
    'Красивіше тебе може бути тільки твоя дочка!',
    'Неймовірно! Як ти живеш з такою красою? Ти, мабуть, найщасливіша жінка на світі!',
    'Навіть не уявляєш, яка гордість мене бере, коли інші чоловіки обертаються в твій слід!',
    'Не може бути! Невже всі досі приховували в секреті свої почуття і жодного разу не казали тобі, що ти найкрасивіша жінка на світі?!',
    'Сьогодні і завжди ти виглядаєш просто чудово!',
    'Я тобі навіть словами не можу передати, як вражений твоєю красою!',
    'Вибач за мовчання, просто я вражений твоєю красою!',
    'Ти просто неймовірна! Як тобі вдається так добре виглядати?!',
    'Я вражений і просто обеззброєний твоєю красою! Браво!',
    'Ось це так! Мені пощастило познайомитися з найкрасивішою жінкою на світі!'
            ]


@bot.message_handler(commands=['start'])  # стартовая команда
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇺🇦 Українська")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇺🇦 Обери мову / 🇬🇧 Choose your language", reply_markup=markup)

def start_2(message):
   # print(int(message.text))
    try:
        f=0
        for i in range(0,int(message.text)):
            bot.send_message(message.chat.id,f"{i+1}. I love you ❤")
    except:
        bot.send_message(message.chat.id, "тут потрібно було вести цифру спробуй заново")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '🇺🇦 Українська' or message.text=='🔙 Головне меню' :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👉👈 Хто найркащя людина у світі ")
        btn2 = types.KeyboardButton('📑 Пари')
        btn7 = types.KeyboardButton('⁉ Питання всього всесвіту життя та смерті')
        btn8 = types.KeyboardButton('🫠 Дивна та не зрозуміла річ')
        btn9 = types.KeyboardButton('👀 Крихітко моя ось маленький комплімент')
        btn10 = types.KeyboardButton('🔙 Повернутися до вибору мову')
        markup.add(btn1, btn2, btn7, btn8, btn9, btn10)
        bot.send_message(message.from_user.id, "👋 Привіт", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Вибери що тебе цікавить')

    elif message.text == '🔙 Повернутися до вибору мову':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇺🇦 Українська")
        btn2 = types.KeyboardButton('🇬🇧 English')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇺🇦 Українська / 🇬🇧 Choose your language", reply_markup=markup)

    elif message.text ==('🫠 Дивна та не зрозуміла річ'):
        msg = bot.send_message(message.chat.id, 'Напиши якусь цифру')
        bot.register_next_step_handler(msg, start_2)


    elif message.text == '👀 Крихітко моя ось маленький комплімент':
        for i in range(1):
            bot.send_message(message.from_user.id, random.choice(compliments))

    elif message.text == '⁉ Питання всього всесвіту життя та смерті':
        bot.send_message(message.from_user.id, "42")

    elif message.text == '👉👈 Хто найркащя людина у світі':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        x = datetime.now()
        bot.send_message(message.from_user.id, "ТИ🫵🥹")
        print(x.hour,x.minute)
        print(x.strftime("%A"))
        bot.send_message(message.from_user.id, x.strftime("%A"))
        btn1 = types.KeyboardButton('Ти впевнений?!')
        btn2 = types.KeyboardButton('Ні не правда(')
        btn6 = types.KeyboardButton('🔙 Головне меню')
        markup.add(btn1, btn2, btn6)
        bot.send_message(message.from_user.id, '⬇ Выберите подраздел', reply_markup=markup)

    elif message.text == 'Ти впевнений?!':
        bot.send_message(message.from_user.id, "Так!!")

    elif message.text == 'Ні не правда(':
        bot.send_message(message.from_user.id, "Правда😡🤬")

    elif message.text == '📑 dfsdf':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('💻 Пари Поліни ')
        btn2 = types.KeyboardButton('🖥 Пари Саши ')
        markup.add(btn1,btn2 )
        bot.send_message(message.from_user.id,'⬇ Выберите подраздел ',  reply_markup=markup)


    elif message.text == '📑 Пари':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('💻 Пари на першу неділю')
        btn2 = types.KeyboardButton('💻 Пари на другу неділю')
        btn3 = types.KeyboardButton('💻 Пари на сьогодні')
        btn4 = types.KeyboardButton('💻 Поточна пара')
        btn6 = types.KeyboardButton('🔙 Головне меню')
        markup.add(btn1, btn2,btn3,btn4,btn6)
        bot.send_message(message.from_user.id, '⬇ обери що тобі потрібно зараз  ', reply_markup=markup)

    elif message.text == '💻 Поточна пара':
        x = datetime.now()
        f = date(x.year, x.month, x.day)
        s = date(2023, 2, 6)
        delta = f - s
        if (round((delta.days) / 7)) % 2 != 0:
            if x.strftime("%A")=="Monday":
                if x.hour<10 and x.hour>8:
                    bot.send_message(message.from_user.id, "В тебе немає першої пари йди спи)")
                elif (x.hour==10 or x.hour==11)  and x.hour<12:
                    bot.send_message(message.from_user.id, "В тебе зараз  міграіця токсикантів в біосфері (лекція)")
                elif (x.hour==12 or x.hour==13 and x.minute>=20) and x.hour<14:
                    bot.send_message(message.from_user.id, "В тебе відсутня 3 пара)")
                elif (x.hour == 14 or x.hour==15 and x.minute >= 15) and x.hour < 16:
                   bot.send_message(message.from_user.id,  "Остання пара на сьогодні ландшафтна екологія (лекція)")
                else:
                   bot.send_message(message.from_user.id, "Пари на сьогодні закінчилися все)")
            elif x.strftime("%A") == "Tuesday":
                if x.hour<10 and x.hour>8:
                    bot.send_message(message.from_user.id, "В тебе немає першої пари йди спи)")
                elif x.hour==10 or x.hour==11  and x.hour<12:
                    bot.send_message(message.from_user.id, "В тебе зараз кліматологія (практики)")
                elif x.hour==12 or x.hour==13 and x.hour<14:
                    bot.send_message(message.from_user.id, "Остання пара на сьогодні гідрологія(практки)")
                else:
                    bot.send_message(message.from_user.id, "Пари на сьогодні закінчилися все)")
            elif x.strftime("%A") == "Wednesday":
                if x.hour < 10 and x.hour > 8:
                    bot.send_message(message.from_user.id, "В тебе зараз ФП")
                elif x.hour > 10 and x.hour < 16:
                    bot.send_message(message.from_user.id, "В тебе відсутні пари з 2 по 4 тому йди відпочивай")
                elif (x.hour == 16 and x.minute>10) or (x.hour < 17 and x.minute<45):
                    bot.send_message(message.from_user.id, "Остання пара на сьогодні ландшафтна екологія (лекція)")
                else:
                    bot.send_message(message.from_user.id, "Пари на сьогодні закінчилися все)")
            elif x.strftime("%A") == "Thursday":
                if x.hour<10 and x.hour>8:
                    bot.send_message(message.from_user.id, "В тебе немає першої пари йди спи)")
                elif x.hour==10 or x.hour==11  and x.hour<12:
                    bot.send_message(message.from_user.id, "В тебе зараз аналітична хімія (лекція")
                elif x.hour==12 or x.hour==13 and x.hour<14:
                    bot.send_message(message.from_user.id, "В тебе зараз моніторинг давкіля (лекція)")
                elif (x.hour == 14 or x.hour==15 and x.minute >= 15) and x.hour < 16:
                   bot.send_message(message.from_user.id,  "В тебе зараз гідрологія (лекція)")
                elif (x.hour == 16 and x.minute > 10) or (x.hour < 17 and x.minute < 45):
                    bot.send_message(message.from_user.id, "Остання пара на сьогодні кліматологія (лекція)")
                else:
                    bot.send_message(message.from_user.id, "Пари на сьогодні закінчилися все)")
            elif x.strftime("%A") == "Friday":
                if x.hour < 10 and x.hour > 8:
                    bot.send_message(message.from_user.id, "В тебе немає першої пари йди спи)")
                elif x.hour == 10 or x.hour == 11 and x.hour < 12:
                    bot.send_message(message.from_user.id, "В тебе одна эдина пара на сьогодны це іноземна мова")
                else:
                    bot.send_message(message.from_user.id, "Пари на сьогодні закінчилися все)")
            else:
                bot.send_message(message.from_user.id," Хей сьогодні вихідні які пари? з глузду зіхала чи як?)")
        else:
            if x.strftime("%A") == "Monday":
                if x.hour < 10 and x.hour > 8:
                    bot.send_message(message.from_user.id, "В тебе немає першої пари йди спи)")
                elif (x.hour == 10 or x.hour == 11) and x.hour < 12:
                    bot.send_message(message.from_user.id, "В тебе зараз  міграіця токсикантів в біосфері (лекція)")
                elif (x.hour == 12 or x.hour == 13 and x.minute >= 20) and x.hour < 14:
                    bot.send_message(message.from_user.id, "В тебе відсутня 3 пара)")
                elif (x.hour == 14 or x.hour == 15 and x.minute >= 15) and x.hour < 16:
                    bot.send_message(message.from_user.id, "Остання пара на сьогодні ландшафтна екологія (лекція)")
                else:
                    bot.send_message(message.from_user.id, "Пари на сьогодні закінчилися все)")
            elif x.strftime("%A") == "Tuesday":
                if x.hour < 10 and x.hour > 8:
                    bot.send_message(message.from_user.id, "В тебе зараз аналітична хімія")
                elif x.hour == 10 or x.hour == 11 and x.hour < 12:
                    bot.send_message(message.from_user.id, "остання на сьогодні пара аналітична хімія ")
                else:
                    bot.send_message(message.from_user.id, "Пари на сьогодні закінчилися все)")
            elif x.strftime("%A") == "Wednesday":
                if x.hour < 10 and x.hour > 8:
                    bot.send_message(message.from_user.id, "В тебе одна пара на сьогодні це ФП")
                else:
                    bot.send_message(message.from_user.id, "Пари на сьогодні закінчилися все)")
            elif x.strftime("%A") == "Thursday":
                if x.hour < 10 and x.hour > 8:
                    bot.send_message(message.from_user.id, "В тебе немає першої пари йди спи)")
                elif x.hour == 10 or x.hour == 11 and x.hour < 12:
                    bot.send_message(message.from_user.id, "В тебе зараз аналітична хімія (лекція")
                elif x.hour == 12 or x.hour == 13 and x.hour < 14:
                    bot.send_message(message.from_user.id, "В тебе зараз моніторинг давкіля (лекція)")
                elif (x.hour == 14 or x.hour == 15 and x.minute >= 15) and x.hour < 16:
                    bot.send_message(message.from_user.id, "В тебе зараз гідрологія (лекція)")
                elif (x.hour == 16 and x.minute > 10) or (x.hour < 17 and x.minute < 45):
                    bot.send_message(message.from_user.id, "Остання пара на сьогодні кліматологія (лекція)")
                else:
                    bot.send_message(message.from_user.id, "Пари на сьогодні закінчилися все)")
            elif x.strftime("%A") == "Friday":
                if x.hour < 10 and x.hour > 8:
                    bot.send_message(message.from_user.id, "В тебе немає першої пари йди спи)")
                elif x.hour == 10 or x.hour == 11 and x.hour < 12:
                    bot.send_message(message.from_user.id, "В тебе зараз іноземна мова")
                elif x.hour == 12 or x.hour == 13 and x.hour < 14:
                    bot.send_message(message.from_user.id, "В тебе зараз моніторинг давкіля (практики)")
                elif (x.hour == 14 or x.hour == 15 and x.minute >= 15) and x.hour < 16:
                    bot.send_message(message.from_user.id, "В тебе зараз міграіця токсикантів в біосфері (лаб)")
                elif (x.hour == 16 and x.minute > 10) or (x.hour < 17 and x.minute < 45):
                    bot.send_message(message.from_user.id, "Остання пара на сьогодні міграіця токсикантів в біосфері (лаб)")
                else:
                    bot.send_message(message.from_user.id, "Пари на сьогодні закінчилися все)")
            else:
                bot.send_message(message.from_user.id, " Хей сьогодні вихідні які пари? з глузду зіхала чи як?)")

    elif message.text == '💻 Пари на першу неділю':
        bot.send_message(message.from_user.id, "--------------\n"
                                               "Понеділок!\n"
                                               "1. Можна по спати\n"
                                               "2. Міграіця токсикантів в біосфері (лекція)\n"
                                               "3. Відсутня\n"
                                               "4. Ландшафтна екологія (лекція)\n"
                                               "--------------\n"
                                               "Вівторок!\n"
                                               "1. Можна по спати\n"
                                               "2. Кліматологія (практики)\n"
                                               "3. Гідрологія(практки)\n"
                                               "--------------\n"
                                               "Середа!\n"
                                               "1. ФП\n"
                                               "2-4 відсутні пари\n"
                                               "5. Ландшафтна екологія (лекція)\n"
                                               "--------------\n"
                                               "Четвер!\n"
                                               "1. Можна по спати\n"
                                               "2. Аналітична хімія (лекція)\n"
                                               "3. Моніторинг давкіля (лекція)\n"
                                               "4. Гідрологія (лекція)\n"
                                               "5. Кліматологія (лекція)\n"
                                               "--------------\n"
                                               "П'ятниця!\n"
                                               "1. Можна спати\n"
                                               "2. іноземна мова (практики)\n"
                                                "--------------\n")

    elif message.text == '💻 Пари на другу неділю':
        x = datetime.now()
        bot.send_message(message.from_user.id, "--------------\n"
                                               "Понеділок!\n"
                                               "1. Можна по спати\n"
                                               "2. Міграіця токсикантів в біосфері (лекція)\n"
                                               "3. Відсутня\n"
                                               "4. Ландшафтна екологія (лекція)\n"
                                               "--------------\n"
                                               "Вівторок!\n"
                                               "1. Аналітична хімія (лаб)\n"
                                               "2. Аналітична хімія (лаб)\n"
                                               "--------------\n"
                                               "Середа!\n"
                                               "1. ФП\n"
                                               "--------------\n"
                                               "Четвер!\n"
                                               "1. Можна по спати\n"
                                               "2. Аналітична хімія (лекція)\n"
                                               "3. Моніторинг давкіля (лекція)\n"
                                               "4. Гідрологія (лекція)\n"
                                               "5. Кліматологія (лекція)\n"
                                               "--------------\n"
                                               "П'ятниця!\n"
                                               "1. Можна спати\n"
                                               "2. іноземна мова (практики)\n"
                                               "3. Моніторинг давкіля (практики)\n"
                                               "4. Міграіця токсикантів в біосфері (лаб)\n"
                                               "5. Міграіця токсикантів в біосфері (лаб)\n"
                                               "--------------\n")

        print(x.hour, x.minute)
        print(x.strftime("%A"))
        if x.strftime("%A")=="Saturday":
            print("asdsad")

    elif message.text == '💻 Пари на сьогодні':
        x = datetime.now()
        f = date(x.year,x.month,x.day)
        print(f)
        s = date(2023, 2, 6)
        delta = f - s
        print(delta)
        print(round((delta.days)/7))
        if (round((delta.days)/7))%2!=0:
            if x.strftime("%A")=="Monday":
                bot.send_message(message.from_user.id,"Сьогодні в нас понеділок тому пари ось такі\n"
                                               "1. Можна по спати\n"
                                               "2. Міграіця токсикантів в біосфері (лекція)\n"
                                               "3. Відсутня\n"
                                               "4. Ландшафтна екологія (лекція)\n")
            elif x.strftime("%A") == "Tuesday":
                bot.send_message(message.from_user.id,  "Сьогодні в нас вівторок тому пари ось такі\n"
                                               "1. Можна по спати\n"
                                               "2. Кліматологія (практики)\n"
                                               "3. Гідрологія(практки)\n")
            elif x.strftime("%A") == "Wednesday":
                bot.send_message(message.from_user.id, "Сьогодні в нас середа тому пари ось такі\n"
                                               "1. ФП\n"
                                               "2-4 відсутні пари\n"
                                               "5. Ландшафтна екологія (лекція)\n")
            elif x.strftime("%A") == "Thursday":
                bot.send_message(message.from_user.id, "Сьогодні в нас четвер тому пари ось такі\n"
                                               "1. Можна по спати\n"
                                               "2. Аналітична хімія (лекція)\n"
                                               "3. Моніторинг давкіля (лекція)\n"
                                               "4. Гідрологія (лекція)\n"
                                               "5. Кліматологія (лекція)\n")
            elif x.strftime("%A") == "Friday":
                bot.send_message(message.from_user.id,"Сьогодні в нас п'ятниця тому пари ось такі\n"
                                               "1. Можна спати\n"
                                               "2. іноземна мова (практики)\n")
            else:
                bot.send_message(message.from_user.id," Хей сьогодні вихідні які пари? з глузду зіхала чи як?)")
        else:
            if x.strftime("%A")=="Monday":
                bot.send_message(message.from_user.id,"Сьогодні в нас понеділок тому пари ось такі\n"
                                               "1. Можна по спати\n"
                                               "2. Міграіця токсикантів в біосфері (лекція)\n"
                                               "3. Відсутня\n"
                                               "4. Ландшафтна екологія (лекція)\n")
            elif x.strftime("%A") == "Tuesday":
                bot.send_message(message.from_user.id,  "Сьогодні в нас вівторок тому пари ось такі\n"
                                               "1. Аналітична хімія (лаб)\n"
                                               "2. Аналітична хімія (лаб)\n")
            elif x.strftime("%A") == "Wednesday":
                bot.send_message(message.from_user.id, "Сьогодні в нас середа тому пари ось такі\n"
                                               "1. ФП\n")
            elif x.strftime("%A") == "Thursday":
                bot.send_message(message.from_user.id, "Сьогодні в нас четвер тому пари ось такі\n"
                                              "1. Можна по спати\n"
                                               "2. Аналітична хімія (лекція)\n"
                                               "3. Моніторинг давкіля (лекція)\n"
                                               "4. Гідрологія (лекція)\n"
                                               "5. Кліматологія (лекція)\n")
            elif x.strftime("%A") == "Friday":
                bot.send_message(message.from_user.id,"Сьогодні в нас п'ятниця тому пари ось такі\n"
                                               "1. Можна спати\n"
                                               "2. іноземна мова (практики)\n"
                                               "3. Моніторинг давкіля (практики)\n"
                                               "4. Міграіця токсикантів в біосфері (лаб)\n"
                                               "5. Міграіця токсикантів в біосфері (лаб)\n")
            else:
                bot.send_message(message.from_user.id," Хей сьогодні вихідні які пари? з глузду зіхала чи як?)")



#Monday  Tuesday  Wednesday   Thursday   Friday
        # Small talk
    elif message.text == 'Привет!':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'привет!':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'как дела?':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'Как дела?':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'Что делаешь?':
        bot.send_message(message.from_user.id, 'Помогаю людям!')

    elif message.text == 'что делаешь?':
        bot.send_message(message.from_user.id, 'Помогаю людям!')

    elif message.text == 'как дела':
        bot.send_message(message.from_user.id, 'Хорошо!')


    # English Language
    elif message.text == '🇬🇧 English':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Повернутися до вибору мову")
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'ой начебто ти справді збираєшся використовувати англійскю версію😌',
                         reply_markup=markup)





bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть