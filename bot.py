import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from utils.config import TELEGRAM_TOKEN
from utils.logger import setup_logger

# Импортируем все хендлеры
from handlers import (
    start,
    random_fact,
    gpt_interface,
    talk,
    quiz,
    translator,
    recommendations,
    help as help_handler
)

async def main():
    # Инициализация логгера
    setup_logger()

    # Создание экземпляра бота с HTML-разметкой по умолчанию
    bot = Bot(
        token=TELEGRAM_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    # FSM-память в оперативке
    dp = Dispatcher(storage=MemoryStorage())

    # Подключаем все роутеры
    dp.include_routers(
        start.router,
        random_fact.router,
        gpt_interface.router,
        talk.router,
        quiz.router,
        translator.router,
        recommendations.router,
        help_handler.router,
    )

    # Настройка списка команд для /menu
    await bot.set_my_commands([
        BotCommand(command="start", description="Запуск"),
        BotCommand(command="random", description="Рандомный факт"),
        BotCommand(command="gpt", description="Свободный вопрос к ChatGPT"),
        BotCommand(command="talk", description="Поговорить с личностью"),
        BotCommand(command="quiz", description="Квиз по теме"),
        BotCommand(command="help", description="Справка по боту"),
        BotCommand(command="translate", description="Переводчик"),
        BotCommand(command="recommend", description="Рекомендации"),
    ])

    print("✅ Бот запущен...")
    await dp.start_polling(bot)


# Точка входа
if __name__ == "__main__":
    asyncio.run(main())
