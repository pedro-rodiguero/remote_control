import http.server
import socketserver
import qrcode  # type: ignore
import pyautogui  # type: ignore
import socket
from urllib.parse import urlparse, parse_qs

PORT = 5000


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/next":
            pyautogui.press("right")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Next slide")
        elif parsed_path.path == "/prev":
            pyautogui.press("left")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Previous slide")
        elif parsed_path.path == "/qrcode":
            ip = self.get_local_ip()
            url = f"http://{ip}:{PORT}"
            qr = qrcode.make(url)
            qr.save("qrcode.png")
            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.end_headers()
            with open("qrcode.png", "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("10.254.254.254", 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = "127.0.0.1"
        finally:
            s.close()
        return ip


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
