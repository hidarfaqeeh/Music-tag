
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from utils.tag_editor import extract_tags, save_file, get_album_cover
from utils.formatter import format_tags_caption
from utils.keyboard_builder import build_edit_keyboard
import os

router = Router()

@router.message(F.audio)
async def handle_audio(message: types.Message, state: FSMContext):
    file = await message.bot.get_file(message.audio.file_id)
    file_path = file.file_path
    downloaded_file = await message.bot.download_file(file_path)
    file_name = f"downloads/{message.audio.file_unique_id}.mp3"
    os.makedirs("downloads", exist_ok=True)
    with open(file_name, "wb") as f:
        f.write(downloaded_file.read())

    tags = extract_tags(file_name)
    album_cover = get_album_cover(file_name)

    caption = format_tags_caption(tags)
    keyboard = build_edit_keyboard(tags)

    if album_cover:
        await message.answer_photo(photo=album_cover, caption=caption, reply_markup=keyboard)
    else:
        await message.answer(caption, reply_markup=keyboard)

    await state.update_data(file_path=file_name, tags=tags)
