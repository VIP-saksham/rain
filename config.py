import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ── Core bot config ────────────────────────────────────────────────────────────
API_ID = int(getenv("API_ID", 23806754))
API_HASH = getenv("API_HASH", "0b52aa37a124eb867ee42cbddcfbcb9f")
BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_ID = int(getenv("OWNER_ID", 7876850863))
OWNER_USERNAME = getenv("OWNER_USERNAME", "ihellxyz")
BOT_USERNAME = getenv("BOT_USERNAME", "RainXmusicbot")
BOT_NAME = getenv("BOT_NAME", "˹Rain ✘ 𝙼ᴜsɪᴄ˼ ♪")
ASSUSERNAME = getenv("ASSUSERNAME", "RainxAssistant")

# ── Database & logging ─────────────────────────────────────────────────────────
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOGGER_ID = int(getenv("LOGGER_ID", -1003169488913))

# ── Limits (durations in min/sec; sizes in bytes) ──────────────────────────────
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "1200"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "157286400"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1288490189999999"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "30"))

# ── External APIs ──────────────────────────────────────────────────────────────
COOKIE_URL = getenv("COOKIE_URL")  # required (paste link)
#API_URL = getenv("API_URL")        # optional
#API_KEY = getenv("API_KEY")        # optional
DEEP_API = getenv("DEEP_API")      # optional

API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
VIDEO_API_URL = getenv("VIDEO_API_URL", 'https://api.video.thequickearn.xyz')
API_KEY = getenv("API_KEY", None) # youtube song api key, generate free key or buy paid plan from panel.thequickearn.xyz

# ── Hosting / deployment ───────────────────────────────────────────────────────
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ── Git / updates ──────────────────────────────────────────────────────────────
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/VIP-saksham/rain")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Main")
GIT_TOKEN = getenv("GIT_TOKEN")  # needed if repo is private

# ── Support links ──────────────────────────────────────────────────────────────
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Team_Rdx_Network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/hellbotsupport")

# ── Assistant auto-leave ───────────────────────────────────────────────────────
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3600"))

# ── Debug ──────────────────────────────────────────────────────────────────────
DEBUG_IGNORE_LOG = True

# ── Spotify (optional) ─────────────────────────────────────────────────────────
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ── Session strings (optional) ─────────────────────────────────────────────────
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ── Media assets ───────────────────────────────────────────────────────────────
START_VIDS = [
    "https://strad-dev131.github.io/TeamXsrc/mp4/Music%20BOT.mp4",
    "https://strad-dev131.github.io/TeamXsrc/mp4/Music%20BOT%20(1).mp4",
    "https://strad-dev131.github.io/TeamXsrc/mp4/MUSIC%20BOT%20(2).mp4",
]
STICKERS = [
    "CAACAgUAAx0Cd6nKUAACASBl_rnalOle6g7qS-ry-aZ1ZpVEnwACgg8AAizLEFfI5wfykoCR4h4E",
    "CAACAgUAAx0Cd6nKUAACATJl_rsEJOsaaPSYGhU7bo7iEwL8AAPMDgACu2PYV8Vb8aT4_HUPHgQ",
]
HELP_IMG_URL = "https://files.catbox.moe/yg2vky.jpg"
PING_VID_URL = "https://files.catbox.moe/nzqd5x.mp4"
PLAYLIST_IMG_URL = "https://files.catbox.moe/did92w.jpg"
STATS_VID_URL = "https://files.catbox.moe/17lama.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/timwpo.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/timwpo.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/timwpo.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/hfda0r.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/xxx92j.jpg"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ── Helpers ────────────────────────────────────────────────────────────────────
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ───── Bot Introduction Messages ───── #
AYU = ["💞", "🦋", "🔍", "🧪", "⚡️", "🔥", "🎩", "🌈", "🍷", "🥂", "🥃", "🕊️", "🪄", "💌"]
AYUV = [
   "<b>────「 {1} 」────</b>\n\n</b>\b\b<b>𝐇єу 𝐓нєяє •🎙 {0} !\n🎵✨ᴅɪᴛᴄʜ ᴛʜᴇ ᴛʜʀᴇᴀᴅs, ʟᴇᴛ's ᴠɪʙᴇ ᴛᴏ ᴛʜᴇ ʀʜʏᴛʜᴍ.\nᴊᴏɪɴ ᴍᴇ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ's ᴄᴜᴛɪᴇsᴛ ᴍᴜsɪᴄ ʙᴏᴛ.🎶",
     "<b>❖ ʜᴇʏ :</b> <b>{0}</b> ⋆\n\n<b>๏ {1} [ 🇮🇳 ] : ғᴀsᴛ-ᴘᴏᴡᴇʀғᴜʟ ᴛɢ ʙᴏᴛ !</b>\n\n<b>๏ sᴍᴏᴏᴛʜ ʙᴇᴀᴛs • sᴛᴀʙʟᴇ & sᴇᴀᴍʟᴇss ᴍᴜsɪᴄ ғʟᴏᴡ 🎶</b>\n\n<b>•── ⋅ ⋅ ⋅ ───────── ⋅ • ⋅ ───────── ⋅ ⋅ ⋅ ──•</b>\n\n<b>๏ ᴘʟᴀʏ ғʀᴏᴍ :</b> <b>ʏᴏᴜᴛᴜʙᴇ • ꜱᴘᴏᴛɪꜰʏ • ʀᴇꜱꜱᴏ • ᴀᴘᴘʟᴇ • ꜱᴀᴀᴠɴ</b>\n\n<b>๏ ꜰᴇᴀᴛᴜʀᴇꜱ :</b> <b>ᴢᴇʀᴏ ᴅᴏᴡɴᴛɪᴍᴇ • ʜᴅ ᴀᴜᴅɪᴏ • ᴠᴄ ꜱᴜᴘᴘᴏʀᴛ</b>\n\n<b>•── ⋅ ⋅ ⋅ ───────── ⋅ • ⋅ ───────── ⋅ ⋅ ⋅ ──•</b>\n\n<b>๏ ᴛᴀᴘ <a href=\"https://t.me/BlushMusicbot?start=help\">ʜᴇʟᴘ</a> ᴛᴏ ᴠɪᴇᴡ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴍᴏᴅᴜʟᴇs.</b>"

]

# ── Runtime structures ─────────────────────────────────────────────────────────
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ── Minimal validation ─────────────────────────────────────────────────────────
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")

if not COOKIE_URL:
    raise SystemExit("[ERROR] - COOKIE_URL is required.")

# Only allow these cookie link formats
if not re.match(r"^https://(batbin\.me|pastebin\.com)/[A-Za-z0-9]+$", COOKIE_URL):
    raise SystemExit("[ERROR] - Invalid COOKIE_URL. Use https://batbin.me/<id> or https://pastebin.com/<id>")
