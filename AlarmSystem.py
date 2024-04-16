from gtts import gTTS # type: ignore
import os

def trigger_alarm(volume=50):
    alarm_message = "Warning! Smoke is detected. Please evacuate immediately"
    tts = gTTS(text=alarm_message, lang='en')
    tts.save("alarm.mp3")
    os.system(f"afplay -v {volume} alarm.mp3")

trigger_alarm(volume=35)



    