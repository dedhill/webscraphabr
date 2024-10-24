import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.config import TOKEN
from app.handlers import router


bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=1)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")