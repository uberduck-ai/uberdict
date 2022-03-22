from collections import defaultdict
import os
import re
from pathlib import Path
from requests import get

pathlist = Path(os.path.dirname(__file__)).glob('languages/*')
_arpabet_dict = defaultdict(list)

languages = {"polish": "https://github.com/uberduck-ai/uberduct/releases/download/dictionaries/polish.dict",
             "english": "https://github.com/uberduck-ai/uberduct/releases/download/dictionaries/english.dict"}

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


def _load_dict():
    for path in pathlist:
        if path.is_file():
            print(str(path))
            with open(str(path), "r") as f:
                for line in f.readlines():
                    line = line.strip("\n")
                    grapheme, *arpa = line.split(" ")
                    grapheme = re.sub(r"\(\d+\)", "", grapheme).lower()
                    arpa = list(filter(None, arpa))
                    _arpabet_dict[grapheme].append(arpa)


def dict():
    for i in languages.keys():
        if not Path(os.path.join(os.path.dirname(__file__), "languages/" + i + ".dict")).is_file():
            print("Downlading CMU dictionary for:", i)
            download(languages[i], os.path.join(os.path.dirname(__file__), "languages/" + i + ".dict"))
    if len(_arpabet_dict) == 0:
        _load_dict()
    return _arpabet_dict