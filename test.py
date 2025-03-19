import glyphilator


# search_metadata = {
#                                             "subject_string":"Google Alert: sample subject",
#                                             "dateRange":{"startDate":None,"endDate":None,"newerThan":"Today"},
#                                             "rest_api_query":"Subject:Google Alert",
#                                             "headless_browser": True,
#                                             "geometrySelection": "Toroid",
#                                             "wordlist_paths" : ["path/to/WL1.txt","path/to/WL2.txt","path/to/WL3.txt"],
#                                             "search_fuzziness":0.6,
#                                             "search_string": "sample string",
#                                             "num_results_requested": 200,
#                                             "scaling_range": (0.2,2.5),
#                                             "scaling_type": "minmax",
#                                             "scaling_scope":"dataset", #determines if glyphs scaling is relative to max and min of whole dataset, or just 1 glyph.
#                                             "scaling_wrt_wordlist":"total", #options ["total","percent","boolean"]
#                                             "save_matched_words":False,
#                                             "protos_save_path":"path/to/antz/save/dir",
#                                             "uploaded_articledata_path":"None",
#                                             "scale_method":"wordlist",
#                                             "csv_headerFlags":[True,True]} #csv_headerflags determines if the [first row, first column] of csv dataset are identifiers or tags as opposed to data

# csv_filepath = r"C:\Users\aglis\Documents\Python_Projects\GmailGlyphilator\examples\student_dataset.csv"
# allGlyphData_dict, articleData, search_metadata = glyphilator.generateGlyphInput_CSV(csv_filepath,search_metadata=search_metadata)
# # print("allglyphdata_dict = ", allGlyphData_dict)

# # print(search_metadata["wordlist_paths"])
# # scaled_allglyphdata,unScaled_allglyphdata = glyphilator.scaleFunc_forCSV(allGlyphData_dict,search_metadata)
# print("unscaled data = \n", unScaled_allglyphdata)
# print("scaled data = \n",scaled_allglyphdata)
from glyphilator import generate_arc
import pandas as pd
import numpy as np
import os
from mapFetcher_mapbox import fetchMapImage
cwd = os.getcwd()

import pandas as pd

# Load the CSV
file_path = os.path.join(cwd,"examples","dGilsdorf_data","for_alec.csv")
df = pd.read_csv(file_path)

# Fill empty cells with 0
df.fillna(0, inplace=True)

# Save the modified CSV
df.to_csv(os.path.join(cwd,"examples","dGilsdorf_data","for_alec_filled.csv"), index=False)

# longitudes = np.array([-0.1278,
# -2.2426,
# -1.8904,
# -1.5491,
# -2.9916,
# -1.4701,
# -2.5879,
# -1.6174,
# -1.1581,
# -1.4044])

# latitudes = np.array([51.5074,
# 53.4808,
# 52.4862,
# 53.8008,
# 53.4084,
# 53.3811,
# 51.4545,
# 54.9783,
# 52.9548,
# 50.9097])



# mapbox_api_key = r"pk.eyJ1IjoiYWdsaXNrZSIsImEiOiJjbTd4eWkybzEwNDN3MmpwbzE3MW04eTFoIn0.nbkkTpDhyG4WcG5xf-Sr0A"
# url,cornerCoords = fetchMapImage(latitudes,longitudes,0.1,api_key=mapbox_api_key)

# print(url)
# print(cornerCoords)

# sampleurl = "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/pin-s+000(-0.1278,51.5074),pin-s+000(-2.2426,53.4808),pin-s+000(-1.8904,52.4862),pin-s+000(-1.5491,53.8008),pin-s+000(-2.9916,53.4084),pin-s+000(-1.4701,53.3811),pin-s+000(-2.5879,51.4545),pin-s+000(-1.6174,54.9783),pin-s+000(-1.1581,52.9548),pin-s+000(-1.4044,50.9097),pin-s+000(-3.752579999999998,50.50284),pin-s+000(-3.752579999999998,55.38516),pin-s+000(0.8887799999999983,50.50284),pin-s+000(0.8887799999999983,55.38516)/[-3.752579999999998, 50.50284, 0.8887799999999983, 55.38516]/1280x1280@2x?access_token=pk.eyJ1IjoiYWdsaXNrZSIsImEiOiJjbTd4eWkybzEwNDN3MmpwbzE3MW04eTFoIn0.nbkkTpDhyG4WcG5xf-Sr0A"
# core_glyph_csv_path = os.path.join(cwd,"resources","glyph_header.csv")
# antzfile = pd.read_csv(core_glyph_csv_path)
# print(antzfile.loc[:,'np_texture_id'])
# antzfile.loc[antzfile['np_node_id'] == 40,'np_texture_id'] = 999
# print(antzfile.loc[:,'np_texture_id'])
# plot = sca

