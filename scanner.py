import socket
import concurrent.futures
from datetime import datetime

TARGET     = input("Enter target IP or hostname: ").strip()
START_PORT = 1
END_PORT   = 1024
TIMEOUT    = 0.5   
THREADS    = 100   


SERVICES = {
    21: "FTP",        22: "SSH",        23: "Telnet",
    25: "SMTP",       53: "DNS",        80: "HTTP",
   110: "POP3",      143: "IMAP",      443: "HTTPS",
   445: "SMB",      3306: "MySQL",    3389: "RDP",
  5432: "PostgreSQL", 8080: "HTTP-alt",
}

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)

    result = sock.connect_ex((ip, port))  
    sock.close()

    is_open = (result == 0)
    return port, is_open

def main():

    try:
        ip = socket.gethostbyname(TARGET)
    except socket.gaierror:
        print(f"[!] Could not resolve '{TARGET}'")
        return

    open_ports = []
    all_ports  = range(START_PORT, END_PORT + 1)

    print(f"\n[*] Target  : {TARGET} ({ip})")
    print(f"[*] Ports   : {START_PORT} – {END_PORT}")
    print(f"[*] Started : {datetime.now().strftime('%H:%M:%S')}\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as pool:

        jobs = {}
        for port in all_ports:
            future = pool.submit(scan_port, ip, port)
            jobs[future] = port

        for finished_job in concurrent.futures.as_completed(jobs):
            port, is_open = finished_job.result()

            if is_open:
                service = SERVICES.get(port, "unknown")
                print(f"  [+] Port {port:>5}/tcp  OPEN  —  {service}")
                open_ports.append(port)

    open_ports.sort()
    print(f"\n[*] Scan complete — {len(open_ports)} open port(s) found")

    if open_ports:
        print(f"[*] Open ports: {', '.join(str(p) for p in open_ports)}")

if __name__ == "__main__":
    main()