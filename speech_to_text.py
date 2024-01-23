import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                return r.recognize_google(audio2)
                
        except sr.UnknownValueError as e:
            print(f"Unknown value error occurred: {e}")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")

while True:
    text = record_text()
    
    # Check if the recognized text is not empty
    if text:
        output_text(text)
        print(f"Recognized text: {text}")

