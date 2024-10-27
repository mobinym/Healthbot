import speech_recognition as sr
from pydub import AudioSegment

# Function to convert audio to WAV format if necessary
def convert_audio_to_wav(file_path):
    audio = AudioSegment.from_file(file_path)  # Load the audio file
    wav_file_path = "converted_audio.wav"
    audio.export(wav_file_path, format="wav")  # Convert to WAV format
    return wav_file_path

# Load your audio file (replace 'your_audio_file' with the actual file path)
file_path = r"C:\Users\yagho\OneDrive\Desktop\New folder\Darvishi_Project\17300143351568ua0pgib-voicemaker.in-speech.wav"  # Path to your audio file
wav_file_path = convert_audio_to_wav(file_path)

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the audio file for recognition
with sr.AudioFile(wav_file_path) as source:
    audio_data = recognizer.record(source)  # Read the entire audio file

# Function to recognize speech in multiple languages
def recognize_speech(audio_data):
    languages = ['en-US', 'ar-SA']  # List of languages to try
    transcriptions = {}  # Dictionary to hold transcriptions by language

    for lang in languages:
        try:
            transcription = recognizer.recognize_google(audio_data, language=lang)
            transcriptions[lang] = transcription  # Store transcription by language
            print(f"Transcription in {lang}: {transcription}")
        except sr.UnknownValueError:
            print(f"Could not understand the audio in {lang}.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            break  # Exit if there's a request error

    return transcriptions  # Return all transcriptions

# Attempt to recognize speech in both languages
transcriptions = recognize_speech(audio_data)

# Determine the most likely transcription based on content and length
if 'en-US' in transcriptions and 'ar-SA' in transcriptions:
    english_transcription = transcriptions['en-US']
    arabic_transcription = transcriptions['ar-SA']
    
    # Check lengths to determine which transcription to consider
    if len(arabic_transcription) > len(english_transcription) * 1.5:  # Arabic is significantly longer
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

# Output the final result
print(f"Detected language: {language}")
print(f"Final Transcription: {transcription}")

#--------------------------------open chrome---------------------------------------
import subprocess
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def check_and_open_chrome(transcription):
    # Check if specific keywords are in the transcription
    if "chrome" in transcription.lower() or "open" in transcription.lower():
        # Open Google Chrome
        try:
            subprocess.Popen("start chrome", shell=True)
            output_text = "Google Chrome has been opened."
            print(output_text)
            speak(output_text)  # Use the TTS engine to speak the text
        except Exception as e:
            error_message = f"Failed to open Google Chrome: {e}"
            print(error_message)
            speak(error_message)
    else:
        no_keywords_message = "No keywords found to open Google Chrome."
        print(no_keywords_message)
        speak(no_keywords_message)

check_and_open_chrome(transcription)
