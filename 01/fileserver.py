import socket
import os


def receive(conn):
    data = conn.recv(1024)
    if not data:
        return data
    return data.decode().strip()


def send(conn, message):
    data = (message+"\r\n").encode()
    conn.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(("localhost", 8000))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            message = receive(conn)
            if not message or message == "die":
                break

            if message == "get":
                send(conn, "What file do you want?")
                fname = receive(conn)

                if os.path.exists(fname):
                    file_contents = open(fname).read()
                    send(conn, file_contents)
                else:
                    send(conn, "No such file")

                continue

            return_message = f"Hi there stranger {addr}, let me repeat that: {message}\r\n"
            send(conn, return_message)
