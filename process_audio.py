import noisereduce as nr
import librosa
import tempfile
import soundfile as sf

def reduce_noise(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    reduced_noise = nr.reduce_noise(y=y, sr=sr)

    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    sf.write(temp_output.name, reduced_noise, sr)

    return temp_output.name
