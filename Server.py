import DeleteUser
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
          #retMessage = ret_data(message[1]) #sends the UserID
          #socket.send(retMessage)
    elif message[0] == 2:
          #Push Data
          print("Push Data")
          #retMessage = push_data(message[1], message[2]) #sends the userID and an list of the rest of the users data.
          #socket.send(retMessage)
    elif message[0] == 3:
          #Delete User
          print("delete User")
          retMessage = DeleteUser.delete_user(message[1], data)
          socket.send_string(retMessage)
          print(data)

