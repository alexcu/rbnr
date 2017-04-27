#!/usr/bin/env python
"""
Main entry point of the RBN recogniser program
"""

from os import path
from glob import glob
from sys import argv
from photo import Photo
import methods

assert len(argv[1:]) == 2, "Usage: ./rbnr method dataset_path"

METHOD_NAME, DS_PATH = argv[1:]

assert path.isdir(DS_PATH), "Given dataset path '%s' does not exist" % DS_PATH

METHOD_DICT = {
    'bibnumber': methods.bibnumber.BibnumberMethod()
}

assert METHOD_NAME in METHOD_DICT.keys(), "Given method '%s' is unknown" % METHOD_NAME

METHOD = METHOD_DICT[METHOD_NAME]
DS_FILES = [path.realpath(f) for f in glob('%s/*.jpg' % DS_PATH)]

for filename in DS_FILES:
    Photo(filename, METHOD)
