from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from app.scrape import scrape
from app.config import list
from aiogram import Router

router = Router()

btn = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="/help")]
])

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello", reply_markup=btn)

@router.message(Command('help'))
async def btc(message: Message):
    await scrape()
    await message.answer(str(list[0]))
    list.clear()