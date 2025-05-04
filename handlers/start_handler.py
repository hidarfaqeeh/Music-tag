
from aiogram import Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

@router.message(commands=["start"])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="قناة المطور", url="https://t.me/yourchannel")],
        [InlineKeyboardButton(text="المطور", url="https://t.me/yourusername")],
        [InlineKeyboardButton(text="اللغة: العربية", callback_data="lang_ar")]
    ])
    await message.answer(
        "أهلاً بك في بوت تعديل وسوم MP3!

"
        "قم بإرسال أي ملف MP3 وسأعرض لك معلوماته الحالية ويمكنك تعديلها بسهولة عبر الأزرار.",
        reply_markup=keyboard
    )
