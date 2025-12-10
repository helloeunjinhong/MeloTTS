from melo.api import TTS

def main():
    speed =1.0
    device = 'cpu'
    text = "안녕하세요! 오늘 날씨가 좋죠?"

    model = TTS(language='KR', device=device)
    speaker_ids = model.hps.data.spk2id

    output_path = 'kr_test.wav'
    model.tts_to_file(text,speaker_ids['KR'], output_path, speed=speed)
    print(f"생성 완료: {output_path}")


if __name__ == "__main__":
    main()