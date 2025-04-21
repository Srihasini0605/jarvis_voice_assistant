import speech_recognition as sr

# List available microphones
mic_list = sr.Microphone.list_microphone_names()
if mic_list:
    print("Microphone detected:", mic_list)
else:
    print("No microphone detected.")
