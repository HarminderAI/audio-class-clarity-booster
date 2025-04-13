import noisereduce as nr
import librosa
import tempfile
import soundfile as sf
from pydub import AudioSegment

def reduce_noise(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    reduced_noise = nr.reduce_noise(y=y, sr=sr)

    # Save reduced noise to temp wav
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    sf.write(temp_output.name, reduced_noise, sr)

    # Normalize volume
    normalized_path = normalize_audio(temp_output.name)
    return normalized_path

def normalize_audio(file_path):
    sound = AudioSegment.from_file(file_path, format="wav")
    normalized_sound = match_target_amplitude(sound, -20.0)
    temp_path = file_path.replace(".wav", "_normalized.wav")
    normalized_sound.export(temp_path, format="wav")
    return temp_path

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)
