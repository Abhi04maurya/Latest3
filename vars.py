#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "3670291"))
API_HASH = environ.get("API_HASH", "1f55b2e9d972c3a5ac3f008c51ed7a4a")
BOT_TOKEN = environ.get("BOT_TOKEN", "8045546324:AAGZ3Gvs9CKGoaEY9IWw4vWVMwGPYGDUlgg")
OWNER = int(environ.get("OWNER", "659925627"))
CREDIT = "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"
AUTH_USER = os.environ.get('AUTH_USERS', '659925627').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


