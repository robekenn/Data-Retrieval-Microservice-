import DeleteUser
import PushUser
import RetrieveUser
import zmq
import json

def JDump(data):
    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)

#initilises the socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#read JSON Database's data
with open('data.json', 'r') as file:
        data = json.load(file)



while True:
    #  Wait for next request from client
    message = socket.recv()

    #changes the recieved JSON to normal data
    message = json.loads(message)
    print(message)

    if message[0] == 1:
          # retrieve data
          print("retrieve Data")
          retMessage = RetrieveUser.retrieve_user(message[1], data)
          retMessage_json = json.dumps(retMessage).encode('utf-8')
          socket.send(retMessage_json)
    elif message[0] == 2:
          # Push Data
          print("Push Data")
          retMessage = PushUser.push_user(message[1], message[2], data)
          socket.send_string(retMessage)
          # Save updated data to JSON file
          JDump(data)
    elif message[0] == 3:
          # Delete User
          print("delete User")
          retMessage = DeleteUser.delete_user(message[1], data)
          socket.send_string(retMessage)
          # Save updated data to JSON file
          JDump(data)

