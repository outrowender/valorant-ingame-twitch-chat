from .endpoints import Endpoints
from emoji import demojize


class Startup:

    @staticmethod
    def run():
        endpoint = Endpoints()
        token = endpoint.getChatToken()

        cid = token["conversations"][0]["cid"]

        def formatMessage(username, message):
            response = "[ttv] " + username + ': ' + message
            return demojize(response)

        def sendMessage(val):
            username = val.split('!')[0].replace(":", "")
            message = val.split(':')[2]
            # message formatting
            printable = formatMessage(username, message)
            endpoint.postNewChatMessage(cid, printable)

        endpoint.startTwitchChat(sendMessage)
