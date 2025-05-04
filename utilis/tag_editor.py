
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, USLT
from config import DEFAULT_TAGS

def extract_tags(file_path):
    tags = {}
    audio = EasyID3(file_path)
    for key in audio.keys():
        tags[key] = audio.get(key, [""])[0]
    return tags

def update_tag(file_path, key, value):
    audio = EasyID3(file_path)
    audio[key] = value
    audio.save()

def clear_tags(file_path):
    audio = EasyID3(file_path)
    audio.clear()
    audio.save()

def apply_default_tags(file_path):
    audio = EasyID3(file_path)
    for key, value in DEFAULT_TAGS.items():
        if key in audio.valid_keys.keys():
            audio[key] = value
    audio.save()

def get_album_cover(file_path):
    audio = ID3(file_path)
    for tag in audio.values():
        if isinstance(tag, APIC):
            return tag.data
    return None

def get_lyrics(file_path):
    audio = ID3(file_path)
    for tag in audio.values():
        if isinstance(tag, USLT):
            return tag.text
    return None
