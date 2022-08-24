"""
This function saves a welcome message.
"""

import json
import time
import requests

def welcome():
    message = "Welcome to Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    message_dict["status_code"] = r.status_code

    while True:
        time.sleep(1.0)

    with open("welcome.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact
