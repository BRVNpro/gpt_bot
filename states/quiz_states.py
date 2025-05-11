from aiogram.fsm.state import State, StatesGroup

# Состояния для квиза
class QuizStates(StatesGroup):
    selecting_topic = State()         # Пользователь выбирает тему
    waiting_for_answer = State()      # Бот ждёт ответ на вопрос
