from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import random
from . import my_list

router = Router()


def get_rand_quote() -> str:
    i = random.randrange((len(my_list.my_list)))
    return my_list.my_list[i]


@router.message(Command('quote'))
async def command_about(message: Message) -> None:
    i = random.randrange((len(my_list.my_list)))
    await message.answer(get_rand_quote())


@router.callback_query(F.data == "quote")
async def on_callback(query: CallbackQuery) -> None:
    i = random.randrange((len(my_list.my_list)))
    await query.message.answer(get_rand_quote())
    print(query)
