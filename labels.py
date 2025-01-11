#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from manim import *
from typing import Type

def get_labels(types: List[Type], *objs: Mobject) -> VGroup:
    labels = VGroup()

    # Mobject
    # -> VMobject
    #    -> VGroup -> Table -> MobjectTable
    #    -> VMobjectFromSVGPath
    #    -> SVGMobject
    #       -> Text
    #       -> SingleStringMathTex -> MathTex

    a: Mobject

    def add(parent: Mobject) -> None:
        if type(parent) in types:
            parent_labels = index_labels(parent)
            labels.add(parent_labels)
        if isinstance(parent, VMobject):
            for child in parent.submobjects:
                add(child)

    for obj in objs:
        add(obj)
    return labels
