import pyautogui
from PIL import Image
import threading
import NDIlib as ndi  # Use the NDI SDK for Python

# Create a threading event to control the loop
stop_event = threading.Event()

def start_ndi_stream():
    if not ndi.initialize():
        print("Cannot run NDI.")
        return

    sender = ndi.send_create()
    if not sender:
        print("Cannot create NDI sender.")
        return

    video_frame = ndi.VideoFrameV2()

    while not stop_event.is_set():
        screen = pyautogui.screenshot()
        screen = screen.resize((1920, 1080), Image.LANCZOS)
        video_frame.data = screen.tobytes()
        video_frame.line_stride_in_bytes = screen.width * 3
        video_frame.xres = screen.width
        video_frame.yres = screen.height

        ndi.send_send_video_v2(sender, video_frame)

    # Clean up NDI resources
    ndi.send_destroy(sender)
    ndi.destroy()

def stop_ndi_stream():
    # Set the event to stop the NDI streaming loop
    stop_event.set()