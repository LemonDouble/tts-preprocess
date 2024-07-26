# tts-preprocess

자체제작 TTS를 만들기 위해 데이터를 전처리합니다.
일회용 스크립트로 짠 내용이라 좀 지저분할 수 있습니다(..)

사용 전에 data, cleaned 두 폴더를 만들어 폴더 구조를 다음과 같이 해 주세요.

```
/
ㄴdata
ㄴcleaned
calculate_length.py
extract_wav_1.py
change_name_2.py
make_list_3.py
(추가) 내가 좋아하는 애니메이션
(추가) 내가 좋아하는 애니메이션 자막
```

작업 프로세스는 다음과 같습니다.

1. git clone, poetry install 이후 좋아하는 애니메이션과 원어 자막을 가져온다.
2. extract_wav_1.py에 비디오 파일 명(video_file),자막 파일 명(subtitle_file)을 설정 후 실행하여 자막 파일을 기준으로 데이터를 분해한다.
3. UVR을 이용하여 원본 데이터에서 배경음악 등의 노이즈를 제거하고, cleaned 폴더에 제거된 wav 파일들을 모은다.
4. cleaned 폴더에 있는 wav 파일을 하나씩 들으며, 다른 소리가 섞였거나 내가 좋아하는 캐릭터가 아닌 데이터를 제거, 깨끗한 내가 좋아하는 캐릭터 목소리만 남긴다.
5. 데이터 처리가 끝났다면, change_name_2.py를 실행해 cleaned 폴더 내 파일들의 이름을 정리한다.
6. make_list_3.py 에서 자막 파일 명(subtitle_file), 캐릭터 명(character_name), 언어 (language) 을 설정 후 실행하여 esd.list 파일을 만든다.
7. calculate_length.py를 실행하여 몇 분 모았는지 확인한다(...)
8. 데이터가 충분히 모일때까지 반복한다.