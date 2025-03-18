from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.filters import CommandStart
import asyncio

API_TOKEN = "8192515613:AAE0YgyWs_aDdmSk_5UHEzX74rAPn-Nj5v4"

# Создайте роутер
router = Router()

# Регистрация обработчиков через фильтры
@router.message(CommandStart())
async def start_command(message: types.Message, bot: Bot):
    # Получите информацию о боте
    bot_info = await bot.get_me()
    bot_username = bot_info.username

    # Создайте InlineKeyboardMarkup с корректным URL
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="🔮 Запустить",
                    url="https://neosomee.github.io/InvisibleBot/"  
                )
            ]
        ]
    )
    await message.answer(
        "🎥 Откройте эффект плаща невидимки в приложении!",
        reply_markup=keyboard
    )

async def main():
    # Создайте бота и диспетчер
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    
    # Подключите роутер к диспетчеру
    dp.include_router(router)
    
    # Запуск бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
