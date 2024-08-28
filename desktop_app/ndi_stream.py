import pyautogui
import pynetworktables as ndi
from PIL import Image

def start_ndi_stream():
    # Start NDI stream
    if not ndi.initialize():
        print("Cannot run NDI.")
        return

    # Create a sender
    sender = ndi.send_create()
    if not sender:
        print("Cannot create NDI sender.")
        return

    # Create a video frame
    video_frame = ndi.VideoFrameV2()

    while True:
        # Capture the screen
        screen = pyautogui.screenshot()
        screen = screen.resize((1920, 1080), Image.LANCZOS)
        video_frame.data = screen.tobytes()
        video_frame.line_stride_in_bytes = screen.width * 3
        video_frame.xres = screen.width
        video_frame.yres = screen.height

        # Send the frame
        ndi.send_send_video_v2(sender, video_frame)