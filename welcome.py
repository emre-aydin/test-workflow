"""
This function saves a welcome message.
"""

import json
import numpy as np

def welcome():
    message = "Welcome to Orquestra!"

    message_dict = {}
    message_dict["message"] = message
    message_dict["schema"] = "message"

    x = np.arange(15, dtype=np.int64).reshape(3, 5)
    x[1:, ::2] = -99
    max_per_row = x.max(axis=1)
    message_dict["max_per_row"] = max_per_row

    with open("welcome.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact