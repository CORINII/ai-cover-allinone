import os

def separate(song_path):
    inst = "temp/inst.wav"
    vocal = "temp/vocal.wav"
    os.makedirs("temp", exist_ok=True)
    print("✨ (예시) 노래를 inst와 vocal로 분리했다고 가정")
    return vocal, inst
