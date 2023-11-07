import pyttsx3
import ctypes
import time

REPEAT_INTERVAL = 3600
while True:
    engine = pyttsx3.init()
    engine.say("Hey Romit, drink water")
    engine.runAndWait()
    ctypes.windll.user32.MessageBoxW(0, "Hey Romit, drink water", "Alert", 10)

    time.sleep(REPEAT_INTERVAL)
