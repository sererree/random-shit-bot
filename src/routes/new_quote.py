from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

router = Router()

@router.message(Command('new_quote'))
async def command_about(message: Message) -> None:
    await message.answer("пока нельзя")

@router.callback_query(F.data == "new_quote")
async def on_callback(query: CallbackQuery) -> None:
    await query.message.answer("пока нельзя")
