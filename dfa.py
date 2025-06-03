from enum import Enum, auto

class State(Enum):
    IDLE = auto()
    AUTHENTICATED = auto()
    SENDING_MESSAGE = auto()
    RECEIVING_MESSAGE = auto()
    SENDING_COMMAND = auto()

class DFA:
    def __init__(self):
        self.state = State.IDLE

    def transition(self, event: str):
        if self.state == State.IDLE and event == 'login_success':
            self.state = State.AUTHENTICATED
        elif self.state == State.AUTHENTICATED:
            if event == 'send_message':
                self.state = State.SENDING_MESSAGE
            elif event == 'receive_message':
                self.state = State.RECEIVING_MESSAGE
            elif event == 'send_command':
                self.state = State.SENDING_COMMAND
        elif event == 'logout':
            self.state = State.IDLE
        return self.state
