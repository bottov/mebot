#!./venv/bin/python3

import os
from datetime import datetime
from dotenv import load_dotenv
from telethon import TelegramClient, events

# Загрузка конфигурации
load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
SESSION = 'session'

# Словарь дат
lastDate = {}

# Переключатель on/off
switch = 'off'

# Создаем клиент
client = TelegramClient(SESSION, API_ID, API_HASH)

@client.on(events.NewMessage(pattern='/off'))
async def handler(event):
    global switch
    switch = 'off'

@client.on(events.NewMessage(outgoing=True, func=lambda e: e.is_private))
async def handler(event):

    if switch == 'on':

        # Берем текст оригинального сообщения
        original_message = event.raw_text
        
        # Преобразуем сообщение в красивый формат
        modified_message = f"✨__{original_message}__✨"

        # Если получателя нет в словаре дат или текущая дата не совпадает с датой в словаре
        if event.chat_id not in lastDate or lastDate[event.chat_id] != datetime.now().date():
            # то обновляем дату последнего сообщения пользователю
            lastDate[event.chat_id] = datetime.now().date()
            # добавляем подпись
            modified_message += "\n\n================\nмой канал @ainolik\nпортфолио @portfoliodev_bot"

        await event.edit(modified_message)  # редактируем сообщение
    print('chat_id >>', event.chat_id, 'switch >>', switch)

@client.on(events.NewMessage(pattern='/on'))
async def handler(event):
    global switch
    switch = 'on'

async def main():
    await client.start()
    print("Бот запущен...")
    await client.run_until_disconnected()

# Запускаем бота
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
