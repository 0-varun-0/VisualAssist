# from gtts import gTTS
# import os
# def text_to_speech(text,output_file):
#     tts = gTTS(text =text , lang ='en', slow = 'False')
#     tts.save(output_file)
#     os.system(f'start {output_file}')
# if __name__ == "__main__":
#     texxt = "Hi my name is varun"
#     output_file_name = "D:/mp3s/123.mp3"
#     text_to_speech(texxt, output_file_name)

import pyttsx3

def text_to_speech(text, output_file="output.mp3"):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty("rate", 120)
    engine.setProperty("volume", 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Save the speech as an MP3 file
    engine.save_to_file(text, output_file)

    # Wait for the speech engine to finish processing
    engine.runAndWait()

if __name__ == "__main__":
    file = open("command.txt", "r")
    text = file.read()
    output_file = "output.mp3"

    text_to_speech(text, output_file)
    print(f"Text converted to speech and saved as {output_file}")
