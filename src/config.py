from .exceptions import ChannelFileError, TokenFileError


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
