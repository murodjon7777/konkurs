from aiogram.dispatcher.filters.state import StatesGroup,State


class PersonalData(StatesGroup):
    tildan=State()
    tilga=State()
    matn=State()