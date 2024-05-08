# socket is used for creating network connections
import socket
# threading is used for creating multiple threads for concurrent scanning
import threading


# Define the functions
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} on {ip} is open")
        sock.close()
    except Exception as e:
        print(f"Error while scanning port {port} on {ip}: {e}")

def scan_range(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()