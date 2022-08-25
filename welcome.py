"""
This function saves a welcome message.
"""

import json
import pyfiglet


def welcome():
    message = "Welcome to Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    print(pyfiglet.figlet_format("Test workflow"))

    with open("welcome.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact