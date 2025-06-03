import socket
import sys
import threading
from protocol import *

def listen(sock):
    while True:
        try:
            data, _ = sock.recvfrom(4096)
            msg = parse_message(data)
            mtype = msg["type"]

            if mtype == MessageType.CHAT:
                print(f"[{msg['sender']}]: {msg['message']}")
            elif mtype == MessageType.USER_STATUS:
                print("Online users:", ", ".join(msg['users']))
            elif mtype == MessageType.COMMAND:
                print("[Server]:", msg['msg'])
            elif mtype == MessageType.PRIVATE:
                print(f"[Private from {msg['sender']}]: {msg['message']}")

            print("> ", end="", flush=True)

        except Exception as e:
            print("Error receiving:", e)

def main():
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <port>")
        return

    server = (sys.argv[1], int(sys.argv[2]))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    uname = input("Username: ")
    pwd = input("Password: ")
    sock.sendto(create_message(MessageType.LOGIN, username=uname, password=pwd), server)

    threading.Thread(target=listen, args=(sock,), daemon=True).start()

    while True:
        msg = input("> ")
        if msg.startswith("/"):
            sock.sendto(create_message(MessageType.COMMAND, command=msg), server)
            if msg == "/exit":
                break
        else:
            sock.sendto(create_message(MessageType.CHAT, message=msg), server)

if __name__ == "__main__":
    main()
