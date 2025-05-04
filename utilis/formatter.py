
def format_tags_caption(tags):
    caption = "وسوم الملف الصوتي:

"
    fields = {
        "title": "العنوان",
        "artist": "الفنان",
        "album": "الألبوم",
        "tracknumber": "رقم المقطع",
        "year": "تاريخ الإصدار",
        "genre": "النوع",
        "comment": "تعليق",
        "albumartist": "فنان الألبوم",
        "conductor": "الموزع",
        "composer": "الملحن",
        "lyricist": "كاتب الكلمات",
        "publisher": "الناشر",
        "copyright": "حقوق النشر",
        "website": "الموقع الرسمي",
        "lyrics": "كلمات الأغنية"
    }
    for key, label in fields.items():
        caption += f"{label}: {tags.get(key, '❌')}
"
    return caption
