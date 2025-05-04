
#!/bin/bash
export $(grep -v '^#' .env | xargs)
pip install -r requirements.txt
python bot.py
