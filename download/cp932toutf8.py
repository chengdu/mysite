#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A python helper script for Speare code editor.
# Copyright (c) 2019 sevenuc.com. All rights reserved.
# 
# THIS FILE IS PART OF SPEARE CODE EDITOR. WITHOUT THE
# WRITTEN PERMISSION OF THE AUTHOR THIS FILE MAY NOT
# BE USED FOR ANY COMMERCIAL PRODUCT.
# 
# More info: 
#    http://sevenuc.com/en/Speare.html
# Contact:
#    Sevenuc support <info@sevenuc.com>
# Issue report and requests pull:
#    https://github.com/chengdu/Speare


# This script convert all C and C++ source code files under a special directory 
# from Japanese text encoding cp932 on Windows to UTF-8 encoding, then they can 
# be better understood by the clang compiler on the modern macOS.

import re
import os, sys
import subprocess
import codecs

if (sys.version_info.major == 2):
    reload(sys)
    sys.setdefaultencoding('utf-8')

encode = "cp932"
def run(cmd, logfile):
    p = subprocess.Popen(cmd, shell=False, universal_newlines=True, stdout=logfile)
    ret_code = p.wait()
    logfile.flush()
    return ret_code

def convformat(fullpath):
    global encode # encoding of source file
    # iconv -f cp932 -t UTF-8 inputfile
    tmppath = fullpath + ".u8"
    a = []
    a.append("iconv")
    a.append("-f")
    a.append(encode) # default is cp932.
    a.append("-t")
    a.append("UTF-8")
    a.append(fullpath)
    f = codecs.open(tmppath, "w", "utf-8")
    rc = run(a, f)
    f.close()
    command = "mv \"" + tmppath + "\" \"" + fullpath + "\""
    os.system(command)
    if rc == 0:
        print("convert: " + fullpath + " done.\n")

def walk_folder(dir):
    #ignores = []
    extensions = ['.h', '.c', '.cpp'] # TODO: support more file type and programming languages
    for root, dirs, files in os.walk(dir):
        for f in files:
            #if f in ignores: continue
            fullpath = os.path.join(root, f)
            ext  = os.path.splitext(fullpath)[1]
            if ext in extensions:
                print("process: " + fullpath + " ...\n")
                convformat(fullpath)

def usage():
    print('Usage: '+sys.argv[0]+' [-e "source code encoding"](optional) -d "source code folder"')


def main():
  global encode
  import argparse
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('-e', '--encoding', dest='encoding', type=str, default='cp932',
                 help='The file encoding of the C and C++ project')
  parser.add_argument('-d', '--dir', dest='dir', type=str, default='',
                 help='The source code folder of the C and C++ project')
  args = parser.parse_args()
  dir = args.dir
  if len(dir) == 0 or not os.path.exists(dir):
      usage()
      return
  encode = args.encoding
  walk_folder(dir)


if __name__ == "__main__":
    main()


