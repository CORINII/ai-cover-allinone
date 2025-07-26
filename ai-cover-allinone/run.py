import os
from scripts import demucs, enhance, rvc_train, pitch_extract, merge_audio

USER_ID = "user01"
SONG = "input/song.mp3"
VOICE = "input/voice_sample.mp3"
OUT = "output/cover_song.mp3"

def main():
    os.makedirs("output", exist_ok=True)
    os.makedirs("models", exist_ok=True)

    print("🎵 Step 1: 노래에서 보컬 분리 중...")
    vocal_path, inst_path = demucs.separate(SONG)

    print("🧑‍🎤 Step 2: AI 가수 학습 또는 불러오기...")
    model_path = rvc_train.get_or_train(USER_ID, VOICE)

    print("📈 Step 3: 음정 추출 중...")
    pitch_path = pitch_extract.extract(vocal_path)

    print("🧼 Step 4: AI 목소리로 커버곡 생성 중...")
    new_vocal_path = enhance.synthesize(model_path, pitch_path, inst_path)

    print("🎛️ Step 5: 반주랑 믹싱 중...")
    merge_audio.combine(new_vocal_path, inst_path, OUT)

    print("✅ 완료! 결과 파일:", OUT)

if __name__ == "__main__":
    main()
