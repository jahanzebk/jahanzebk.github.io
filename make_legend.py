import json
import os
import re
from PIL import Image

extensions_regex = "\\.((jpg)|(jpeg)|(png))$"

def get_files_to_add():
    files = [f"uploads/{file}" for file in os.listdir("uploads") if re.search(extensions_regex, file.lower())]
    print(files)
    return files

def get_aspect_ratio(file):
    with Image.open(file) as im:
        w, h = im.size
        aspect = w / h
        return aspect

def write_legend(files):
    legend = []
    with open("legend.json", "r") as legend_file:
        json_data = legend_file.read()
        legend = json.loads(json_data)
    for file in files:
        aspect_ratio = get_aspect_ratio(file)
        filename = file.split("/")[1]
        print(f"{filename}, {aspect_ratio}")
        legend.insert({0, "filename": filename, "aspectRatio": aspect_ratio})
    json_content = json.dumps(legend, indent=4)
    with open("legend.json", "w") as legend_file:
        legend_file.write(json_content)



def main():
    files = get_files_to_add()
    write_legend(files)

main()