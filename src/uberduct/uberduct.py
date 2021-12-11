from collections import defaultdict
import os
import re

_arpabet_dict = defaultdict(list)


def _load_dict():
    with open(
        os.path.join(os.path.dirname(__file__), "dict/cmudict.dict"), "r"
    ) as f:
        for line in f.readlines():
            line = line.strip("\n")
            grapheme, *arpa = line.split(" ")
            grapheme = re.sub(r"\(\d+\)", "", grapheme)
            _arpabet_dict[grapheme].append(arpa)


def dict():
    if len(_arpabet_dict) == 0:
        _load_dict()
    return _arpabet_dict
