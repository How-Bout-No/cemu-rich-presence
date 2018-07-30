from pypresence import Presence
import time
import win32gui
import re
import sys

gametitle = None

def enumWindowsProc(hwnd, lParam):
    global gametitle
    wintitle = win32gui.GetWindowText(hwnd)
    if "Cemu" in wintitle:
        try:
            gametitle = re.findall(r'\](.*?)\[', wintitle)[2].strip()
        except:
            gametitle = ''

win32gui.EnumWindows(enumWindowsProc, 0)

if gametitle is None:
    print("Cemu is not running!")
    sys.exit()

client_id = '473587029498658846'
RPC = Presence(client_id)
RPC.connect()
image_key = 'cemulogo_png'
starttime = time.time()

while True:
    if gametitle == '':
        win32gui.EnumWindows(enumWindowsProc, 0)
        print("No game playing...\nChecking again in 5 seconds...\n\n")
        time.sleep(5)
    elif gametitle is None:
        print("Cemu is not running!")
        sys.exit()
    else:
        win32gui.EnumWindows(enumWindowsProc, 0)
        RPC.update(state=gametitle, details="Now Playing:", start=starttime, large_image=image_key)
        time.sleep(500)
