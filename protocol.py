from enum import IntEnum
import json

class MessageType(IntEnum):
    LOGIN = 1
    CHAT = 2
    USER_STATUS = 3
    COMMAND = 4
    PRIVATE = 5  # Private messaging

def create_message(mtype, **kwargs):
    return json.dumps({"type": mtype, **kwargs}).encode('utf-8')

def parse_message(data):
    try:
        return json.loads(data.decode('utf-8'))
    except Exception:
        return None
