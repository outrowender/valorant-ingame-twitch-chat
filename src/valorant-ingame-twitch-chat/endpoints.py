import requests
from exceptions import ValorantAPIError
from auth import Auth
import urllib3
import socket


class Endpoints:

    def __init__(self) -> None:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        auth = Auth()
        self.headers = auth.getHeaders()
        self.config = auth.getConfig()
        self.port = self.config["port"]

    def __gameGetRequest(self, endpoint):
        response = requests.get(
            "https://127.0.0.1:{port}{endpoint}".format(
                port=self.port, endpoint=endpoint
            ),
            headers=self.headers,
            verify=False,
        )

        # custom exceptions for http status codes
        self.__verify_status_code(response.status_code)

        try:
            r = response.json()
            return r
        except:
            raise ValorantAPIError("An error ocurred trying to get game APIs")

    def __gamePostRequest(self, endpoint, data):
        response = requests.post(
            "https://127.0.0.1:{port}{endpoint}".format(
                port=self.port, endpoint=endpoint
            ),
            headers=self.headers,
            verify=False,
            json=data,
        )

        # custom exceptions for http status codes
        self.__verify_status_code(response.status_code)

        try:
            r = response.json()
            return r
        except:
            raise ValorantAPIError("An error ocurred trying to get game APIs")

    def __verify_status_code(self, status_code):
        """Verify that the request was successful according to exceptions"""
        if status_code in [404, 401, 500]:
            raise ValorantAPIError(
                "An invalid status code returned from game APIs")

    def getChatToken(self):
        return self.__gameGetRequest("/chat/v6/conversations/ares-parties")

    def postNewChatMessage(self, cid, message):
        data = {
            "cid": cid,
            "message": message,
            "type": "system"
        }
        return self.__gamePostRequest("/chat/v6/messages", data)

    def startTwitchChat(self, callback):

        server = 'irc.chat.twitch.tv'
        port = 6667
        nickname = 'outrowender'
        token = 'oauth:u34ikeodfdhuiugs89sg94u0mzoh2l'
        channel = '#coreano'

        sock = socket.socket()

        sock.connect((server, port))
        sock.send(f"PASS {token}\n".encode('utf-8'))
        sock.send(f"NICK {nickname}\n".encode('utf-8'))
        sock.send(f"JOIN {channel}\n".encode('utf-8'))

        while True:
            resp = sock.recv(2048).decode('utf-8')
            callback(resp)
