from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from utils.prompts import load_message

router = Router()

# Команда /start — отображение меню
@router.message(F.text == "/start")
async def start_command(message: Message):
    text = load_message("main.txt")
    image = FSInputFile("images/avatar_main.jpg")

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎲 Рандомный факт", callback_data="random")],
        [InlineKeyboardButton(text="💬 Задать вопрос", callback_data="gpt")],
        [InlineKeyboardButton(text="👤 Поговорить с личностью", callback_data="talk")],
        [InlineKeyboardButton(text="❓ Квиз", callback_data="quiz")],
        [InlineKeyboardButton(text="🌐 Переводчик", callback_data="translate")],
        [InlineKeyboardButton(text="🎬 Рекомендации", callback_data="recommend")],
    ])

    await message.answer_photo(photo=image, caption=text, reply_markup=kb)


# Колбэк, если пользователь нажал "Закончить"
@router.callback_query(F.data == "start")
async def start_callback(callback: CallbackQuery):
    await start_command(callback.message)
