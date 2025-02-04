import os
import json
import torch
import whisper
from pathlib import Path
from datetime import datetime
from moviepy.editor import VideoFileClip

# Set device (use GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the smallest Whisper model
# The original 'whisper.load_model' has been updated to 'whisper.load_model'
model = whisper.load_model("tiny").to(device)

# Supported file extensions for audio & video
AUDIO_EXTENSIONS = [".mp3", ".wav", ".m4a", ".flac"]
VIDEO_EXTENSIONS = [".mp4", ".mkv", ".avi", ".mov"]

# Input & Output Directories
INPUT_FOLDER = "/content/media"   # Change this to the folder containing media files
OUTPUT_FOLDER = "transcriptions"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Function to extract audio from video
def extract_audio(video_path):
    try:
        video = VideoFileClip(video_path)
        audio_path = str(Path(video_path).with_suffix(".wav"))
        video.audio.write_audiofile(audio_path, codec="pcm_s16le", verbose=False, logger=None)
        return audio_path
    except Exception as e:
        print(f"❌ Error extracting audio from {video_path}: {e}")
        return None

# Function to transcribe audio using Whisper
def transcribe_audio(file_path):
    try:
        print(f"🔍 Processing: {file_path}")
        result = model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        print(f"❌ Error transcribing {file_path}: {e}")
        return None

# Main function to scan and transcribe media files
def process_media_folder(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = Path(file).suffix.lower()

            # Process audio files directly
            if file_ext in AUDIO_EXTENSIONS:
                transcription = transcribe_audio(file_path)

            # Process video files (extract audio first)
            elif file_ext in VIDEO_EXTENSIONS:
                audio_path = extract_audio(file_path)
                if audio_path:
                    transcription = transcribe_audio(audio_path)
                    os.remove(audio_path)  # Remove extracted audio after processing

            else:
                continue  # Skip unsupported file types

            # Save transcription results
            if transcription:
                save_transcription(file, transcription)

# Function to save transcriptions as JSON & TXT
def save_transcription(file_name, transcription):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base_name = Path(file_name).stem

    # Save as TXT
    txt_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_{timestamp}.txt")
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(transcription)

    # Save as JSON
    json_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_{timestamp}.json")
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump({"file": file_name, "transcription": transcription}, json_file, indent=4)

    print(f"✅ Transcription saved: {txt_path}")

# Run the script
if __name__ == "__main__":
    print("🚀 Starting Transcription Process...")
    process_media_folder(INPUT_FOLDER)
    print("🎉 All files processed successfully!")
"_________________________________________________________________________________________________________________________________________"


"2"

import os
import json
import torch
import whisper
from pathlib import Path
from datetime import datetime
from moviepy.editor import VideoFileClip

# Set device (use GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the smallest Whisper model
model = whisper.load_model("tiny").to(device)

# Supported file extensions for audio & video
AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a", ".flac"}
VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov"}

# Input & Output Directories
INPUT_FOLDER = "/content/media"   # Change this to the folder containing media files
OUTPUT_FOLDER = "transcriptionssss"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def extract_audio(video_path):
    """Extracts audio from a video file and saves it as a WAV file."""
    try:
        audio_path = str(Path(video_path).with_suffix(".wav"))
        with VideoFileClip(video_path) as video:
            video.audio.write_audiofile(audio_path, codec="pcm_s16le", verbose=False, logger=None)
        return audio_path
    except Exception as e:
        print(f"❌ Error extracting audio from {video_path}: {e}")
        return None

def transcribe_audio(file_path):
    """Transcribes an audio file using Whisper AI."""
    try:
        print(f"🔍 Processing: {file_path}")
        result = model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        print(f"❌ Error transcribing {file_path}: {e}")
        return None

def process_media_folder(folder):
    """Scans and processes media files in the given folder."""
    for root, _, files in os.walk(folder):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                file_ext = Path(file).suffix.lower()

                if file_ext in AUDIO_EXTENSIONS:
                    transcription = transcribe_audio(file_path)

                elif file_ext in VIDEO_EXTENSIONS:
                    audio_path = extract_audio(file_path)
                    if audio_path:
                        transcription = transcribe_audio(audio_path)
                        os.remove(audio_path)  # Clean up extracted audio after use

                else:
                    continue  # Skip unsupported file types

                if transcription:
                    save_transcription(file, transcription)

            except Exception as e:
                print(f"❌ Unexpected error processing {file}: {e}")

def save_transcription(file_name, transcription):
    """Saves transcription in both TXT and JSON formats."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        base_name = Path(file_name).stem

        txt_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_{timestamp}.txt")
        json_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_{timestamp}.json")

        with open(txt_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(transcription)

        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump({"file": file_name, "transcription": transcription}, json_file, indent=4)

        print(f"✅ Transcription saved: {txt_path}")

    except Exception as e:
        print(f"❌ Error saving transcription for {file_name}: {e}")

if __name__ == "__main__":
    print("🚀 Starting Transcription Process...")
    process_media_folder(INPUT_FOLDER)
    print("🎉 All files processed successfully!")
