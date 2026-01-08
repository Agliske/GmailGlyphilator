import numpy as np
import csv
import os
import glyphilator as gly
import pandas as pd
from glyphilator import scaleFunc_forCSV

def bar_spacing(num_bars = 10,spacing = 0.5):
    """
    bar_spacing genearates an evenly spaced list of entries centered at 0 position.

    Args:
        num_bars (int, optional): Number of entries in spacing list. Defaults to 10.
        spacing (float, optional): how far apart the entries should be. Defaults to 2.5.

    Returns:
        list: evenly spaced numbers
    """
    
    loc = 0
    centering_offset = num_bars * spacing /2
    spacing_list = [0 - centering_offset + spacing/2]
    
    for i in range(0,num_bars - 1):
        loc = loc + spacing
        spacing_list.append(loc - centering_offset + spacing/2)
    
    return spacing_list


def generate_histoglyph_input(path_to_csvs,search_metadata = {"scaling_range": (0.0,2.5),
                                                              "scaling_type":"minmax"}):
    """
    generate_histoglyph_input generates the necessary data structures to construct a hyper-histoglyph.

    Args:
        path_to_csvs (string): absolute path to a directory containing CSVs

    Returns:
        List of list of list of float: all the data to make a histoglyph viz. If second level list has more than 1 element it creates 
        a hyper-histoglyph, which is a glyph of histo-glyphs
    """
    #histoglyph_list = [[[1,2,3]], #creates 4 regular histoglyphs. generated from a single 3-column, 4 row CSV
    #                   [[1,2,3]],
    #                  [[1,2,3]],
    #                  [[1,2,3]],
    #                  ] 

    #histoglyph_list = [[[1,2,3],[1,2,3]]] # this is one row of two 3-col csvs. creates a single hyper-histoglyph with 2 histoglyphs, 3 bars each

    #histoglyph_list = [[[1,2,3],[1,2,3]], #this contains 4 hyper-histoglyphs. 2 histoglyphs, 3 cols each
    #                   [[1,2,3],[1,2,3]],
    #                   [[1,2,3],[1,2,3]],
    #                   [[1,2,3],[1,2,3]]
    #                  ]    

    #collect list of CSV paths in chosen dir
    #open each, verify number of rows is the same for each, throw error if not.
    
    #initialize histoglyph_list_scaled
    #initialize histoglyph_list_unscaled
    #append and empty list per row in the csvs in each

    #initialize col_name_list = []
    
    
    #for each csv path:

        #open each CSV, save column names in a list of list of str (this will be our tags: column-name:Data)
        #remove the first row(column names)

        #in_dict = {"total": csv_array_scaled}
        #csv_array_scaled, csv_array_unscaled = scaleFunc_forCSV()

        # for each row in csv:

            #append the data for that row to histoglyph_list[row].append(row_data_as_list)
    
    files = os.listdir(path_to_csvs)
    
    #get list of filepaths for each csv in the given directory
    list_csv_filepaths = []
    for file in files:
        if file.endswith('.csv'):
            list_csv_filepaths.append(path_to_csvs + "\\" + file)
    
    #open each file, verify that they have same num rows (also initialize histoglyph_list with empty lists = num rows)
    histoglyph_list_scaled = []
    histoglyph_list_unscaled = []
    numrows = 0
    for line in open(list_csv_filepaths[0]):
        numrows = numrows + 1
        histoglyph_list_unscaled.append([])
        histoglyph_list_scaled.append([])

    histoglyph_list_unscaled.pop(-1) #removing because my for loop included the header, which we won't use.
    histoglyph_list_scaled.pop(-1)

    for i in range(0,len(list_csv_filepaths)):
        path = list_csv_filepaths[i]
        checked_rows = 0
        for line in open(path):
            checked_rows = checked_rows + 1
        
        if checked_rows != numrows:
            raise ValueError
    
    #scale each csv by data in each column, mapped to mintarget/maxtarget for glyph scaling, then organize appropriately
    column_names_list = []
    for path in list_csv_filepaths:
        unscaled_data_array = np.loadtxt(path,delimiter=",",skiprows=1)
        
        #save column names to the list, for use as tags later
        with open(path) as file:
            reader = csv.reader(file)
            headers = next(reader)
        column_names_list.append(headers)

        data_in_dict = {"total":unscaled_data_array}
        scaled_data_array, unscaled_data_array = scaleFunc_forCSV(data_in_dict,search_metadata)

        for j in range(0,unscaled_data_array.shape[0]):
            unscaled_row = unscaled_data_array[j,:]
            scaled_row = scaled_data_array[j,:]

            histoglyph_list_scaled[j].append(scaled_row.tolist())
            histoglyph_list_unscaled[j].append(unscaled_row.tolist())


    return histoglyph_list_scaled,histoglyph_list_unscaled,column_names_list

