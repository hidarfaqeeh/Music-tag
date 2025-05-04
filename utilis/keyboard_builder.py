
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def build_edit_keyboard(tags):
    buttons = []
    fields = {
        "title": "العنوان",
        "artist": "الفنان",
        "album": "الألبوم",
        "tracknumber": "رقم المقطع",
        "year": "تاريخ الإصدار",
        "genre": "النوع",
        "comment": "تعليق",
        "lyrics": "كلمات الأغنية",
        "albumartist": "فنان الألبوم",
        "conductor": "الموزع",
        "composer": "الملحن",
        "lyricist": "كاتب الكلمات",
        "publisher": "الناشر",
        "copyright": "حقوق النشر",
        "website": "الموقع الرسمي"
    }

    for key, label in fields.items():
        buttons.append([InlineKeyboardButton(text=label, callback_data=f"edit_{key}")])

    control_buttons = [
        [InlineKeyboardButton(text="عرض كلمات الأغنية", callback_data="show_lyrics")],
        [InlineKeyboardButton(text="حذف الوسوم", callback_data="clear_tags")],
        [InlineKeyboardButton(text="تطبيق الحقوق الافتراضية", callback_data="apply_defaults")],
        [InlineKeyboardButton(text="حفظ الملف", callback_data="save_file")],
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons + control_buttons)
