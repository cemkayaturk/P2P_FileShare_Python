import socket
import json

listener_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
IP = socket.gethostbyname(socket.gethostname())
listener_socket.bind(("25.21.128.101",5000))
print("Listening for broadcasts...")
while True:
    data, addr = listener_socket.recvfrom(4096)
    recieved_message = data.decode()
    print("New messeage from: ")
    print(recieved_message)
    ip_address = addr[0]
    json_message = json.loads(recieved_message)
    Service_Agenda = {}
    for chunk in json_message["files"]:
        Service_Agenda.update({chunk: ip_address})
    with open('Service_Agenda.txt', 'w') as dictn:
        dictn.write(str(Service_Agenda))
    dictn.close()



