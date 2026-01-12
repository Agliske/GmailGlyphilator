import glyphilator
import histoGlyphilator
import os
import pandas as pd

angles = histoGlyphilator.angle_spacing(6)
loc_dict_list = histoGlyphilator.format_angles_to_loc_dict(angles)