import sys
import socket
import formato

def check_client_port() -> int:
    port: int
    try:
        port = int(sys.argv[1])
    except IndexError as e:
        print(e)
        print("""No ingresaste ningun valor al iniciar,
              Se asignara: 9000""")
        port = 9_000
    except ValueError as e:
        print(e)
        print("""Ingresaste texto,
              Se asignara: 9000""")
        port = 9_000
    return port
    
def management_sms(client_socket: socket.socket) -> None:

    COLORS = {
        "RED": "\033[31m",
        "RESET": "\033[0m"
    }

    my_format = formato.Formato("*")

    while True:
        sms_from_server: str = client_socket.recv(1024).decode("utf-8")
        my_format.show_message(f"Server -> {sms_from_server}")

        client_sms: str = input(f"{COLORS['RED']}('end' to finish)-> {COLORS['RESET']}")

        if client_sms == "end":
            client_socket.send(client_sms.encode("utf-8"))
            client_socket.close()
            print(f"Client Socket is Closed")
            break

        client_socket.send(client_sms.encode("utf-8"))

def main() -> None:

    NAME_OF_COMPUTER: str = socket.getfqdn()
    IP: str = socket.gethostbyname(NAME_OF_COMPUTER)
    CLIENT_PORT: int =  check_client_port()
    SERVER_PORT: int = 8_000

    client_socket: socket.socket = socket.socket()

    client_socket.bind((IP, CLIENT_PORT))
    client_socket.connect((IP, SERVER_PORT))

    management_sms(client_socket)

if __name__ == "__main__":
    main()