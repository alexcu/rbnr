#!/usr/bin/env python

from os import path, listdir
from sys import argv
import photo
import methods

assert len(argv[1:]) == 2, "Usage: ./rbnr method dataset_path"

METHOD_NAME, DS_PATH = argv[1:]

assert path.isdir(DS_PATH), "Given dataset path '%s' does not exist" % DS_PATH

METHOD_DICT = {
    'bibdetect': methods.bibdetect.BibdetectMethod()
}

assert METHOD_NAME in METHOD_DICT.keys(), "Given method '%s' is unknown" % METHOD_NAME

METHOD = METHOD_DICT[METHOD_NAME]
DS_FILES = ["%s/%s" % (path.realpath(DS_PATH), f) for f in listdir(DS_PATH)]
