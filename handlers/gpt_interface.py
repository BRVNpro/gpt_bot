from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, FSInputFile

from utils.chatgpt_instance import gpt
from utils.prompts import load_prompt

router = Router()

DEFAULT_GPT_PROMPT = load_prompt("gpt.txt")


class GPTState(StatesGroup):
    waiting_for_question = State()


@router.message(F.text == "/gpt")
async def gpt_start(message: Message, state: FSMContext):
    image = FSInputFile("images/gpt.jpg")
    await message.answer_photo(image, caption="💬 Отправь свой вопрос.")
    await state.set_state(GPTState.waiting_for_question)


@router.callback_query(F.data == "gpt")
async def gpt_callback(callback: CallbackQuery, state: FSMContext):
    await gpt_start(callback.message, state)


@router.message(GPTState.waiting_for_question)
async def gpt_process(message: Message, state: FSMContext):
    await state.clear()
    user_text = message.text
    await message.answer("⏳ Думаю...")

    try:
        response = await gpt.send_question(DEFAULT_GPT_PROMPT, user_text)
        await message.answer(response)
    except Exception as e:
        await message.answer(f"⚠️ Ошибка: {e}")