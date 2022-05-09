import socket

# для тестов
msgtest={
    "method": "howLen",
    "task_id" : "1123",
    "tasks": [
        {
            "api": "weather API",
            "parameters" : {
              "time":"12/12/12"
            }
        },
        {
            "api": "COVID API",
            "parameters" : {
              "time":"11/11/11"
            }
        }
    ]
}

msgOneTest={
    "method": "getData",
    "task_id" : "1123",
    "tasks": 
        {
            "api": "weather API",
            "parameters" : {
                "start_time":"10/10/10",
                "end_time":"12/12/12",
                "location":"Vologda"
            }
        }
}
def getLength(Socket):
    length = 0
    while not length:
        length = int(Socket.recv(1024).decode())
    Socket.sendall(bytes(length))
    return length

def setLength(Socket,msg):
    Socket.sendall(bytes(len(msg)))
    length = int(Socket.recv(1024).decode())
    while not len(msg) == length:
        length = int(Socket.recv(1024).decode())

    return length
msg = [
    msgtest
]
HOST, PORT = "localhost", 50000
def getLocalExternalIP():
    # getlockal ip
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as temp_socket:
        temp_socket.connect(("8.8.8.8", 80))
        HOST = str(temp_socket.getsockname()[0])
        print("Lockal ip: {}".format(HOST))
    return HOST

for dataMsg in msg:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        #data = dataMsg 
        data=str(dataMsg).encode('utf-8')
        sock.sendall(data)
        lenght = 10240
        received = sock.recv(lenght).decode('utf-8')
        print("Sent:     {}".format(data.decode()))
        print("Received: {}".format(received))
        print("------")