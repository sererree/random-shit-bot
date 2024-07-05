import asyncio
import random
import aioschedule
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from src import list, local
from src.bot import bot

router = Router()


def get_rand_quote() -> str:
    i = random.randrange((len(list.my_list)))
    return list.my_list[i]


@router.message(Command('send_quotes'))
async def command_about(message: Message) -> None:
    local.subscribe(message.from_user.id)
    await message.answer("будет смешни")


async def send_to_all_users() -> None:
    while True:
        print("Начинаю рассылку!")

        for users, data in local.users().items():
            print(f"Проверяю пользователя {users}")
            subscribed = data["subscribed"]

            if subscribed:
                quote = get_rand_quote()
                print(f"Отправляю этому пользователю цитату {quote}")
                await bot.send_message(chat_id=users, text=quote)

        await asyncio.sleep(120)


@router.callback_query(F.data == "send_quotes")
async def on_callback(query: CallbackQuery) -> None:
    local.subscribe(query.from_user.id)
    await query.message.answer("будет смешни")
