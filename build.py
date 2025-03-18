#!/usr/bin/env python3

"""Build script for generating en/zh resume files"""

import os
from enum import Enum


DOCUMENT_CLASS = r"""\documentclass{resume}
"""
CJK_ENCODE = r"""% !TEX TS-program = xelatex
% !TEX encoding = UTF-8 Unicode
% !Mode:: "TeX:UTF-8"
"""
CJK_FONT = r"""\usepackage{zh_CN-Adobefonts_external}
"""


class Region(Enum):
    """Enum for region, sets correct phone number for resume"""
    CN = 1
    US = 2


class Language(Enum):
    """Enum for language, sets correct language for resume"""
    EN = 1
    ZH = 2


def load_file(filename):
    """Read file content"""
    with open(filename, mode="r", encoding="utf8") as f:
        content = f.read()
    return content


def save_file(content, filename):
    """Save file content"""
    with open(filename, mode="wb") as f:
        f.write(content.encode("utf-8"))


def generate_content(region, language):
    """Generate content for resume"""
    if language == Language.ZH:
        content = CJK_ENCODE
    else:
        content = ""

    content += DOCUMENT_CLASS

    if language == Language.ZH:
        content += CJK_FONT

    content += load_file("header")

    content += f"\\{region.name.lower()}true\n"
    content += f"\\{language.name.lower()}true\n"

    content += load_file("content")

    filename = f"resume_{language.name.lower()}{region.name.upper()}.tex"
    save_file(content, filename)

    if language == Language.ZH:
        os.system(f"xelatex {filename}")
    else:
        os.system(f"pdflatex {filename}")


if __name__ == "__main__":
    for r in Region:
        for lang in Language:
            generate_content(r, lang)
