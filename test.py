import glyphilator
import histoGlyphilator
import os
import pandas as pd

csv_dir = os.path.join(os.getcwd(),"examples","histoglyphilator","tiny_examples")
output_file = os.path.join(os.getcwd(),"examples","histoglyphilator","tiny_examples","test_output_csv.csv")
basic_glyph_data = [0.95, 0.65, 0.63, 0.55, 0.45]
hyper_histoglyph_list = [[0.6,0.8,0.5,0.7],[0.3,0.2,0.8,0.2],[0.6,0.5,0.8,0.1]]

angles_list = histoGlyphilator.angle_spacing(len(hyper_histoglyph_list))
loc_dict_list = histoGlyphilator.format_angles_to_loc_dict(angles_list)
# print("loc_dict_list = ", loc_dict_list)



antzfile = pd.read_csv(os.path.join(os.getcwd(),"resources","histo_glyph","glyph_header.csv"))

parent_id = 40 #np_node_id of the plane object is 40. We want to drop all of our things on the plane.
last_used_id = 40 

pin_and_ring = pd.read_csv(os.path.join(os.getcwd(),"resources","histo_glyph","hyperglyph_root_and_ring.csv"))


#change ids, parent ids of pin and ring to be appropriate
pin_and_ring.loc[pin_and_ring.index[0],["parent_id"]] = last_used_id #last used is currently the plane. likely need to save this id.
last_used_id = last_used_id + 1
pin_and_ring.loc[pin_and_ring.index[0],['np_node_id','np_data_id','record_id']] = last_used_id
pin_and_ring.loc[pin_and_ring.index[1],["parent_id"]] = last_used_id
last_used_id = last_used_id + 1
pin_and_ring.loc[pin_and_ring.index[1],['np_node_id','np_data_id','record_id']] = last_used_id
parent_id = last_used_id
antzfile = pd.concat([antzfile,pin_and_ring])

for i in range(0,len(hyper_histoglyph_list)):
    working_glyph,last_used_id = histoGlyphilator.generate_single_histoglyph(parent_id,last_used_id,basic_glyph_data,basic_glyph_data,search_metadata={})
    working_glyph = histoGlyphilator.apply_location_to_glyph(working_glyph,0,loc_dict_list[i])
    antzfile = pd.concat([antzfile,working_glyph])

antzfile.to_csv(output_file,index=False,encoding="utf-8")
#working_glyph,last_used_id = histoGlyphilator.generate_single_histoglyph(parent_id,last_used_id,basic_glyph_data,basic_glyph_data,search_metadata={})
#antzfile = pd.concat([antzfile,working_glyph])
#antzfile.to_csv(output_file,index=False,encoding="utf-8")



