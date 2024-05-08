# socket is used for creating network connections
import socket
# threading is used for creating multiple threads for concurrent scanning
import threading


# Define the functions
# This function takes the IP address and port number and attempts to etsablish a TCP connection
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

# This function takes the IP, Start Port, and End Port and iterates through the range of ports numbers specified
def scan_range(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()

# Defines the main function
def main():
    ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the start port number: "))
    end_port = int(input("Enter the end port number: "))
    scan_range(ip, start_port, end_port)

# Call the main function
if __name__ == "__main__":
    main()