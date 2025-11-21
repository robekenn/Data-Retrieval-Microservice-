# Data-Retrieval-Microservice

This microservice provides three operations for managing user data:
1. **Retrieve User Data** - Get user information by ID
2. **Push User Data** - Add or update user information
3. **Delete User** - Remove a user from the database

## Communication Protocol

This microservice uses the **ZeroMQ (ZMQ)** protocol with a REQ-REP pattern on port 5555.

### Setup Connection

```python
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```

---

## 1. Retrieve User Data

### How to REQUEST Data

Send a JSON-encoded list with:
- **Position 0**: Operation code `1` (for retrieve)
- **Position 1**: User ID (string)

**Example Call:**
```python
import zmq
import json

# Create request
request = [1, "user_001"]
serialized_request = json.dumps(request).encode('utf-8')

# Send to server
socket.send(serialized_request)
```

### How to RECEIVE Data

The server responds with a JSON object containing:
- User data (if found): `{"id": "user_001", "name": "...", "email": "...", ...}`
- Error message (if not found): `{"error": "User not found"}`

**Example Call:**
```python
# Receive response
response = socket.recv()
user_data = json.loads(response)
print(user_data)
```

**Example Output (Success):**
```json
{
  "id": "user_001",
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30
}
```

**Example Output (User Not Found):**
```json
{
  "error": "User not found"
}
```

---

## 2. Push User Data

### How to REQUEST Data

Send a JSON-encoded list with:
- **Position 0**: Operation code `2` (for push)
- **Position 1**: User ID (string)
- **Position 2**: User data dictionary (can include name, email, age, etc.)

**Example Call:**
```python
import zmq
import json

# Create request with user data
user_data = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "age": 28
}
request = [2, "user_004", user_data]
serialized_request = json.dumps(request).encode('utf-8')

# Send to server
socket.send(serialized_request)
```

### How to RECEIVE Data

The server responds with a string message:
- `"OK - User added"` - New user was created
- `"OK - User updated"` - Existing user was updated

**Example Call:**
```python
# Receive response
response = socket.recv()
message = response.decode('utf-8')
print(message)
```

**Example Output:**
```
OK - User added
```

---

## 3. Delete User

### How to REQUEST Data

Send a JSON-encoded list with:
- **Position 0**: Operation code `3` (for delete)
- **Position 1**: User ID (string)

**Example Call:**
```python
import zmq
import json

# Create request
request = [3, "user_001"]
serialized_request = json.dumps(request).encode('utf-8')

# Send to server
socket.send(serialized_request)
```

### How to RECEIVE Data

The server responds with a string message:
- `"OK"` - User was successfully deleted
- `"ERROR NO USERS DELETED"` - User ID not found

**Example Call:**
```python
# Receive response
response = socket.recv()
message = response.decode('utf-8')
print(message)
```

**Example Output:**
```
OK
```

---

## UML Sequence Diagram

```
┌─────────────┐          ┌──────────┐          ┌─────────────────┐
│ Test Client │          │   ZMQ    │          │ Microservice    │
│  Program    │          │ Socket   │          │    Server       │
└──────┬──────┘          └────┬─────┘          └────────┬────────┘
       │                      │                         │
       │  1. RETRIEVE USER    │                         │
       ├─────────────────────>│                         │
       │ [1, "user_001"]      │   forward request       │
       │                      ├────────────────────────>│
       │                      │                         │
       │                      │                    ┌────▼────────┐
       │                      │                    │retrieve_user│
       │                      │                    │  (user_id)  │
       │                      │                    └────┬────────┘
       │                      │   return user data      │
       │                      │<────────────────────────┤
       │  user JSON object    │                         │
       │<─────────────────────┤                         │
       │                      │                         │
       │                      │                         │
       │  2. PUSH USER        │                         │
       ├─────────────────────>│                         │
       │ [2, "user_004", {...}]  forward request        │
       │                      ├────────────────────────>│
       │                      │                         │
       │                      │                    ┌────▼────────┐
       │                      │                    │  push_user  │
       │                      │                    │(id, data)   │
       │                      │                    └────┬────────┘
       │                      │                         │
       │                      │                    ┌────▼────────┐
       │                      │                    │   JDump()   │
       │                      │                    │ (save JSON) │
       │                      │                    └────┬────────┘
       │                      │   return "OK"           │
       │                      │<────────────────────────┤
       │  "OK - User added"   │                         │
       │<─────────────────────┤                         │
       │                      │                         │
       │                      │                         │
       │  3. DELETE USER      │                         │
       ├─────────────────────>│                         │
       │ [3, "user_001"]      │   forward request       │
       │                      ├────────────────────────>│
       │                      │                         │
       │                      │                    ┌────▼────────┐
       │                      │                    │ delete_user │
       │                      │                    │  (user_id)  │
       │                      │                    └────┬────────┘
       │                      │                         │
       │                      │                    ┌────▼────────┐
       │                      │                    │   JDump()   │
       │                      │                    │ (save JSON) │
       │                      │                    └────┬────────┘
       │                      │   return "OK"           │
       │                      │<────────────────────────┤
       │  "OK"                │                         │
       │<─────────────────────┤                         │
       │                      │                         │
```

### Key Notes:
- The test client never calls the microservice functions directly
- All communication goes through ZMQ sockets
- Each request follows the REQ-REP pattern (one request, one reply)
- Operation codes: 1=Retrieve, 2=Push, 3=Delete
- Data is persisted to `data.json` after Push and Delete operations

---

## Running the Microservice

### Start the Server:
```bash
python Server.py
```

### Run the Test Client:
```bash
python testClient.py
```

---

## Team Contributions

### Microservice 3:

**Kaedin:** Completed the Push User and Retrieve User microservice. Created the final README file and recorded a video demo.

**Kenneth:** Completed delete user microservice. Started initial draft of the README file.

---

## Team Ground Rules
1. We will use Microsoft Teams and email for quick communication, and Canvas discussions for important announcements or project updates. Please remember to turn on your notifications.
 
2. Team members should respond to messages within 72 hours , unless they’ve communicated an expected delay in advance.
 
3. If a team member becomes unresponsive for more than 24 hours from when an assignment is due the rest of the team will notify the instructor. We will not redistribute their work; instead, we will continue with our individual responsibilities and adjust our integration plan as needed.
 
4. Each teammate is responsible for completing and submitting their own microservice and main program. Everyone is accountable for their own code.
 
5. Team members are expected to actively participate in communication, meetings, and check-ins. If someone consistently (more then 2 times) does not participate or contribute, the issue will be documented and shared with the instructor.
