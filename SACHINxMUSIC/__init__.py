from SACHINxMUSIC.core.bot import RAUSHAN
from SACHINxMUSIC.core.dir import dirr
from SACHINxMUSIC.core.git import git
from SACHINxMUSIC.core.userbot import Userbot
from SACHINxMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = RAUSHAN()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
