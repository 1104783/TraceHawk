import os
import http.server
import socketserver
import threading
import requests
from urllib.parse import urlparse
from time import sleep

# Define the HTTP request handler
class IPLoggerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Get real IP from X-Forwarded-For header (set by Ngrok)
        forwarded_ip = self.headers.get('X-Forwarded-For')
        if forwarded_ip:
            visitor_ip = forwarded_ip.split(',')[0].strip()
        else:
            visitor_ip = self.client_address[0]

        print(f"\n[+] Visitor IP: {visitor_ip}")

        try:
            # Query IP geolocation
            res = requests.get(f"http://ip-api.com/json/{visitor_ip}").json()
            print(res)
        except Exception as e:
            print(f"[!] Failed to get IP info: {e}")

        # Respond to visitor
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>Thanks! Your IP has been logged.</h1>")

def start_server():
    with socketserver.TCPServer(("localhost", 8000), IPLoggerHandler) as httpd:
        print("[+] Server running on http://localhost:8000")
        httpd.serve_forever()

def start_ngrok(authtoken):
    os.system("pkill ngrok")
    os.system(f"ngrok config add-authtoken {authtoken}")
    os.system("ngrok http 8000 > /dev/null &")
    sleep(2)
    try:
        tunnel_info = requests.get("http://127.0.0.1:4040/api/tunnels").json()
        public_url = tunnel_info["tunnels"][0]["public_url"]
        print(f"[+] Share this link: {public_url}")
    except Exception as e:
        print(f"[!] Ngrok failed: {e}")

def main():
    print("=== Python IP Logger with Ngrok ===")
    authtoken = input("[?] Enter your Ngrok authtoken: ").strip()
    if not authtoken:
        print("[!] Authtoken is required. Exiting.")
        return

    choice = input("[?] Generate tracking link? (Y/N): ").strip().lower()
    if choice != 'y':
        print("[!] Exiting.")
        return

    start_ngrok(authtoken)

    try:
        server_thread = threading.Thread(target=start_server)
        server_thread.daemon = True
        server_thread.start()
        print("[!] Press CTRL+C to stop...")
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Server stopped.")

if __name__ == "__main__":
    main()