def generate_single_histoglyph(parent_id,last_used_id,glyph_data,tag_data,search_metadata = {}):
    """
    generate_single_glyph generates a snippet of an antzfile pertaining to a single histoglyph. Assumes 
    the header is generated elsewhere.

    Args:
        parent_id (int): the parent node that you want this glyph to sit on
        last_used_id(int): the starting point to assign new node ids from
        glyph_data (list of float): the unscaled data that will size the elements of the glyph
        tag_data (list of str): the 
        search_metadata (dict): search_metadata config dictionary used by glyphilator.py, and gui.py
    """
    cwd = os.getcwd()
    working_glyph_row_path = os.path.join(cwd,"resources","histo_glyph","glyph_layer_2_model_ring.csv")
    first_two_element_of_glyph_path = os.path.join(cwd,"resources","histo_glyph","glyph_root_and_layer_1.csv")
    tag_file_path = os.path.join(cwd,"resources","histo_glyph","tag_file_header.csv")

    #pre-calculating where the bars should be on the plane
    spacing_list = bar_spacing(len(glyph_data))
    
    working_glyph = pd.read_csv(first_two_element_of_glyph_path)

    node_id_counter = last_used_id



    #update node_id, parent_id, record_id for root node
    node_id_counter = node_id_counter + 1
    working_glyph.loc[working_glyph.index[0],['np_node_id','np_data_id','record_id']] = node_id_counter
    working_glyph.loc[working_glyph.index[0],'parent_id'] = parent_id #the parent id for the root is always 0

    #update the node_id, parent_id, of layer 1 node (plane)
    node_id_counter = node_id_counter + 1
    working_glyph.loc[working_glyph.index[1],['np_node_id','np_data_id','record_id']] = node_id_counter
    working_glyph.loc[working_glyph.index[1],'parent_id'] = node_id_counter - 1 #parent id for layer 1 is root id. aka current id - 1
    node_id_plane = node_id_counter #saving node id of layer 1 toroid to access in next for loop

    #add a bar for every element in glyph_data list
    for i in len(glyph_data):

        working_row = pd.read_csv(working_glyph_row_path)
        node_id_counter = node_id_counter + 1
        working_row.loc[working_row.index[0],['np_node_id','np_data_id','record_id']] = node_id_counter
        working_row.loc[working_glyph.index[0],'parent_id'] = node_id_plane

        #place the bar correctly on plane
        working_row.loc[working_row.index[0],'translate_x'] = None
        working_row['translate_x'] = working_row['translate_x'].astype(float)
        working_row.loc[working_row.index[0],'translate_x'] = spacing_list[i]

        #scale data by glyph data scale factor
        working_row.loc[working_row.index[0],'scale_z'] = None
        working_row['scale_z'] = working_row['scale_z'].astype(float)
        working_row.loc[working_row.index[0],'scale_z'] = glyph_data[i]

        #Appending row to glyph
        working_glyph = pd.concat([working_glyph,working_row])
    
    last_used_id = node_id_counter
    
    return working_glyph, last_used_id







def initialize_viz():

    cwd = os.getcwd()
    core_glyph_csv_path = os.path.join(cwd,"resources","histo_glyph","glyph_header.csv")
    working_glyph_row_path = os.path.join(cwd,"resources","histo_glyph","glyph_layer_2_model_ring.csv")
    first_two_element_of_glyph_path = os.path.join(cwd,"resources","histo_glyph","glyph_root_and_layer_1.csv")
    tag_file_path = os.path.join(cwd,"resources","histo_glyph","tag_file_header.csv")
    
    antzfile = pd.read_csv(core_glyph_csv_path)

