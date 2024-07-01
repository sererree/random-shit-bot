from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import random
from src import list

router = Router()


def get_rand_quote() -> str:
    i = random.randrange((len(list.my_list)))
    return list.my_list[i]

@router.message(Command('send_quotes'))
async def command_about(message: Message) -> None:
    i = random.randrange((len(list.my_list)))
    await message.answer(get_rand_quote())

@router.callback_query(F.data == "send_quotes")
async def on_callback(query: CallbackQuery) -> None:
    i = random.randrange((len(list.my_list)))
    await query.message.answer(get_rand_quote())