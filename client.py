import socket
import threading

HOST = "localhost"  
PORT = 65416

def receiver(sock):

    while True:
        try:
            data = sock.recv(1024)
            if str(data) == "b''":
                break
            if data:
                data = data.decode("utf-8")
                print(data)
        except:
            print('An error occurred!')
            sock.close()
            break

if __name__ == '__main__':

    sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    thread = threading.Thread(target=receiver,args=(sock,))
    thread.start()

    while True:
        try:
            message = input("")
            sock.sendall(message.encode('utf-8'))
        except KeyboardInterrupt:
            sock.close()
            break

        