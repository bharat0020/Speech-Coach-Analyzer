import os
import time
from utils.audio_utils import analyze_audio, transcribe_audio, correct_grammar
from utils.mic_input import record_audio

os.makedirs("samples", exist_ok=True)

print("🎤 Welcome to the Speech Tone & Feedback Analyzer")
print("Choose input mode:\n1. Record from Mic\n2. Upload .wav file")

choice = input("Enter 1 or 2: ")

filename = ""
if choice == "1":
    print("Recording for 5 seconds...")
    filename = f"samples/mic_record_{int(time.time())}.wav"
    record_audio(filename, duration=5)
elif choice == "2":
    filename = input("Enter path to .wav file: ").strip()
    if not os.path.exists(filename):
        print("❌ File not found.")
        exit()
else:
    print("Invalid choice.")
    exit()

print(f"\n✅ Analyzing: {filename}")
text_with_pauses, original_text = transcribe_audio(filename)  # transcription + original
clean_text = original_text.replace("[...]", "").replace("  ", " ").strip()

feedback = analyze_audio(filename, clean_text)
corrected = correct_grammar(clean_text)

print("\n📝 Transcription:")
print(text_with_pauses)


print("\n✅ Grammar Suggestions:")
print(corrected)

print("\n🧠 Analysis Summary:")
print("-" * 40)
for line in feedback:
    print(line)

# Save report
os.makedirs("feedback_output", exist_ok=True)
report_path = f"feedback_output/feedback_{int(time.time())}.txt"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("Speech Analysis Feedback\n")
    f.write("="*40 + "\n\n")
    f.write("📝 Transcription:\n" + text_with_pauses + "\n\n")
    f.write("✅ Grammar Suggestions:\n" + corrected + "\n\n")
    f.write("🧠 Feedback:\n")
    for line in feedback:
        f.write(line + "\n")

print(f"\n📁 Feedback saved to: {report_path}")
