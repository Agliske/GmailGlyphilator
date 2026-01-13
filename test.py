import glyphilator
import histoGlyphilator
import os
import pandas as pd
import matplotlib as mpl

csv_dir = os.path.join(os.getcwd(),"examples","histoglyphilator","tiny_examples")
output_file = os.path.join(os.getcwd(),"examples","histoglyphilator","tiny_examples","test_output_csv.csv")
basic_glyph_data = [0.95, 0.65, 0.63, 0.55, 0.45]
hyper_histoglyph_list = [[0.6,0.8,0.5,0.7],[0.3,0.2,0.8,0.2],[0.6,0.5,0.8,0.1]]

keys_list = list(mpl.colormaps.keys())

print(keys_list)


