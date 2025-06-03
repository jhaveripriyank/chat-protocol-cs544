
# CS 544 Chat Protocol – Stateful UDP Messaging System

This project implements a **stateful, real-time chat protocol** over UDP as part of the **CS 544: Computer Networks** course at **Drexel University**. The system supports user authentication, public and private messaging, user tracking, and proper protocol state management using a **Deterministic Finite Automaton (DFA)**.

## Project Overview

- **Type**: UDP-based chat protocol
- **Language**: Python 3
- **Architecture**: Client-Server Model
- **Features**: Login, Real-Time Chat, `/list`, `/pm`, `/exit`, User Join/Leave Notifications
- **DFA-Driven**: Enforces stateful behavior (Idle, Authenticated, Sending, Receiving)

---

## Project Files

| File        | Description                                                |
|-------------|------------------------------------------------------------|
| `server.py` | Main UDP server handling user sessions and message routing |
| `client.py` | Command-line chat client with real-time I/O                |
| `dfa.py`    | Implements DFA-based state transition logic per client     |
| `protocol.py` | Defines structured message types (PDUs) using JSON       |
| `utils.py`  | User database and authentication logic                     |

---

