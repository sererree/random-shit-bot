from aiogram import Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

router = Router()


@router.message(Command("menu"))
async def show_menu(message: Message) -> None:
    keyboard = [
        [InlineKeyboardButton(text="хочу цитату", callback_data="quote")],
        [InlineKeyboardButton(text="хочу добавить цитату", callback_data="new_quote")]

    ]

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    await message.answer("чего хочешь", reply_markup=markup)
