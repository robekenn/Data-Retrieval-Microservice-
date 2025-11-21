import zmq
import json
import time

context = zmq.Context()

#  Socket to talk to server
print("Connecting to Data Retrieval Microservice Server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print("\n" + "="*60)
print("MICROSERVICE TEST CLIENT")
print("="*60 + "\n")

# ========================================
# TEST 1: PUSH USER DATA (Add New User)
# ========================================
print("\n--- TEST 1: PUSH USER DATA (Add New User) ---")
user_data = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "age": 28
}
request = [2, "user_004", user_data]
serialized_request = json.dumps(request).encode('utf-8')

print(f"Sending request: {request}")
socket.send(serialized_request)

response = socket.recv()
print(f"Response: {response.decode('utf-8')}")
print("Test 1 Complete\n")

time.sleep(0.5)  # Small delay between requests

# ========================================
# TEST 2: RETRIEVE USER DATA
# ========================================
print("\n--- TEST 2: RETRIEVE USER DATA ---")
# Create new socket for new request
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = [1, "user_004"]
serialized_request = json.dumps(request).encode('utf-8')

print(f"Sending request: {request}")
socket.send(serialized_request)

response = socket.recv()
retrieved_data = json.loads(response)
print(f"Retrieved user data: {json.dumps(retrieved_data, indent=2)}")
print("Test 2 Complete\n")

time.sleep(0.5)

# ========================================
# TEST 3: PUSH USER DATA (Update Existing User)
# ========================================
print("\n--- TEST 3: PUSH USER DATA (Update Existing User) ---")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

updated_user_data = {
    "name": "Alice Johnson-Smith",
    "email": "alice.smith@example.com",
    "age": 29,
    "city": "Portland"
}
request = [2, "user_004", updated_user_data]
serialized_request = json.dumps(request).encode('utf-8')

print(f"Sending request: {request}")
socket.send(serialized_request)

response = socket.recv()
print(f"Response: {response.decode('utf-8')}")
print("Test 3 Complete\n")

time.sleep(0.5)

# ========================================
# TEST 4: RETRIEVE UPDATED USER DATA
# ========================================
print("\n--- TEST 4: RETRIEVE UPDATED USER DATA ---")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = [1, "user_004"]
serialized_request = json.dumps(request).encode('utf-8')

print(f"Sending request: {request}")
socket.send(serialized_request)

response = socket.recv()
retrieved_data = json.loads(response)
print(f"Retrieved updated user data: {json.dumps(retrieved_data, indent=2)}")
print("Test 4 Complete\n")

time.sleep(0.5)

# ========================================
# TEST 5: DELETE USER
# ========================================
print("\n--- TEST 5: DELETE USER ---")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = [3, "user_001"]
serialized_request = json.dumps(request).encode('utf-8')

print(f"Sending request: {request}")
socket.send(serialized_request)

response = socket.recv()
print(f"Response: {response.decode('utf-8')}")
print("Test 5 Complete\n")

time.sleep(0.5)

# ========================================
# TEST 6: RETRIEVE NON-EXISTENT USER
# ========================================
print("\n--- TEST 6: RETRIEVE NON-EXISTENT USER ---")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = [1, "user_999"]
serialized_request = json.dumps(request).encode('utf-8')

print(f"Sending request: {request}")
socket.send(serialized_request)

response = socket.recv()
retrieved_data = json.loads(response)
print(f"Response: {json.dumps(retrieved_data, indent=2)}")
print("Test 6 Complete\n")

time.sleep(0.5)

# ========================================
# TEST 7: DELETE NON-EXISTENT USER
# ========================================
print("\n--- TEST 7: DELETE NON-EXISTENT USER ---")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = [3, "user_999"]
serialized_request = json.dumps(request).encode('utf-8')

print(f"Sending request: {request}")
socket.send(serialized_request)

response = socket.recv()
print(f"Response: {response.decode('utf-8')}")
print("Test 7 Complete\n")

print("\n" + "="*60)
print("ALL TESTS COMPLETED")
print("="*60 + "\n")  
