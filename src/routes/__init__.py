from aiogram import Router

from . import menu, quote, start, new_quote, my_list

router = Router()

router.include_routers(
    start.router,
    menu.router,
    quote.router,
    new_quote.router,


)