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
    ACCENT  = auto() # r'acute{e}': the accent matches the letter.
    SHIFT   = SUB | SUPER
    ALL     = SHIFT | DIFF | ACCENT

print(
    Opt.NONE.value,
    Opt.SUB.value,
    Opt.SUPER.value,
    Opt.SHIFT.value,
    Opt.DIFF.value,
    Opt.ALL.value,
)
opts = Opt.SUB | Opt.SUPER | Opt.DIFF

print(f"{Opt.NONE in opts = }")
print(f"{Opt.SUB in opts = }")
print(f"{Opt.SUPER in opts = }")
print(f"{Opt.SHIFT in opts = }")
print(f"{Opt.DIFF in opts = }")
print(f"{Opt.ALL in opts = }")
