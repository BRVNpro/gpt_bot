from aiogram.fsm.state import State, StatesGroup

class QuizStates(StatesGroup):
    selecting_topic = State()
    waiting_for_answer = State()
