import speech_recognition as sr
import subprocess

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say a command...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    return ""

def handle_command(command):
    if "open calculator" in command:
        subprocess.Popen(["open", "-a", "Calculator"])
    elif "open safari" in command:
        subprocess.Popen(["open", "-a", "Safari"])
    elif "open notes" in command:
        subprocess.Popen(["open", "-a", "Notes"])
    else:
        print("Command not recognized.")

if __name__ == "__main__":
    command = recognize_speech()
    if command:
        handle_command(command)
