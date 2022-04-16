from src.startup import Startup
from src.helpers import colored

try:
    Startup.run()
except Exception as e:
    # print(e) # remove for prod
    message = type(e).__name__ + ": "+e.args[0]
    print(colored(255, 0, 0, message))
