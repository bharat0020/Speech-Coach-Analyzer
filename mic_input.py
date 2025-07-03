import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np

def record_audio(filename, duration=5, samplerate=44100):
    print("🔴 Recording...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')  # ✔️ save as Int16 PCM
    sd.wait()
    wav.write(filename, samplerate, recording)  # ✔️ No conversion needed now
    print(f"✔️ Saved recording to {filename}")
