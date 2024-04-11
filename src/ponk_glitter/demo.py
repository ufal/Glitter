#!/usr/bin/env python3
from models.robeczech import Robeczech
from lib.tui import print_glittered_text, print_table_of_glittered_text

text = "Dneska je všední den."

rbcz = Robeczech()
gt = rbcz.glitter_text(text)
print_table_of_glittered_text(gt)
print_glittered_text(gt)
