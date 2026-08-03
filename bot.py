import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# TOKENINGIZNI SHUYERGA YOZING
TOKEN = "TOKENINGIZNI_SHU_YERGA_QO'YING"

# Tugmalar (Bog'lanish uchun bot havolasi qo'yildi)
main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🚗 Evroprotokol", callback_data="evroprotokol")],
        [InlineKeyboardButton(text="📋 Avtobaxolash", callback_data="avtobaxolash")],
        [InlineKeyboardButton(text="🛡 Avtosugurta", callback_data="avtosugurta")],
        [InlineKeyboardButton(text="📞 Biz bilan bog'lanish", url="https://t.me/yandex_rasmiy_bot")]
    ]
)

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    text = "<b>Assalomu alaykum! Avto Xamroh botga xush kelibsiz.</b>"
    await message.answer(text, reply_markup=main_keyboard, parse_mode=ParseMode.HTML)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
