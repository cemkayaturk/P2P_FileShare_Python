import socket
import timeimport json
import os


UDP_IP_ADDRESS = # for example 192.255.255.255
UDP_PORT_NO = 5000
username = input("Enter Your Username: ")


def Message():
    message = {"username": username, "files":()}
    path = #\P2P_File_Sharing_App\files"
    dirs = os.listdir(path)
    message.update({"files":dirs})
    return message

print("Sharing your library...")
print(Message())

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    json_Message = json.dumps(Message())
    clientSock.sendto(bytes(json_Message,'utf-8'), (UDP_IP_ADDRESS, UDP_PORT_NO))
    time.sleep(15)
