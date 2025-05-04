
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import BOT_TOKEN
from handlers import start_handler, audio_handler, edit_handler

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_routers(
        start_handler.router,
        audio_handler.router,
        edit_handler.router
    )

    await bot.set_my_commands([
        BotCommand(command="start", description="ابدأ استخدام البوت")
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
