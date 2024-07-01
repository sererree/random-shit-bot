from aiogram import Router

from . import menu, quote, start, new_quote, my_list, send_quotes

router = Router()

router.include_routers(
    start.router,
    menu.router,
    quote.router,
    new_quote.router,
    send_quotes.router


)