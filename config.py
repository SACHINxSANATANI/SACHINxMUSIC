import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_USERNAME = getenv("OWNER_USERNAME","V_VIP_OWNER")
BOT_USERNAME = getenv("BOT_USERNAME","HIMANSHI_MUSIC_BOT")
BOT_NAME = getenv("BOT_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", None))
OWNER_ID = int(getenv("OWNER_ID", 5959548791))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SACHINxSANATANI/SACHINxMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/All_SANATANI_BOT")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+Ckzm2ypQyIIzZTll")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph//file/8851111e156d9219d2e9c.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph//file/a15788e80dbe3249fbd05.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/9acd828ec45a363add2e9.jpg"
STATS_IMG_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
