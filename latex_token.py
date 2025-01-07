#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data about a token occurrence in a source string.
"""

class Token():

    start: int
    length: int
    string: str

    def __init__(self, start: int, length: int, string: str) -> None:
        self.start = start
        self.length = length
        self.string = string

    def __repr__(self) -> str:
        return f'[{self.start}:{self.end}] {self.string}'

    @property
    def end(self) -> int:
        return self.start + self.length

