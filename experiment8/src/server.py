import socket

HOST = '127.0.0.1'  # Localhost address 
PORT = 65432        # Port to listen ( non sudo ports > 1023)

# using context manager type (we don't need to close the socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    """
    socket.AF_INET - For IPv4
    socket.SOCK_STREAM - For TCP protocol
    """
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)