#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from manim import *

def get_labels(objs: Mobject) -> VGroup:
    labels = VGroup()

    def add(parent: Mobject) -> None:
        if isinstance(parent, SVGMobject):
            labels.add(index_labels(parent))
        if isinstance(parent, VMobject):
            for child in parent.submobjects:
                add(child)

    for obj in objs:
        add(obj)
    return labels
