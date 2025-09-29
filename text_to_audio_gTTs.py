import os
from gtts import gTTS

def text_to_speech_file(text: str, folder: str) -> str:
    # Create folder if not exists
    folder_path = os.path.join("user_uploads", folder)
    os.makedirs(folder_path, exist_ok=True)

    # Save path
    save_file_path = os.path.join(folder_path, "audio.mp3")

    # Generate speech
    tts = gTTS(text=text, lang="en")
    tts.save(save_file_path)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    return save_file_path


# # Example usage
# text_to_speech_file(
#     "Mujhe aap bahot pasand ho",
#     "b63f2f94-9b51-11f0-ba36-c035326f0804"
# )
