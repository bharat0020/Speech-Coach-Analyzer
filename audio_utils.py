import librosa
import numpy as np
import speech_recognition as sr
import language_tool_python

def correct_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)
    return corrected

def transcribe_audio(path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio = recognizer.record(source)
    try:
        raw_text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        raw_text = "[Unclear speech - could not transcribe]"
    except sr.RequestError:
        raw_text = "[Error accessing transcription service]"

    # Now add pauses (this doesn't affect grammar input)
    y, sr_val = librosa.load(path)
    pauses = detect_pauses(y, sr_val)
    words = raw_text.split()
    for idx, _ in enumerate(pauses):
        if idx < len(words) - 1:
            words.insert(idx * 2 + 1, "[...]")
    marked_text = ' '.join(words)

    return marked_text, raw_text  # return both for different uses

def detect_pauses(y, sr, pause_threshold=0.4):
    energy = librosa.feature.rms(y=y)[0]
    times = librosa.times_like(energy, sr=sr)
    pause_times = []
    is_pausing = False
    start = 0

    for i, e in enumerate(energy):
        if e < 0.01:
            if not is_pausing:
                start = times[i]
                is_pausing = True
        else:
            if is_pausing:
                pause_duration = times[i] - start
                if pause_duration >= pause_threshold:
                    pause_times.append((round(start, 2), round(times[i], 2)))
                is_pausing = False
    return pause_times

def analyze_audio(path, spoken_text=""):
    y, sr = librosa.load(path)
    duration = librosa.get_duration(y=y, sr=sr)
    rms = np.mean(librosa.feature.rms(y=y))
    pitch = librosa.yin(y, fmin=50, fmax=300, sr=sr)
    pitch_std = np.std(pitch)
    zcr = librosa.feature.zero_crossing_rate(y)[0]
    speech_rate = np.mean(zcr) * sr / 100

    pause_ratio = len(detect_pauses(y, sr)) / (duration / 0.4)

    if pitch_std < 15:
        tone = "Calm"
    elif rms > 0.05:
        tone = "Energetic"
    else:
        tone = "Neutral"

    feedback = [
        f"Duration              : {round(duration, 2)} sec",
        f"Estimated Speech Rate : {round(speech_rate, 2)} WPM",
        f"Pitch Variability     : {round(pitch_std, 2)}",
        f"RMS Energy            : {round(rms, 4)}",
        f"Detected Tone         : {tone}",
        f"Pause Ratio           : {round(pause_ratio, 2)}",
        "",
        "📋 Feedback:",
    ]

    if speech_rate > 170:
        feedback.append("- Try slowing down a little for clarity.")
    elif speech_rate < 110:
        feedback.append("- Try speaking a bit faster to sound fluent.")
    else:
        feedback.append("- Good speaking pace!")

    if pitch_std < 10:
        feedback.append("- Add more pitch variation for expressiveness.")
    else:
        feedback.append("- Pitch variation is good.")

    if rms < 0.01:
        feedback.append("- Speak louder with more energy.")
    else:
        feedback.append("- Good volume and energy.")

    filler_words = ['um', 'uh', 'like', 'so', 'you know']
    detected_fillers = [w for w in filler_words if w in spoken_text.lower()]
    if detected_fillers:
        feedback.append(f"- Detected Filler Words: {detected_fillers}")
        feedback.append("- Try reducing these fillers to improve fluency.")
    else:
        feedback.append("- No filler words detected. Great fluency!")

    if pause_ratio > 0.3:
        feedback.append("- Too many pauses between words. Try to reduce gaps.")

    fluency_score = max(10 - int(pause_ratio * 10 + len(detected_fillers)), 1)
    feedback.append(f"\n💬 Fluency Score: {fluency_score}/10")

    return feedback
