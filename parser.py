#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mobject
 +- VMobject
    +- SVGMobject
       +- Text
       +- SingleStringMathTex
          +- MathTex

VMobject has a list of child VMobjects called submobjects.
"""

from manim import *

class Parser():

    def parse(self, root: Mobject) -> None:

        def parse_ssmt(tex: SingleStringMathTex) -> None:
            print(type(tex).__name__, len(tex))

        def parse_node(parent: Mobject) -> None:
            if type(parent) is SingleStringMathTex:
                parse_ssmt(parent)
            elif isinstance(parent, VMobject):
                for child in parent.submobjects:
                    parse_node(child)

        parse_node(root)

if __name__ == '__main__':
    parser = Parser()
    tex = MathTex('x=1', 'y=2')
    parser.parse(tex)
