# 🦅 TraceHawk IP Address Tracker and Logger by ARCHKHERT

---

## 📌 Introduction

TraceHawk IP Address Tracker and Logger by ARCHKHERT is a powerful Python-based tool designed for tracking and logging IP addresses in real time. It spins up a local HTTP server and uses Ngrok to expose the server over the internet, allowing anyone who clicks the link to be tracked instantly.

Perfect for ethical hacking, penetration testing, network monitoring, and education, TraceHawk provides geolocation data and prints the target's IP address as soon as the page is accessed.

---

## 🚀 Features

- 🔗 Automatically generates Ngrok public URL for tracking
- 🌐 Logs IPs from incoming HTTP requests
- 📍 Retrieves detailed geolocation using ip-api.com
- 💻 Lightweight, portable, and command-line friendly
- 🔐 Authtoken prompt for secure Ngrok integration
- 🧵 Multi-threaded server for stable request handling
- 📦 Works on Arch Linux, Termux, and non-root Android setups (via Pyroid3)

---

## 🛠️ Installation Guide

> 📂 Follow these steps to install and run TraceHawk on Arch Linux (or any Linux distro).

---

### 🔽 1. Clone the Repository

```git clone https://github.com/archkhertdev/TraceHawk.git```


---

### 🧪 2. Create a Virtual Environment (Recommended)

```python -m venv venv```
```source venv/bin/activate```


---

### 📦 3. Install Required Python Packages

```pip install requests``` (Do this inside venv)


---

### ⚙️ 4. Install Ngrok (If not installed)

```sudo pacman -S unzip curl -O https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip unzip ngrok-stable-linux-amd64.zip```

```sudo mv ngrok /usr/local/bin```

(If you're having problems installing ngrok, watch some tutorials on YT or ask AI)


---

### 🚀 Usage Instructions

▶️ Run the IP Logger

python ip_logger.py

1. Enter your Ngrok authtoken when prompted. **(NOTE: You must create an account on ngrok and use your own API. IT IS FREE)**


2. The tool will generate a public tracking link.


3. Send the link to your target (with permission).


4. When they open it, their IP + geolocation will be printed instantly.

5. Press CTRL+C to end the program and type ```pkill ngrok``` so you can use your API again




---

### 📁 Example Output

=== Python IP Logger with Ngrok ===
[?] Enter your Ngrok authtoken: <paste-it-here>
[+] Share this link: https://abc123.ngrok.io

[+] Visitor IP: 203.0.113.42
{
  'query': '203.0.113.42',
  'country': 'United States',
  'regionName': 'California',
  'city': 'Los Angeles',
  'isp': 'ExampleISP',
  ...
}


---

### ⚠️ Legal & Ethical Usage

This tool is provided for educational and authorized testing purposes only.
Do not use it against individuals, websites, or networks without explicit permission.
Using this tool on unauthorized targets may violate local laws and cybersecurity regulations.


---

### 👤 Author

Khert (ARCHKHERT)
Ethical Hacker | Security Researcher | Arch Linux Enthusiast
🔗 GitHub: https://github.com/your-username


---

> “Hacking isn’t about breaking systems. It’s about breaking boundaries — ethically.”
— ARCHKHERT 🧠💻
