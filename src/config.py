from .exceptions import ChannelFileError, TokenFileError
import scrapetube


class Config:
    def getChannel(self):
        try:
            with open("./twitch-channel.txt") as channel:
                return channel.read()
        except:
            raise ChannelFileError("twitch-channel.txt not found")

    def getToken(self):
        try:
            with open("./twitch-token.txt") as token:
                return token.read()
        except:
            return "BLANK"
            #raise TokenFileError("twitch-token.txt not found")
            
    def videoID(self):
        with open("yt.txt", encoding="utf-8") as f:
            for line in f:
                channel=line
                videos=scrapetube.get_channel(channel)
                for vidoe in videos:
                    ID=(vidoe["videoId"])
                    break
                return ID


