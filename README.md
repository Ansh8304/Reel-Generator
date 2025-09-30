# InstaReel Generator 🎬

This project is a simple, web-based application built with **Flask** that automatically generates short video reels (like those found on Instagram or TikTok) from a user's uploaded images and text description. It combines uploaded images into a sequence and overlays a generated voiceover, perfect for quickly creating engaging social media content.

---

## 💡 How It Works

The application operates in two main parts: the web interface and the background processing service.

1.  **Web Interface (`main.py`):**
    * Users upload their images and provide a text description via a simple form.
    * The application generates a unique folder ID (using `uuid.uuid1()`) and stores the images, along with the text description in a `desc.txt` file, inside the `user_uploads/` directory.
    * It also creates an `input.txt` file (similar to `sample_input_ffmped.txt`) that lists the uploaded images and sets a **2-second duration** for each one, preparing them for concatenation.

2.  **Background Processor (`generate_process.py`):**
    * This script runs continuously, checking for new, unconverted folders in `user_uploads/`.
    * **Text-to-Speech:** It uses the `text_to_audio_gTTs.py` module (which leverages **gTTS**) to convert the text in `desc.txt` into an `audio.mp3` file.
    * **Reel Creation (FFmpeg):** It then uses a powerful **FFmpeg** command (as seen in `ffmped_command.txt`) to:
        * Concatenate the images listed in `input.txt`.
        * Overlay the generated `audio.mp3`.
        * Scale and pad the video to the popular **1080x1920** (9:16 vertical) resolution.
        * Save the final reel as an MP4 file in `static/reels/`.
    * Once a folder is processed, its ID is added to the `done.txt` file to prevent reprocessing.

---

## 🛠️ Key Technologies

* **Backend Framework:** Python (Flask)
* **Media Processing:** FFmpeg
* **Text-to-Speech:** gTTS
* **Tools:** `os`, `subprocess`, `uuid`
