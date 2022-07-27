from aiogram import types
from dispatcher import dp
import config

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@dp.message_handler(is_owner=True, commands=["post"])
async def post_command(message: types.Message):
    config.IS_POSTING_REQUESTED = True

    await message.answer("Пришлите текст поста (с картинкой или без):")

@dp.message_handler(is_owner=True, commands=["setlink"])
async def setlink_command(message: types.Message):
    with open("link.txt", "+w") as f:
        f.write(message.text.replace("/setlink ", "").strip())
        f.close()

    await message.answer("Ссылка успешно сохранена!")

@dp.message_handler(is_owner=True, commands=["getlink"])
async def getlink_command(message: types.Message):
    with open("link.txt", "r") as f:
        content = f.readlines()
        f.close()

    await message.answer("Текущая ссылка: {}".format(content[0].strip()))

@dp.message_handler(is_owner=True)
async def messages_handler(message: types.Message):
    if config.IS_POSTING_REQUESTED:
        config.IS_POSTING_REQUESTED = False

        inline_btn = InlineKeyboardButton("Получить ссылку!", callback_data="get_link_button")
        inline_kb = InlineKeyboardMarkup().add(inline_btn)

        await message.bot.send_message(config.CHANNEL_ID, message.text, reply_markup=inline_kb)

        await message.answer("Пост опубликован!")




