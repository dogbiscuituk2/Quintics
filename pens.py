from enum import Enum

class Pen(Enum):
    NONE    = 0 # Transparent
    FG      = 1 # Foreground default
    BG      = 2 # Background
    HILITE  = 3 # Highlight background
    BLACK   = 4 # These remaining colour names are all purely logical
    BROWN   = 5
    RED     = 6
    ORANGE  = 7
    YELLOW  = 8
    GREEN   = 9
    BLUE    = 10
    CYAN    = 11
    MAGENTA = 12
    VIOLET  = 13
    GREY    = 14
    WHITE   = 15
