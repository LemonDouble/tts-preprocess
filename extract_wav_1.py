import pysubs2
from moviepy.editor import VideoFileClip


def parse_subtitles(subtitle_file):
    subs = pysubs2.load(subtitle_file)
    dialogues = []
    for event in subs.events:
        start = event.start / 1000.0
        end = event.end / 1000.0
        text = event.text
        dialogues.append((start, end, text))
    return dialogues


def extract_audio(video_file):
    video = VideoFileClip(video_file)
    audio = video.audio
    return audio


def save_audio_clips(audio, dialogues, output_folder):
    for i, (start, end, text) in enumerate(dialogues):
        audio_clip = audio.subclip(start, end)
        audio_clip_path = f"{output_folder}/{i}.wav"
        audio_clip.write_audiofile(audio_clip_path, codec='pcm_s16le')


if __name__ == "__main__":
    video_file = ""
    subtitle_file = ""
    output_folder = "./data"

    dialogues = parse_subtitles(subtitle_file)
    audio = extract_audio(video_file)
    save_audio_clips(audio, dialogues, output_folder)
