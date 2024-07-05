from aiogram import Dispatcher

from src.routes import send_quotes
from routes import router
import asyncio

from bot import bot


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)

    dp.startup.register(send_quotes.send_to_all_users)

    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())
