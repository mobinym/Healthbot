import speech_recognition as sr
from pydub import AudioSegment

#--------------------------key-Value-for-Quary--------------------------------------------------
def extract_special_terms(transcription: str) -> str:

    keywords = ["orthopedics", "dentist", "cardiologist", "general", "brain and nerves"]
    

    for keyword in keywords:
        if keyword in transcription:
            return keyword 
    return "هیچ کلمه خاصی یافت نشد"  


#----------------------------------------------------------------------------
def convert_audio_to_wav(file_path):
    audio = AudioSegment.from_file(file_path)
    wav_file_path = "converted_audio.wav"
    audio.export(wav_file_path, format="wav")  
    return wav_file_path


file_path = r"17300143351568ua0pgib-voicemaker.in-speech.wav"  # Path to your audio file
wav_file_path = convert_audio_to_wav(file_path)


recognizer = sr.Recognizer()


with sr.AudioFile(wav_file_path) as source:
    audio_data = recognizer.record(source)  


def recognize_speech(audio_data):
    languages = ['en-US', 'ar-SA']  
    transcriptions = {}  

    for lang in languages:
        try:
            transcription = recognizer.recognize_google(audio_data, language=lang)
            transcriptions[lang] = transcription  
            print(f"Transcription in {lang}: {transcription}")
        except sr.UnknownValueError:
            print(f"Could not understand the audio in {lang}.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            break  

    return transcriptions  


transcriptions = recognize_speech(audio_data)


if 'en-US' in transcriptions and 'ar-SA' in transcriptions:
    english_transcription = transcriptions['en-US']
    arabic_transcription = transcriptions['ar-SA']
    
    if len(arabic_transcription) > len(english_transcription) * 1.5:
        transcription = arabic_transcription
        language = 'Arabic'
    else:
        transcription = english_transcription
        language = 'English'
elif 'en-US' in transcriptions:
    transcription = transcriptions['en-US']
    language = 'English'
elif 'ar-SA' in transcriptions:
    transcription = transcriptions['ar-SA']
    language = 'Arabic'
else:
    transcription = None
    language = 'None'


print(f"Detected language: {language}")
print(f"Final Transcription: {transcription}")
print(extract_special_terms(transcription))

#--------------------------------open chrome---------------------------------------
# import subprocess
# import pyttsx3
# import numpy as np


# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def check_and_open_chrome(transcription):
    
#     if "chrome" in transcription.lower() or "open" in transcription.lower():
       
#         try:
#             subprocess.Popen("start chrome", shell=True)
#             output_text = "Google Chrome has been opened."
#             print(output_text)
#             speak(output_text)  
#         except Exception as e:
#             error_message = f"Failed to open Google Chrome: {e}"
#             print(error_message)
#             speak(error_message)
#     else:
#         no_keywords_message = "No keywords found to open Google Chrome."
#         print(no_keywords_message)
#         speak(no_keywords_message)

# check_and_open_chrome(transcription)



#----------------------------Quary To DB----------------------------------------------------------
import pyodbc

server = 'MYM-DESKTOP'
database = 'Darvishi_db'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

def get_job_ids_by_title(job_title):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
    try:
        query = "SELECT JobID FROM MedicalJobs WHERE JobTitle = ?"
        cursor.execute(query, (job_title,))
        
        results = cursor.fetchall()
        job_ids = [result[0] for result in results] 
        return job_ids  

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

user_input = extract_special_terms(transcription)
job_ids = get_job_ids_by_title(user_input)

if job_ids:
    print(f"The Job IDs for '{user_input}' are: {job_ids}")
else:
    print(f"No jobs found with the title '{user_input}'.")
