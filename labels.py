#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from manim import *
from typing import Type

def get_labels(*objs: VMobject) -> VGroup:
    """
    Get index_labels for children of MathTex objects.

    Parameters:
    objs: the VMobject instances to be traversed recursively. For each MathTex 
    object found, the index_labels of its children are added to the output. 

    Returns:
    VGroup: A VGroup containing the index_labels of all matching objects.
    """
    labels = VGroup()

    def add(parent: VMobject) -> None:
        if type(parent) == MathTex:
            for child in parent.submobjects:
                labels.add(index_labels(child))
        if isinstance(parent, VMobject):
            for child in parent.submobjects:
                add(child)

    for obj in objs:
        add(obj)
    return labels
