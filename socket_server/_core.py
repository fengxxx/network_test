import sys

from ctypes import *

if sys.platform=='darwin':
    print "mac"
elif sys.platform=="dos":
    windll.Kernel32.GetStdHandle.restype = c_ulong
    h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

ERROR_START="ERROR_____START"
ERROR_END="ERROR_______END"
DATA_FILE_START="FILE______START"
DATA_FILE_END="FILE________END"
DATA_MSG_START="MSG_______START"
DATA_MSG_END="MSG_________END"
DATA_MSG_END="MSG_________END"
REGIST_GIVE="REGIST_____GIVE"

FONT_COLOR_RED=12
FONT_COLOR_DARKRED=4
FONT_COLOR_BLUE=9
FONT_COLOR_DARKBLUE=1
FONT_COLOR_GREEN=10
FONT_COLOR_DARKGREEN=2
FONT_COLOR_WHITE=15
FONT_COLOR_GRAY=8
FONT_COLOR_YELLOW=14
FONT_COLOR_DARKYELLOW=6
FONT_COLOR_DEFLUT=FONT_COLOR_WHITE


def setFontColor(c):
    if sys.platform=="dos":
        global h
        windll.Kernel32.SetConsoleTextAttribute(h,c)
    else:
        ()
