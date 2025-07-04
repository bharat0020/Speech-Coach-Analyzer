
# 🎙️ Speech Coach Analyzer

The **Speech Coach Analyzer** is a Python-based tool that analyzes recorded or uploaded speech. It extracts the spoken text and evaluates tone, pause ratio, fluency score, and confidence level. This tool is useful for speech evaluation, interview feedback, communication training, and more.

---

## 📌 Features

- 🎤 Microphone input for live speech recording
- 📁 Upload `.wav` files for analysis
- ✍️ Automatic speech transcription
- 🧠 Tone detection (e.g., Neutral, Happy, Angry)
- ⏸️ Pause ratio and fluency scoring
- 📊 Confidence level of analysis
- 📝 Generates a text report of the results

---

## 📁 Project Structure

```
speech_tone_analyzer/
├── app.py                  # Main script to run the analyzer
├── requirements.txt        # Required Python packages
├── utils/
│   └── mic_input.py
│   └── audio_utils.py        # Microphone input handler
├── output/
│   └── analysis_report.txt # Result log file
└── README.md               # Project overview and documentation
```

---

## ⚙️ Installation

### Prerequisites

Ensure Python 3.7+ is installed on your system. You can install dependencies using:

```bash
pip install -r requirements.txt
```

Or manually install core packages:

```bash
pip install speechrecognition numpy scipy pyaudio
```

> If `pyaudio` fails to install, use:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## 🚀 Usage

### 🎤 Record from Microphone

1. Run the script:

```bash
python app.py
```

2. Speak clearly into your microphone.

3. Output will be saved in `output/analysis_report.txt`.

---

### 📂 Analyze a `.wav` File

1. Replace or modify the filename in `app.py`:

```python
filename = "your_audio_file.wav"
```

2. Then run:

```bash
python app.py
```

---

## 📊 Sample Output

```
📝 Transcription:
Hello, how are you doing today?

Detected Tone         : Neutral
Pause Ratio           : 0.16
Fluency Score         : 9/10
Confidence Level      : 92%
```

---

## 🙋‍♂️ Author

- **Bharat Mittal** AND **Lalatendu Biswal**
- Email: [04mittalb@gmail.com][lalatendu118@gmail.com](mailto:yourname@example.com)
- GitHub: [github.com/bharat0020][github.com/Lalatendu2004Biswal](https://github.com/your-username)

---

## 📝 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.
