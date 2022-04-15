from program import start
from helpers import colored

try:
    start()
except Exception as e:
    # print(e) # remove for prod
    message = type(e).__name__ + ": "+e.args[0]
    print(colored(255, 0, 0, message))
