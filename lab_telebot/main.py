import telebot

class TodoBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.todo_list = []

    def start(self):
        @self.bot.message_handler(commands=['start'])
        def start(message):
            self.bot.reply_to(message, 'Привет! Это твой список задач. Чтобы добавить задачу, используй команду /create.')

        @self.bot.message_handler(commands=['create'])
        def create_item(message):
            item = message.text.split('/create ')[1]
            self.todo_list.append(item)
            self.bot.reply_to(message, f'Задача "{item}" добавлена в список.')

        @self.bot.message_handler(commands=['read'])
        def read_items(message):
            if len(self.todo_list) > 0:
                response = 'Список задач:\n'
                for index, item in enumerate(self.todo_list, start=1):
                    response += f'{index}. {item}\n'
            else:
                response = 'Список задач пуст.'
            self.bot.reply_to(message, response)

        @self.bot.message_handler(commands=['update'])
        def update_item(message):
            index, new_item = message.text.split('/update ')[1].split(' ', 1)
            index = int(index) - 1
            if 0 <= index < len(self.todo_list):
                self.todo_list[index] = new_item
                self.bot.reply_to(message, f'Задача обновлена: "{new_item}"')
            else:
                self.bot.reply_to(message, 'Неверный индекс задачи.')

        @self.bot.message_handler(commands=['delete'])
        def delete_item(message):
            index = int(message.text.split('/delete ')[1]) - 1
            if 0 <= index < len(self.todo_list):
                deleted_item = self.todo_list.pop(index)
                self.bot.reply_to(message, f'Задача "{deleted_item}" удалена из списка.')
            else:
                self.bot.reply_to(message, 'Неверный индекс задачи.')

        self.bot.polling()


bot = TodoBot('5997376678:AAG_FfCwGbJ8Iu-jJ2fVs_BwKWo6jI4cm_w')
bot.start()
