
from aiogram.fsm.state import StatesGroup, State

class EditState(StatesGroup):
    waiting_for_field_input = State()
