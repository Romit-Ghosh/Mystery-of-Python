# For windows
import pyttsx3

names = [
  'Romit','cdint','messi','ronaldo',
  ]

engine = pyttsx3.init()
for name in names:
    engine.say(f"Shoutout to {name}")

engine.runAndWait()

