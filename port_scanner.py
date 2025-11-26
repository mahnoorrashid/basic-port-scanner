import socket
from datetime import datetime

def scan_port(host: str, port: int, timeout: float = 0.5) -> None:
    """Attempt to connect to a given port on a host."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        # If result != 0 it's closed or filtered, we just ignore it.
    finally:
        s.close()


def main() -> None:
    print("=== Basic Port Scanner ===")
    print("⚠ Use this only on systems you own or have permission to scan.\n")

    target = input("Enter host to scan (e.g. 127.0.0.1): ").strip()

    try:
        start_port = int(input("Start port (e.g. 1): "))
        end_port = int(input("End port   (e.g. 1024): "))
    except ValueError:
        print("[!] Please enter valid numbers for ports.")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("[!] Invalid port range.")
        return

    print(f"\nScanning {target} from port {start_port} to {end_port}...")
    print(f"Time started: {datetime.now()}\n")

    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    print("\nScan complete.")


if __name__ == "__main__":
    main()
