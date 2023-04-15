import socket
import threading 

HOST = "localhost" 
PORT = 65416

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def handle_client(conn,IP):

    while True:
        try:
            data = conn.recv(1024) 
            
            if str(data) == "b''":
                break

            data = data.decode("utf-8")
            data = bcolors.OKGREEN + "<" + IP + "> " + bcolors.ENDC + data
            data = bytes(data,"utf-8")

            data_send(data,conn)
            
        except:
            clients.remove(conn)
            conn.close()
            break

def data_send(data,conn):

    for client in clients:
        if client != conn:
            client.send(data)

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen()

    clients = []

    while True:
        conn, addr = sock.accept()

        print(bcolors.OKGREEN + f"Connected by [{addr[0]}]" + bcolors.ENDC)
        clients.append(conn)

        thread = threading.Thread(target=handle_client,args=(conn,addr[0],))
        thread.start()

        

