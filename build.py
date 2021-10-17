#!/usr/bin/env python3
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
    cn = 1
    us = 2


class Language(Enum):
    en = 1
    zh = 2


def readFile(filename):
    with open(filename, mode="r") as f:
        content = f.read()
    return content


def saveFile(content, filename):
    with open(filename, mode="w") as f:
        f.write(content)


def generateContent(region, language):
    if language == Language.zh:
        content = CJK_ENCODE
    else:
        content = ""

    content += DOCUMENT_CLASS

    if language == Language.zh:
        content += CJK_FONT

    content += readFile("header.tex")

    content += "\\{0}true\n".format(region.name)
    content += "\\{0}true\n".format(language.name)

    content += readFile("content.tex")

    filename = "resume_{0}{1}.tex".format(language.name, region.name.upper())
    saveFile(content, filename)
    os.system("pdflatex {0}".format(filename))


if __name__ == "__main__":
    for r in Region:
        for lang in Language:
            generateContent(r, lang)
