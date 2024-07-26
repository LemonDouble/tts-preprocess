import os
import uuid

import pysubs2

subtitle_file = ""
character_name = ""
language = "JP"  # ZH, EN
cleand_folder = "./cleaned"

file_list = os.listdir(cleand_folder)

subs = pysubs2.load(subtitle_file)
dialogs = []
for event in subs.events:
    dialogs.append(event.text)

metadata = []
for item in file_list:
    idx = int(item.replace(".wav", ""))
    uid = uuid.uuid4()
    os.rename(f"{cleand_folder}/{item}", f"{cleand_folder}/{uid}.wav")

    metadata.append(f"{uid}.wav|{character_name}|{language}|{dialogs[idx]}\n")

with open("esd.list", "w", encoding="utf-8") as f:
    f.writelines(metadata)
