import pyttsx3

def greet_jarvis():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties (optional: adjust volume and rate if needed)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)   # Volume (0.0 to 1.0)
    
    # List available voices
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"Voice ID: {voice.id}, Name: {voice.name}")

    # Choose a voice (You can select based on the output from the above loop)
    # For example, to select a specific voice, set voice.id to the desired ID
    # engine.setProperty('voice', voices[0].id)  # Change index to select different voice

    # Optionally, set a JARVIS-like voice if available
    # Here you might need to find a suitable voice with a robotic tone

    # Speak the greeting
    greeting_text = "Hello. I am JARVIS, your virtual assistant,I will convert your speech into text."
    engine.say(greeting_text)
    
    # Wait for the speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    greet_jarvis()
