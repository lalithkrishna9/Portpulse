# Network Scanner

A lightweight TCP port scanner written in Python. Scans a target host across a range of ports and identifies which ones are open, along with the service typically running on them.

---

## What It Does

- Takes a hostname or IP address as input
- Scans ports 1–1024 (configurable)
- Uses multithreading to run 100 port checks simultaneously
- Prints open ports in real time as they are found
- Shows a summary of all open ports at the end

---

## How It Works

The scanner attempts a **TCP connect** on each port. This is the most basic form of port scanning:

- If the target responds with a connection → port is **open**
- If the target refuses or doesn't respond within the timeout → port is **closed / filtered**

This is the same technique used by tools like `nmap` in its default scan mode.

---

## Requirements

- Python 3.x
- No third-party libraries — uses only the Python standard library (`socket`, `concurrent.futures`, `datetime`)

---

## Usage

```bash
python scanner.py
```

You will be prompted to enter a target:

```
Enter target IP or hostname: scanme.nmap.org
```

### Example Output

```
[*] Target  : scanme.nmap.org (45.33.32.156)
[*] Ports   : 1 – 1024
[*] Started : 14:32:10

  [+] Port    22/tcp  OPEN  —  SSH
  [+] Port    80/tcp  OPEN  —  HTTP

[*] Scan complete — 2 open port(s) found
[*] Open ports: 22, 80
```

---

## Configuration

All settings are at the top of the file and easy to change:

| Variable | Default | Description |
|---|---|---|
| `START_PORT` | `1` | First port to scan |
| `END_PORT` | `1024` | Last port to scan |
| `TIMEOUT` | `0.5` | Seconds to wait per port before giving up |
| `THREADS` | `100` | How many ports to check simultaneously |

To scan all ports, change `END_PORT` to `65535`. Note this will take longer.

---

## Legal & Ethics

> **Only scan hosts you own or have explicit permission to scan.**

Unauthorized port scanning is illegal in most countries. Use this tool only on:

- Your own machines
- Your own local network (`192.168.x.x`)
- `scanme.nmap.org` — a host provided by the nmap team specifically for practice

---

## Project Structure

```
network-scanner/
└── scanner.py      # Main script
└── README.md       # This file
```

---

## Concepts Covered

This project demonstrates the following beginner cybersecurity and networking concepts:

- **TCP/IP** — how connections are established (SYN → SYN-ACK → ACK handshake)
- **Port scanning** — identifying open services on a host
- **Sockets** — low-level network programming in Python
- **Multithreading** — running tasks concurrently to improve speed
- **Service enumeration** — mapping port numbers to known services

---

## Possible Improvements

- Add UDP scanning support
- Add banner grabbing (read what the service sends back on connect)
- Save results to a file
- Add a progress bar
- Accept port range as a command-line argument instead of hardcoding it

---

## Author

Built as a beginner cybersecurity project to learn port scanning fundamentals.
