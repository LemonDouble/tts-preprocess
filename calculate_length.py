import os
import wave
import contextlib

folder_path = 'cleaned'

total_duration = 0.0

for filename in os.listdir(folder_path):
    if filename.endswith('.wav'):
        file_path = os.path.join(folder_path, filename)
        with contextlib.closing(wave.open(file_path, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            total_duration += duration

minutes = int(total_duration // 60)
seconds = int(total_duration % 60)

print(f'Wav 파일의 총 시간 : {minutes} minutes and {seconds} seconds')
