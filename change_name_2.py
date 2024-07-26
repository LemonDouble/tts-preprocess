import re
import os


def extract_number_from_filename(filename):
    matches = re.findall(r'\d+', filename)
    return matches[1]


lst = os.listdir("./cleaned")

for item in lst:
    os.rename(f"./cleaned/{item}", f"./cleaned/{extract_number_from_filename(item)}.wav")
