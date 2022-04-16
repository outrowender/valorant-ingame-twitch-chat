from .endpoints import Endpoints


class Startup:

    @staticmethod
    def run():
        endpoint = Endpoints()
        token = endpoint.getChatToken()

        cid = token["conversations"][0]["cid"]

        def sendMessage(val):
            username = val.split('!')[0].replace(":", "")
            message = val.split(':')[2]
            # message formatting
            printable = "twitch@" + username + ': ' + message
            endpoint.postNewChatMessage(cid, printable)

        endpoint.startTwitchChat(sendMessage)
