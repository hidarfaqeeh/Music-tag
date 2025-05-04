
from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InputFile
from config import DEFAULT_TAGS
from states import EditState
from utils.tag_editor import update_tag, clear_tags, apply_default_tags, get_lyrics
from utils.formatter import format_tags_caption
from utils.keyboard_builder import build_edit_keyboard
import os

router = Router()

@router.callback_query()
async def process_callback(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    file_path = data.get("file_path")
    tags = data.get("tags", {})

    if call.data == "save_file":
        await call.message.answer_document(InputFile(file_path, filename="edited.mp3"))
        return

    if call.data == "clear_tags":
        clear_tags(file_path)
        await call.message.answer("تم حذف جميع الوسوم.")
    elif call.data == "apply_defaults":
        apply_default_tags(file_path)
        await call.message.answer("تم تطبيق الحقوق الافتراضية.")
    elif call.data == "show_lyrics":
        lyrics = get_lyrics(file_path)
        await call.message.answer(lyrics if lyrics else "لا توجد كلمات مسجلة.")
    elif call.data.startswith("edit_"):
        field = call.data.split("_", 1)[1]
        await state.set_state(EditState.waiting_for_field_input)
        await state.update_data(current_field=field)
        await call.message.answer(f"أدخل القيمة الجديدة لـ {field}:")
        return
    elif call.data == "back":
        pass  # سيُعاد عرض الوسوم

    # تحديث العرض
    from utils.tag_editor import extract_tags
    tags = extract_tags(file_path)
    caption = format_tags_caption(tags)
    keyboard = build_edit_keyboard(tags)
    await call.message.answer(caption, reply_markup=keyboard)
    await state.update_data(tags=tags)

@router.message(EditState.waiting_for_field_input)
async def process_field_input(message: types.Message, state: FSMContext):
    data = await state.get_data()
    file_path = data.get("file_path")
    field = data.get("current_field")
    update_tag(file_path, field, message.text)
    await message.answer(f"تم تحديث {field} بنجاح.")
    await state.clear()

    from utils.tag_editor import extract_tags
    from utils.formatter import format_tags_caption
    from utils.keyboard_builder import build_edit_keyboard

    tags = extract_tags(file_path)
    caption = format_tags_caption(tags)
    keyboard = build_edit_keyboard(tags)
    await message.answer(caption, reply_markup=keyboard)
    await state.update_data(tags=tags)
