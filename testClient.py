import zmq
import json

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")



# -- TEST Recieve Data --

#request with serilization

#siReq = [1, "user_001"]
#serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
#socket.send(serialized_list_json)

#receive responce
#message = socket.recv()
#print(message)

# -- END TEST Recieve Data -- 


# -- TEST Push Data --

#request with serilization

# -- Some sort of user data  (Please format this how you need!)--
# list = [...]


#siReq = [2, "user_002", list]
#serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
#socket.send(serialized_list_json)


#receive responce
#message = socket.recv()
#print(message)

# -- END TEST Push Data --

# -- TEST DELETE USER --

#request with serilization
siReq = [3, "user_001"]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)


#receive responce
message = socket.recv()
print(message)

# -- END TEST DELETE USER --  
