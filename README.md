Here's a **detailed README file** for your **AI-Powered Media Transcription using Whisper** project:  

---

# **AI-Powered Media Transcription using Whisper**  
🚀 **Automatically Transcribe Audio & Video Files Using OpenAI’s Whisper Model**  

## **📌 Overview**  
This project leverages **OpenAI’s Whisper** model to transcribe **audio and video** files into text efficiently.  
- 🛠 **Supports Multiple Formats**: Processes **MP3, WAV, FLAC, MP4, MKV, AVI, MOV** and more.  
- 🎯 **AI-Powered Transcription**: Uses **OpenAI Whisper (tiny model)** for accurate speech-to-text conversion.  
- 🎬 **Handles Video Files**: Extracts **audio from videos** automatically before transcription.  
- 📂 **Saves Results in Structured Format**: Outputs transcriptions as **TXT** and **JSON**.  
- ⚡ **Optimized for Speed**: Uses **GPU (CUDA)** if available for faster processing.  

---

## **📁 Folder Structure**  
```
📦 AI-Whisper-Transcription
 ┣ 📂 transcriptions/       # Output folder (transcription results)
 ┣ 📂 media/                # Input folder (place audio/video files here)
 ┣ 📜 transcribe.py         # Main script
 ┣ 📜 requirements.txt      # Required dependencies
 ┣ 📜 README.md             # Project documentation
```

---

## **📦 Installation**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-repo/AI-Whisper-Transcription.git
cd AI-Whisper-Transcription
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Ensure You Have FFmpeg Installed**  
MoviePy requires FFmpeg for audio extraction. Install it using:  
- **Linux:** `sudo apt install ffmpeg`  
- **Mac:** `brew install ffmpeg`  
- **Windows:** Download from [FFmpeg](https://ffmpeg.org/download.html)  

---

## **🚀 Usage**  
### **1️⃣ Place Media Files in the `/media` Folder**  
Put your **audio and video** files inside the `media/` folder.  

### **2️⃣ Run the Script**  
```bash
python transcribe.py
```
The script will **scan, process, and transcribe** all media files inside the folder.  

### **3️⃣ Check the Output Folder**  
After processing, transcription files are saved in the `/transcriptions` folder in **both TXT and JSON** formats.  

---

## **⚙️ How It Works**
### **🔍 1. Folder Scanning**  
The script **recursively scans** the `/media` folder and identifies audio and video files.

### **🎬 2. Processing Video Files**  
If a **video file** is detected, **MoviePy** extracts the audio and converts it into **WAV format**.

### **🧠 3. AI-Powered Speech-to-Text**  
Whisper's **tiny model** is used for transcription:
```python
result = model.transcribe(audio_path)
```

### **📂 4. Save Results in Multiple Formats**  
The transcriptions are stored in:
- **TXT Format** for human-readable text.
- **JSON Format** for structured storage and further processing.

---

## **🛠 Features & Functionality**
✅ **Supports Multiple Audio Formats:** MP3, WAV, FLAC, M4A, etc.  
✅ **Supports Video Processing:** Extracts audio from MP4, AVI, MKV, etc.  
✅ **Uses OpenAI Whisper Model:** AI-powered transcription with high accuracy.  
✅ **Saves Outputs in Structured Formats:** TXT & JSON for easy access.  
✅ **Automatic Audio Cleanup:** Deletes temporary audio files after transcription.  
✅ **Error Handling & Logging:** Uses `try-except` blocks for efficient execution.  
✅ **Fast Processing with GPU:** Uses CUDA if available for faster transcriptions.  

---

## **📊 Example Output**
### **🎬 Sample Video Input:**  
**Input:** `interview.mp4`  
The script extracts audio and transcribes it.

### **📂 Transcription Output (TXT Format)**
```
interview_2024-02-01_12-30-45.txt
------------------------------------
Hello everyone, welcome to this interview.
Today, we will discuss AI innovations...
```

### **📜 JSON Format**
```json
{
    "file": "interview.mp4",
    "transcription": "Hello everyone, welcome to this interview. Today, we will discuss AI innovations..."
}
```

---

## **💡 Future Improvements**
🔹 **Multi-Language Support**: Use Whisper’s larger models for better **multi-language transcription**.  
🔹 **Speaker Diarization**: Implement **speaker separation** to identify different voices in audio.  
🔹 **Real-Time Transcription**: Extend the script for **live speech recognition**.  
🔹 **Cloud Integration**: Save transcriptions to **Google Drive or AWS S3**.  

---

## **📜 License**
This project is licensed under the **MIT License**.

---


### 🚀 **Now Run the Script and Convert Your Media Files into Accurate Transcriptions!** 🎉
