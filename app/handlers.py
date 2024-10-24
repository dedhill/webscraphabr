from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from app.scrape import scrape
from app.config import list, links
from aiogram import Router

router = Router()

btn = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="/help")]
])

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello thats web scrapper bot for habr.com", reply_markup=btn)

@router.message(Command('help'))
async def btc(message: Message):
    list_in = 1
    await scrape()
    for i in list:
            await message.answer(f"{str(list[list_in])}, \n {str(links[list_in])}" )
            list_in = list_in + 1
    list.clear()
