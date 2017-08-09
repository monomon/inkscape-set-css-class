#!/usr/bin/env python

"""
Sets a css class on selected elements, while optionally removing the elements' styling.
If inline styles are not removed, the css class might not have effect.

Inspired by MergeStyles (and best used together with it).
"""

__author__ = "Mois Moshev"
__email__ = "mois@monomon.me"
__copyright__ = "Copyright (C) 2017 Mois Moshev"
__license__ = "GPL"

import inkex
import sys

class SetCSSClass(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("-n", "--name",
                                     action="store", type="string",
                                     dest="name", default="",
                                     help="Name of css class to apply")
        self.OptionParser.add_option("-c", "--clear_styles",
                                     action="store", type="inkbool",
                                     dest="clear_styles", default=True,
                                     help="Name of css class to apply")

    def effect(self):
        newclass = self.options.name
        elements = self.selected.values()

        for el in elements:
            current_classes = el.attrib.has_key("class") and el.attrib["class"].split() or []

            if newclass not in current_classes:
                current_classes.append(newclass)

            if self.options.clear_styles:
                el.attrib["style"] = ""

            el.attrib["class"] = " ".join(current_classes)

if __name__ == "__main__":
    e = SetCSSClass()
    e.affect()
