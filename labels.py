#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from manim import *
from typing import Type

def get_labels(types: List[Type], *objs: Mobject) -> VGroup:
    """
    Get index_labels for objects of given type(s). 

    Parameters:
    types (List[Type]): List of types to check against.
    If it matches a supplied Type, its index_labels are added to the output.
    And then, if it's a VMobject, its submobjects are traversed recursively.

    Returns:
    VGroup: A VGroup containing the index_labels of the matching objects.

    Reminder: Some of the types likely to be encountered during algebraic 
    animations include the following (where -> points to a subclass):

    Mobject
    -> VMobject
       -> VMobjectFromSVGPath
       -> VGroup -> Table -> MobjectTable
       -> Polygram -> Polygon -> Rectangle
       -> SVGMobject
          -> Text
          -> SingleStringMathTex -> MathTex
    """
    labels = VGroup()

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

# TODO: add operation to include only index_labels for objects whose immediate parent is a MathTex.

def get_ssmt_labels(*objs: Mobject) -> VGroup:
    """
    Get index_labels for SingleStringMathTex objects. 

    Parameters:
    objs (Mobject): the supplied objects. Each is checked for its Type.
    If it's a SingleStringMathTex, its index_labels are added to the output.
    And then, if it's a VMobject, its submobjects are traversed recursively.

    Returns:
    VGroup: A VGroup containing the index_labels of all SingleStringMathTex 
    objects found.
    """
    return get_labels([SingleStringMathTex], *objs)
