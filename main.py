from src.startup import Startup
print("Starting up...")
try:
    Startup.run()
except Exception as e:
    # print(e) # remove for prod
    message = type(e).__name__ + ": "+e.args[0]
    print(message)

input("Press any key to exit")
