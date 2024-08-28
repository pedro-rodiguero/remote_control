import socket
import qrcode
import os

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.254.254.254", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def generate_qr_code(url):
    qr = qrcode.make(url)
    qr_path = os.path.join(os.getcwd(), "qrcode.png")
    qr.save(qr_path)
    return qr_path