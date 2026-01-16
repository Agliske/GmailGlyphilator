import glyphilator
import histoGlyphilator
import os
import pandas as pd
import matplotlib as mpl
import numpy as np


# csv_dir = os.path.join(os.getcwd(),"examples","histoglyphilator","tiny_examples")
# output_file = os.path.join(os.getcwd(),"examples","histoglyphilator","tiny_examples","test_output_csv.csv")
# basic_glyph_data = [0.95, 0.65, 0.63, 0.55, 0.45]
# hyper_histoglyph_list = [[0.6,0.8,0.5,0.7],[0.3,0.2,0.8,0.2],[0.6,0.5,0.8,0.1]]

# keys_list = list(mpl.colormaps.keys())

# print(keys_list)
search_metadata = {"histoglyph_bar_colors": [],
                   "csv_headerFlags":[True,True,None,None]}
current_wordlist_folder = os.path.join(os.getcwd(),"examples","histoglyphilator","tiny_examples")

def generate_colormap_list():
    global search_metadata
    global current_wordlist_folder
    global dropdown_csvSelector

    
    file_list = os.listdir(current_wordlist_folder)
    csv_list = []
    for filepath in file_list:
        if filepath.endswith('.csv'):
            csv_list.append(os.path.join(current_wordlist_folder,filepath))
        else:
            continue

    histoglyph_bar_colors = []
    for csv_filepath in csv_list:
        colors = []
        print(csv_filepath)
        csv_array = np.genfromtxt(csv_filepath, delimiter=",",missing_values="",filling_values=0,skip_header=False,encoding="utf-8",dtype=str)
        columnNames = csv_array[0,:]

        for i in range(0,len(columnNames)):
            colors.append('coolwarm')
        histoglyph_bar_colors.append(colors)
    
    search_metadata["histoglyph_bar_colors"] = histoglyph_bar_colors

generate_colormap_list()
print(search_metadata["histoglyph_bar_colors"])
