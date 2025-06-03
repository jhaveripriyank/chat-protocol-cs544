## How to Run the Project

### 1. Clone or Download


git clone https://github.com/your-username/chat-protocol-cs544.git
cd chat-protocol-cs544


> Or download and extract the ZIP.

### 2. Run the Server

In the project folder:

python server.py


### 3. Run a Client (in another terminal)

python client.py 127.0.0.1 9000


Login when prompted:
Username: alice
Password: pass123


### 4. Start More Clients

Open more terminals to simulate multiple users:
python client.py 127.0.0.1 9000

---

## Built-in User Accounts

Defined in `utils.py`:

| Username | Password |
|----------|----------|
| alice    | pass123  |
| bob      | secret   |
| steve    | nicks    |

---

## Chat Commands

| Command              | Description                                      |
|----------------------|--------------------------------------------------|
| `hello there`        | Public message to all users                      |
| `/list`              | View all online users                            |
| `/pm <user> <msg>`   | Send private message to a specific user          |
| `/exit`              | Gracefully disconnect from the server            |

---

## DFA States

Each client follows a DFA:

```
[Idle] → [Authenticated] → [Sending Message | Receiving Message | Sending Command]
```

Transitions are based on events (login, message, command, logout), ensuring stateful protocol behavior.

---

## Security

- All messages follow structured PDU formats
- Credentials are validated against a hardcoded user list
- QUIC was considered; implemented using UDP for simplicity

---

## Exit Instructions

- To exit a client: type `/exit`
- To stop the server: press `Ctrl + C`

---

## Example Output

**Client 1:**
```
Username: alice
Password: pass123
> [Server]: Login successful.
> [Server]: bob has joined the chat.
> [bob]: hey alice!
> [Private from bob]: you free?
```

**Client 2:**
```
Username: bob
Password: secret
> hello alice!
> /pm alice you free?
> /exit
```

---

## Course Info

- **Course**: CS 544 – Computer Networks
- **Instructor**: Prof. Brian Mitchell
- **University**: Drexel University
- **Term**: Spring 2025

---

## Contributors

- Priyank Jhaveri - pj365@drexel.edu
- Prapti Patel  - pp695@drexel.edu
- Darsh Solanki - ds3923@drexel.edu

---
