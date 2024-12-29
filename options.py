#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Options class for Painter.
"""

from enum import Flag, auto

class Opt(Flag):
    NONE    = 0
    SUB     = auto() # 'x_1': '1' matches 'x'.
    SUPER   = auto() # 'x^2': '2' matches 'x'.
    DIFF    = auto() # r'\frac{d^2x}{dy^2}': 'd' & '2' match 'x' or 'y'.
    MATH    = auto() # r'\overbrace{x}': brace matches'x'.
    ACCENT  = auto() # r'acute{e}': the accent matches the letter.
    DEBUG   = auto() # override all: assign colours sequentially.
    SHIFT   = SUB | SUPER
    SYM     = MATH | ACCENT
    DEFAULT = SHIFT | DIFF | SYM # everything except DEBUG.

if __name__ == '__main__':

    print(
        Opt.NONE.value,
        Opt.SUB.value,
        Opt.SUPER.value,
        Opt.DIFF.value,
        Opt.MATH.value,
        Opt.ACCENT.value,
        Opt.DEBUG.value,
        Opt.SHIFT.value,
        Opt.SYM.value,
        Opt.DEFAULT.value,
    )
    opts = Opt.SHIFT | Opt.DIFF | Opt.ACCENT

    print(f"{Opt.NONE in opts = }")
    print(f"{Opt.SUB in opts = }")
    print(f"{Opt.SUPER in opts = }")
    print(f"{Opt.DIFF in opts = }")
    print(f"{Opt.MATH in opts = }")
    print(f"{Opt.ACCENT in opts = }")
    print(f"{Opt.DEBUG in opts = }")
    print(f"{Opt.SHIFT in opts = }")
    print(f"{Opt.SYM in opts = }")
    print(f"{Opt.DEFAULT in opts = }")
