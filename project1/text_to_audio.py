import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY

 
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def text_to_speech_file(text: str, folder: str) -> str:
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", 
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5", 
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )
    dir_path = f"user_uploads/{folder}"
    os.makedirs(dir_path, exist_ok=True)

    save_file_path = os.path.join(dir_path, "audio.mp3")


    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    return save_file_path


text_to_speech_file("Best python course" , "30aa0546-0c2c-11f1-af80-60a5e2230c61")