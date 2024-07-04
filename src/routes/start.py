import os.path

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.routes import menu
from src import local
import json

router = Router()


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    local.add_user(message.from_user.id, False)
    await menu.show_menu(message)
