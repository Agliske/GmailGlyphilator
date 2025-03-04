import glyphilator


search_metadata = {
                                            "subject_string":"Google Alert: sample subject",
                                            "dateRange":{"startDate":None,"endDate":None,"newerThan":"Today"},
                                            "rest_api_query":"Subject:Google Alert",
                                            "headless_browser": True,
                                            "geometrySelection": "Toroid",
                                            "wordlist_paths" : ["path/to/WL1.txt","path/to/WL2.txt","path/to/WL3.txt"],
                                            "search_fuzziness":0.6,
                                            "search_string": "sample string",
                                            "num_results_requested": 200,
                                            "scaling_range": (0.2,2.5),
                                            "scaling_type": "minmax",
                                            "scaling_scope":"dataset", #determines if glyphs scaling is relative to max and min of whole dataset, or just 1 glyph.
                                            "scaling_wrt_wordlist":"total", #options ["total","percent","boolean"]
                                            "save_matched_words":False,
                                            "protos_save_path":"path/to/antz/save/dir",
                                            "uploaded_articledata_path":"None",
                                            "scale_method":"wordlist",
                                            "csv_headerFlags":[True,True]} #csv_headerflags determines if the [first row, first column] of csv dataset are identifiers or tags as opposed to data

csv_filepath = r"C:\Users\aglis\Documents\Python_Projects\GmailGlyphilator\examples\student_dataset.csv"
allGlyphData_dict, articleData, search_metadata = glyphilator.generateGlyphInput_CSV(csv_filepath,search_metadata=search_metadata)
# print("allglyphdata_dict = ", allGlyphData_dict)

# print(search_metadata["wordlist_paths"])
scaled_allglyphdata,unScaled_allglyphdata = glyphilator.scaleFunc_forCSV(allGlyphData_dict,search_metadata)
print("unscaled data = \n", unScaled_allglyphdata)
print("scaled data = \n",scaled_allglyphdata)