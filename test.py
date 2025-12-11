import librosa
import soundfile as sf
import os

from melo.api import TTS

def synth_with_pitch(
    text: str,
    out_path: str,
    language: str = "KR",  #EN,JP,ZH,KR,FR,ES
    n_steps: float = -5.0, #피치
    device: str ="auto",
    speed: float = 1.0,
):
    tmp_path = "tmp_raw.wav"

    print("TTS 생성 중...")
    model = TTS(language = language, device=device)
    speaker_ids = model.hps.data.spk2id

    if language.upper() == "EN":
        spk = "EN-Default" #기본 억양
    else:
        spk = language.upper()

    model.tts_to_file(text,speaker_ids[spk], tmp_path, speed=speed)

    print("피치 {n_steps} semitone 만큼 조정 중...")
    y, sr = librosa.load(tmp_path,sr=None)
    y_shifted = librosa.effects.pitch_shift(y,sr=sr, n_steps=n_steps)
    sf.write(out_path, y_shifted, sr)

    if os.path.exists(tmp_path):
        os.remove(tmp_path)

    print(f"[완료] {out_path} 생성 (언어={language}, 피치={n_steps} semitone)")



if __name__ == "__main__":

    text = "안녕하세요. 피치조정 테스트를 위해 만들어진 script 입니다."

    synth_with_pitch(
        text=text,
        out_path="kr_low_pitch.wav",
        language="KR",
        n_steps=-8.0,
        device="auto",
        speed=1.0,
    )
