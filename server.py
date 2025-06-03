import socket
import threading
from protocol import *
from utils import authenticate
from dfa import DFA, State

PORT = 9000
clients = {}
user_states = {}
usernames = {}

def handle_client(addr, data, sock):
    message = parse_message(data)
    if not message: return
    mtype = MessageType(message['type'])

    if addr not in user_states:
        user_states[addr] = DFA()

    dfa = user_states[addr]

    if mtype == MessageType.LOGIN:
        uname, pwd = message["username"], message["password"]
        if authenticate(uname, pwd):
            clients[addr] = sock
            usernames[addr] = uname
            dfa.transition('login_success')
            sock.sendto(create_message(MessageType.COMMAND, msg="Login successful."), addr)

            # Notify others
            broadcast = create_message(MessageType.CHAT, sender="Server", message=f"{uname} has joined the chat.")
            for client in clients:
                if client != addr:
                    sock.sendto(broadcast, client)
        else:
            sock.sendto(create_message(MessageType.COMMAND, msg="Invalid credentials."), addr)

    elif mtype == MessageType.CHAT and dfa.state == State.AUTHENTICATED:
        dfa.transition('send_message')
        sender = usernames.get(addr, "unknown")
        msg = message['message']
        broadcast = create_message(MessageType.CHAT, sender=sender, message=msg)
        for client_addr in clients:
            sock.sendto(broadcast, client_addr)

    elif mtype == MessageType.COMMAND:
        dfa.transition('send_command')
        cmd = message['command']
        if cmd == "/list":
            user_list = list(usernames.values())
            sock.sendto(create_message(MessageType.USER_STATUS, users=user_list), addr)

        elif cmd.startswith("/pm"):
            parts = cmd.split(' ', 2)
            if len(parts) < 3:
                sock.sendto(create_message(MessageType.COMMAND, msg="Usage: /pm <user> <message>"), addr)
            else:
                target_user, pm_msg = parts[1], parts[2]
                target_addr = next((a for a, u in usernames.items() if u == target_user), None)
                if target_addr:
                    pm = create_message(MessageType.PRIVATE, sender=usernames[addr], message=pm_msg)
                    sock.sendto(pm, target_addr)
                else:
                    sock.sendto(create_message(MessageType.COMMAND, msg="User not found."), addr)

        elif cmd == "/exit":
            uname = usernames.get(addr, "Unknown")
            sock.sendto(create_message(MessageType.COMMAND, msg="Goodbye!"), addr)
            dfa.transition('logout')
            clients.pop(addr, None)
            usernames.pop(addr, None)

            # Notify others
            broadcast = create_message(MessageType.CHAT, sender="Server", message=f"{uname} has left the chat.")
            for client in clients:
                sock.sendto(broadcast, client)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", PORT))
    print(f"Server running on port {PORT}...")

    while True:
        data, addr = sock.recvfrom(4096)
        threading.Thread(target=handle_client, args=(addr, data, sock), daemon=True).start()

if __name__ == "__main__":
    main()
