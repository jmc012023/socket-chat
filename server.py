import socket
import formato

def management_clients(client_socket: socket.socket,
                       client_ip: str, client_port: int):
    COLORS = {
        "RED": "\033[31m",
        "RESET": "\033[0m"
    }

    my_server_format = formato.Formato("*")

    print(f"Client connected from IP: {client_ip}, Puerto: {client_port}")
    sms_to_client: str = "Bienvenido al servidor"
    client_socket.send(sms_to_client.encode("utf-8"))

    while True:
        sms_from_client: str = client_socket.recv(1024).decode("utf-8")

        if sms_from_client == "end":
            print(f"\tClient [{client_port}] -> CLOSED")
            client_socket.close()
            break
        my_server_format.show_message(f"Client [{client_port}] -> {sms_from_client}")

        sms_server: str = input(f"{COLORS['RED']}-> {COLORS['RESET']}")
        client_socket.send(sms_server.encode("utf-8"))

def management_server(server_socket: socket.socket) -> None:

    while True:
        try:
            client_socket: socket.socket
            client_address: tuple[str, int]

            client_socket, client_address = server_socket.accept()

            management_clients(client_socket, client_address[0], client_address[1])
            break

        except:
            break

def main() -> None:
    NAME_OF_COMPUTER: str = socket.getfqdn()
    IP: str = socket.gethostbyname(NAME_OF_COMPUTER)
    PORT: int = 8_000

    server_socket: socket.socket = socket.socket()
    server_socket.bind((IP, PORT))

    server_socket.listen()

    print(f"""Servidor escuchando en http://{server_socket.getsockname()[0]}
          :{server_socket.getsockname()[1]}""")
    
    management_server(server_socket)
    server_socket.close()
    print("Socket Server is Closed")

    print("END OF CHAT")

if __name__ == "__main__":
    main()