# Импортируем модули
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем токен Telegram из переменных окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Получаем токен OpenAI из переменных окружения
OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")

OPENAI_PROXY = os.getenv("OPENAI_PROXY")


# Если какой-то токен не найден — можно сразу здесь выкинуть ошибку (по желанию)
if not TELEGRAM_TOKEN:
    raise ValueError("❗ TELEGRAM_TOKEN не найден в .env")

if not OPENAI_TOKEN:
    raise ValueError("❗ OPENAI_TOKEN не найден в .env")

if not OPENAI_PROXY:
    raise ValueError("❗ OPENAI_PROXY не найден в .env")