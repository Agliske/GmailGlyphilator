import glyphilator
import histoGlyphilator
import os
import pandas as pd

search_metadata = {"scaling_range": (0.1,0.7),
                    "scaling_type":"minmax"}

csv_dir_path = os.path.join(os.getcwd(),"examples","histoglyphilator","tiny_examples")
output_dir_path = os.path.join(os.getcwd(),"antz","antz","User","Prototypes","example")
histoGlyphilator.create_viz(csv_dir_path,output_dir_path,search_metadata)