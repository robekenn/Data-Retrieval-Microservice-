# Data-Retrieval-Microservice
This microservice uses the Zero-MQ protocal.

For this microservice please connect via:
```
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```

Requesting:
Retrieve Data: --Todo--

Push Data: --Todo--

Delete-User:
The delete-user function will be called if the server recieves a JSON object that contains a list [3 (the protocal for delete-user), userID].
You will ned to send this through the socket.send(...)
Example:
```
#request with serilization
request = [3, "user_001"]
serialized_list_json = json.dumps(siReq).encode('utf-8')

# send to the server
socket.send(serialized_list_json)
```


Receiveing:

Retrieve Data:--Todo--

Push Data:--Todo--

Delete-User:
The Server will return a "OK" or "ERROR". to wait for the responce call socket.recv()
```
#receive responce
message = socket.recv()
```


Team Ground Rules
1. We will use Microsoft Teams and email for quick communication, and Canvas discussions for important announcements or project updates. Please remember to turn on your notifications.
 
2. Team members should respond to messages within 72 hours , unless they’ve communicated an expected delay in advance.
 
3. If a team member becomes unresponsive for more than 24 hours from when an assignment is due the rest of the team will notify the instructor. We will not redistribute their work; instead, we will continue with our individual responsibilities and adjust our integration plan as needed.
 
4. Each teammate is responsible for completing and submitting their own microservice and main program. Everyone is accountable for their own code.
 
5. Team members are expected to actively participate in communication, meetings, and check-ins. If someone consistently (more then 2 times) does not participate or contribute, the issue will be documented and shared with the instructor.
