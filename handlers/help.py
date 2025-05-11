# Импорт стандартных вещей
from aiogram import Router, F
from aiogram.types import Message

# Импорт функции для чтения файла
from utils.prompts import load_prompt

# Создаём роутер
router = Router()

# Команда /help показывает инструкции
@router.message(F.text == "/help")
async def help_command(message: Message):
    # Загружаем текст справки из файла messages/main.txt
    text = load_prompt("main.txt")

    try:
        # Отправляем справку
        await message.answer(text)
    except Exception as e:
        await message.answer(f"⚠️ Не удалось показать справку: {e}")
