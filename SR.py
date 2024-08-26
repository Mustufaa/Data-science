import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import io

def play_audio(audio_file):
    # Play the audio file
    audio = AudioSegment.from_mp3(audio_file)
    play(audio)

def main():
    st.title("Speech Recognition System")

    st.write("## Live Speech Convertor")
    st.write("1. Click the button to record your speech.")
    st.write("2. The system will convert your speech to text and display it.")

    recognizer = sr.Recognizer()

    # Record and display audio
    if st.button("Start Recording"):
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)
            st.write("Processing...")

        # Save the audio file
        audio_file = io.BytesIO()
        with open("temp.wav", "wb") as f:
            f.write(audio.get_wav_data())
        
        st.audio("temp.wav", format="audio/wav")

        try:
            # Use pocketsphinx for offline recognition
            text = recognizer.recognize_sphinx(audio)
            st.write(f"**Transcription:** {text}")

            # Optionally, you can play a greeting or other audio file here
            # play_audio("greeting.mp3") # Uncomment if you have a greeting.mp3 file

        except sr.UnknownValueError:
            st.write("Sorry, could not understand the audio.")
        except sr.RequestError:
            st.write("Sorry, there was an issue with the request.")
    
    st.write("## Audio Files")
    # Upload and display a saved audio file if needed
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
    
    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav/mp3')
        # Optionally, process the uploaded file
        with sr.AudioFile(uploaded_file) as source:
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_sphinx(audio)
                st.write(f"**Transcription:** {text}")
            except sr.UnknownValueError:
                st.write("Sorry, could not understand the audio.")
            except sr.RequestError:
                st.write("Sorry, there was an issue with the request.")

if __name__ == "__main__":
    main()
