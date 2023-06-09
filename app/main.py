import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, addr = server_socket.accept() # wait for client
    while True:
        data = conn.recv(1024) # wait for client to send data
        if not data: # check if client is still connected
            break
        conn.send(b'+PONG\r\n')
    

if __name__ == "__main__":
    main()
