
# MP3 Tag Editor Bot

بوت تيليجرام لتعديل وسوم ملفات MP3 بسهولة باستخدام Python وAiogram.

## كيفية التشغيل

### على VPS:

```bash
git clone https://github.com/your-repo/mp3-tag-editor-bot.git
cd mp3-tag-editor-bot
bash start.sh
```

### على Heroku / Railway / Render:

- قم بإنشاء مشروع جديد.
- ارفع الملفات التالية:
  - `bot.py`
  - `handlers/`, `utils/`, `states/`, `config.py`, `downloads/`
  - `requirements.txt`
  - `Procfile`
- حدد `python` كلغة، و`Procfile` لتشغيل البوت.
- ضع متغير `BOT_TOKEN` في إعدادات البيئة.

### الإعداد:

قم بتعديل `config.py` وضع توكن البوت الخاص بك هناك أو استخدم متغيرات بيئة في النظام.

**المطور**: @yourusername
