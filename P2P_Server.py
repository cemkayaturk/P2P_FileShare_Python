import os
import math
import socket
import datetime

source = #
destination = #

content_name = input("Enter the name of the file you want to serve: ")
filename = content_name+'.png'
c = os.path.getsize(filename)
CHUNK_SIZE = math.ceil(math.ceil(c)/5)

index = 1
with open(filename, 'rb') as infile:
    chunk = infile.read(int(CHUNK_SIZE))
    os.chdir(destination)
    while chunk:
        chunkname = content_name+'_'+str(index)
        with open(chunkname, 'wb+') as chunk_file:
            chunk_file.write(chunk)
        index += 1
        chunk = infile.read(int(CHUNK_SIZE))
chunk_file.close()

print("Files are ready to serve!")

SERVER_HOST = "25.21.128.101"
SERVER_PORT = 5001
BUFFER_SIZE = 4096

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST,SERVER_PORT))

while True:
    server_socket.listen(5)

    print(f"[+]Listening as {SERVER_HOST}:{SERVER_PORT}")
    client_socket, address = server_socket.accept()
    print(f"[-] {address} is connected.")



    chunk_file_name = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    filesize = os.path.getsize(chunk_file_name)
    client_socket.send(str(filesize).encode('utf-8'))

    progress = range(filesize)
    with open(chunk_file_name, "rb+") as f:
        print(f"Sending {chunk_file_name} to {address}...")
        for _ in progress:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)
        print(f"{chunk_file_name} sent to {address}!")
    os.chdir(source)
    with open("Server_log.txt",'a') as log:
        log.write(f"{chunk_file_name} sent to {address} at {datetime.datetime.now()}!\n")
    os.chdir(destination)
    client_socket.close()

server_socket.close()
