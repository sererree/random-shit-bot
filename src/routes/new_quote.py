from aiogram.types import Message, CallbackQuery
from src.bot import bot
from aiogram import Router, F, Dispatcher
from aiogram.filters import Command




router = Router()
# dp = Dispatcher(bot)

# @dp.message_handler
# async def new(message: Message):
#     list.append(message.text)




@router.message(Command('new_quote'))
async def command_about(message: Message) -> None:
    await message.answer("пока нельзя")


@router.callback_query(F.data == "new_quote")
async def on_callback(query: CallbackQuery) -> None:
    await query.message.answer("пока нельзя")

