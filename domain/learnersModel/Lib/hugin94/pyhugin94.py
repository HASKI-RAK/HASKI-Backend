# Hugin Python API - Copyright (C) 2017-2023, Hugin Expert A/S.

# -*- coding: utf-8 -*-
from base64 import b64decode as _hh10
from bz2 import decompress as _hh1

FILE_NAME = "domain/learnersModel/Lib/hugin94/read.txt"
f = open(FILE_NAME, "r")
jls_extract_var2 = f.readline()
exec(_hh1(_hh10(jls_extract_var2)))
