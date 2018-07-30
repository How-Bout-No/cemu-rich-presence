from pypresence import Presence
import time
import win32gui
import re
import sys

def enumWindowsProc(hwnd, lParam):
    global gametitle
    wintitle = win32gui.GetWindowText(hwnd)
    if "Cemu" in wintitle:
        try:
            gametitle = re.findall(r'\](.*?)\[', wintitle)[2].strip()
        except:
            print("Cemu is not running!")
            sys.exit()
        
win32gui.EnumWindows(enumWindowsProc, 0)

client_id = '473587029498658846'
RPC = Presence(client_id)
RPC.connect()
image_key = 'cemulogo_png'
starttime = time.time()

print(RPC.update(state=gametitle, details="Now Playing:", start=starttime, large_image=image_key))

while True:
    win32gui.EnumWindows(enumWindowsProc, 0)
    RPC.update(state=gametitle, details="Now Playing:", start=starttime, large_image=image_key)
    time.sleep(500)
