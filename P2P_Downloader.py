import socket
import os
import shutil
import json
import datetime

source = r'C:\Users\cemka\PycharmProjects\P2P_File_Sharing_App'
destination = r'C:\Users\cemka\PycharmProjects\P2P_File_Sharing_App\files'

SERVER_PORT = 5001
BUFFER_SIZE = 4096
while True:
    with open('Service_Agenda.txt','r') as agenda:
        json_ag = agenda.read()
        json_load = json_ag.replace("'", "\"")
        Service_Agenda = json.loads(json_load)
    base_file_name = input("Please Enter the Name of the File You Want to Download: ")

    index = 1
    while index!=6:

        filename = base_file_name+"_"+str(index)
        SERVER_HOST = Service_Agenda[filename]
        downloader_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        downloader_socket.connect((SERVER_HOST, SERVER_PORT))


        downloader_socket.send(bytes(filename, 'utf-8'))
        received = downloader_socket.recv(BUFFER_SIZE).decode('utf-8')
        filesize = int(received)
        filename = os.path.basename(filename)


        progress = range(filesize)
        with open(filename, "wb") as f:
            print(f"Downloading {filename} file from {SERVER_HOST}...")
            for _ in progress:

                bytes_read = downloader_socket.recv(BUFFER_SIZE)
                if not bytes_read:
                    break
                f.write(bytes_read)
        with open('Download_log.txt','a') as log:
            log.write(f"{filename} is dowloaded from {SERVER_HOST} at {datetime.datetime.now()}!\n")
            print(f"{filename} is dowloaded from {SERVER_HOST}!")

        index += 1
        downloader_socket.close()

    content_name = base_file_name
    chunknames = [content_name + '_1', content_name + '_2', content_name + '_3', content_name + '_4',
                  content_name + '_5']

    with open(content_name+'.png', 'wb') as outfile:
        for chunk in chunknames:
            with open(chunk, 'rb') as infile:
                 outfile.write(infile.read())
            shutil.move(source+"/"+chunk,destination+"/"+chunk)