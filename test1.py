import speech_recognition as sr
import os
import webbrowser  
import numpy

record = sr.Recognizer()

print("در حال گوش کردن...")
with sr.Microphone() as source:
    record.pause_threshold = 1
    audio = record.listen(source)

print("در حال پردازش صدا...")

try:
    text = record.recognize_google(audio, language='fa-IR')
    print("\n" + text)

    commands = {
        "گوگل کروم": r"C:\Users\DELL\AppData\Local\Google\Chrome\Application\chrome.exe",
        " سوپر مارکت دیجی کالا ": "https://www.digikala.com/fresh",
        "دیجی کالا": "https://www.digikala.com",
    }

    for key, value in commands.items():
        if key in text and "باز" in text:
            if value.startswith("http"):
                webbrowser.open(value)  
            else:
                os.startfile(value)  

except sr.UnknownValueError:
    print("متاسفانه نتوانستم صدا را تشخیص دهم.")
except sr.RequestError:
    print("خطا در اتصال به سرویس شناسایی صدا.")
except Exception as e:
    print(f"یک خطا رخ داده است: {e}")
