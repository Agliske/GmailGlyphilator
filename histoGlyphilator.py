import numpy as np
import csv
import os
import glyphilator as gly
import pandas as pd
import matplotlib as mpl
from glyphilator import scaleFunc_forCSV,generate_centered_grid
pd.set_option("mode.copy_on_write", True)

sample_loc_data = {"translate_x":0,"translate_y":0, "translate_z":0, "rotate_x":0, "rotate_y":0, "rotate_z":0}
sample_search_metadata = {}

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

def angle_spacing(num_objecs = 5, min_angle = -135, max_angle = 135, min_spacing = 30):
    angles = []
    for i in range(0,num_objecs):
        angles.append(0)

    #check if squishing is needed:
    if num_objecs*min_spacing > (max_angle - min_angle):
        applied_spacing = (max_angle - min_angle) / num_objecs
    else:
        applied_spacing = min_spacing

    applied_angle_range = [-1 * (num_objecs * min_spacing)/2, (num_objecs * min_spacing)/2]
    # print("applied_angle_range = ",applied_angle_range)
    # if num_objecs // 2 == 0: #check if num_objects is even
    #     applied_spacing = min_spacing/2
    for i in range(0,num_objecs):
        angles[i] = applied_angle_range[0] + i * applied_spacing + applied_spacing/2 #small end of range plus the spacing times number applied.
    
    angles = [angle - 180 for angle in angles] #flip everything around because antz 0 deg is at 6 o'clock.

            
    return angles

def format_angles_to_loc_dict(angle_list):
    loc_list = []
    for angle in angle_list:
        
        new_loc = sample_loc_data.copy()
        new_loc['translate_x'] = angle
        loc_list.append(new_loc)
        
    
    return loc_list

def format_xyz_to_loc_dict(xy_list,height_list):
    loc_list = []
    for i in range(0,len(xy_list)):
        new_loc = sample_loc_data.copy()
        new_loc['translate_x'] = xy_list[i][0]
        new_loc['translate_y'] = xy_list[i][1]
        new_loc['translate_z'] = height_list[i]
        loc_list.append(new_loc)
    return loc_list

def generate_histoglyph_input(path_to_csvs,search_metadata = {"scaling_range": (0.0,1.5),
                                                              "scaling_type":"minmax"}):
    """
    generate_histoglyph_input generates the necessary data structures to construct a hyper-histoglyph.

    Args:
        path_to_csvs (string): absolute path to a directory containing CSVs

    Returns:
        List of list of list of float: all the data to make a histoglyph viz. If second level list has more than 1 element it creates 
        a hyper-histoglyph, which is a glyph of histo-glyphs
    """

    
    files = os.listdir(path_to_csvs)
    
    #get list of filepaths for each csv in the given directory
    list_csv_filepaths = []
    for file in files:
        if file.endswith('.csv'):
            list_csv_filepaths.append(path_to_csvs + "\\" + file)
    
    #open each file, verify that they have same num rows (also initialize histoglyph_list with empty lists = num rows)
    histoglyph_list_scaled = []
    histoglyph_list_unscaled = []
    histoglyph_list_normalized = []
    numrows = 0
    for line in open(list_csv_filepaths[0]):
        numrows = numrows + 1
        histoglyph_list_unscaled.append([])
        histoglyph_list_scaled.append([])
        histoglyph_list_normalized.append([])

    histoglyph_list_unscaled.pop(-1) #removing because my for loop included the header, which we won't use.
    histoglyph_list_scaled.pop(-1)
    histoglyph_list_normalized.pop(-1)

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
        scaled_data_array, unscaled_data_array, normalized_0_to1 = scaleFunc_forCSV(data_in_dict,search_metadata)

        for j in range(0,unscaled_data_array.shape[0]):
            normalized_row = normalized_0_to1[j,:]
            unscaled_row = unscaled_data_array[j,:]
            scaled_row = scaled_data_array[j,:]

            histoglyph_list_scaled[j].append(scaled_row.tolist())
            histoglyph_list_unscaled[j].append(unscaled_row.tolist())
            histoglyph_list_normalized[j].append(normalized_row.tolist())


    return histoglyph_list_scaled,histoglyph_list_unscaled,histoglyph_list_normalized,column_names_list

def apply_location_to_glyph(glyph, ind = 0, location_data = sample_loc_data):
    """
    apply_location_to_glyph applies positional data to a glyph to save space on the generate_single_histoglyph function.

    Args:
        glyph (dataframe): pandas dataframe that has the standard 94 columns of data for an ANTZ/GaiaViz save file.
        ind (int): the index of the glyph that you want to change in a multi-row dataframe.
        location_data (dict): dict of the form {"translate_x":0,"translate_y":0, "translate_z":0, "rotate_x":0, "rotate_y":0, "rotate_z":0}
                              that contains position where the glyph is supposed to be placed.

    Returns:
        glyph(dataframe): The same dataframe as give, except with the location data changed according to given location_data dict.
    """
    glyph.loc[glyph.index[ind],'translate_x'] = None
    glyph['translate_x'] = glyph['translate_x'].astype(float)
    glyph.loc[glyph.index[ind],'translate_x'] = location_data["translate_x"]

    glyph.loc[glyph.index[ind],'translate_y'] = None
    glyph['translate_y'] = glyph['translate_y'].astype(float)
    glyph.loc[glyph.index[ind],'translate_y'] = location_data["translate_y"]

    glyph.loc[glyph.index[ind],'translate_z'] = None
    glyph['translate_z'] = glyph['translate_z'].astype(float)
    glyph.loc[glyph.index[ind],'translate_z'] = location_data["translate_z"]

    glyph.loc[glyph.index[ind],'rotate_x'] = None
    glyph['rotate_x'] = glyph['rotate_x'].astype(float)
    glyph.loc[glyph.index[ind],'rotate_x'] = location_data["rotate_x"]

    glyph.loc[glyph.index[ind],'rotate_y'] = None
    glyph['rotate_y'] = glyph['rotate_y'].astype(float)
    glyph.loc[glyph.index[ind],'rotate_y'] = location_data["rotate_y"]

    glyph.loc[glyph.index[ind],'rotate_z'] = None
    glyph['rotate_z'] = glyph['rotate_z'].astype(float)
    glyph.loc[glyph.index[ind],'rotate_z'] = location_data["rotate_z"]

    return glyph

def generate_single_histoglyph(parent_id,last_used_id,glyph_data,tag_data,colormap,normalized_data, search_metadata = sample_search_metadata):
    """
    generate_single_glyph generates a snippet of an antzfile pertaining to a single histoglyph. Assumes 
    the header is generated elsewhere.

    Args:
        parent_id (int): the parent node that you want this glyph to sit on
        last_used_id(int): the starting point to assign new node ids from
        glyph_data (list of float): the unscaled data that will size the elements of the glyph
        tag_data (list of str): the 
        colormap(object): matplotlib colormap object
        normalized_data(list of float): data scaled on 0-1 for color selection purposes
        search_metadata (dict): search_metadata config dictionary used by glyphilator.py, and gui.py
    """
    cwd = os.getcwd()
    working_glyph_row_path = os.path.join(cwd,"resources","histo_glyph","data_bar.csv")
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
    for i in range(0,len(glyph_data)):

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

        #add color based on matplotlib color choice:
        rgba_list = colormap(normalized_data[i])
        rgba_list = [int((i*255)) for i in rgba_list]
        rgba_list = [float((i)) for i in rgba_list]
        working_row.loc[working_row.index[0],["color_r","color_g","color_b"]] = rgba_list[0:3]

        #Appending row to glyph
        working_glyph = pd.concat([working_glyph,working_row])
    
    #reset the index so I can properly find the rows i want later.
    working_glyph = working_glyph.reset_index(drop=True)
    
    last_used_id = node_id_counter
    
    return working_glyph, last_used_id

def create_viz(csv_dir_path,output_dir_path,search_metadata = {"scaling_range": (0.0,2.5),
                                                              "scaling_type":"minmax"}):

    output_node_file_path = os.path.join(output_dir_path,"node.csv")

    #pre-generating data/info for histoglyphs
    histoglyph_list_scaled,histoglyph_list_unscaled,histoglyph_list_normalized,column_names_list = generate_histoglyph_input(csv_dir_path,search_metadata)
    num_hyperhistoglyphs = len(histoglyph_list_scaled)
    num_histoglyphs_on_hyperhistoglyph = len(histoglyph_list_scaled[0])

    hyper_histoglyph_locations = generate_centered_grid(num_hyperhistoglyphs)
    hyper_histoglyph_heights = [0 for i in range(0,num_hyperhistoglyphs)]
    hyper_loc_dict_list = format_xyz_to_loc_dict(hyper_histoglyph_locations,hyper_histoglyph_heights)

    angles_list = angle_spacing(num_histoglyphs_on_hyperhistoglyph) 
    angles_loc_dict_list = format_angles_to_loc_dict(angles_list)

    colormap = mpl.colormaps['viridis'].resampled(99)
    
    #starting csv file generation
    antzfile = pd.read_csv(os.path.join(os.getcwd(),"resources","histo_glyph","glyph_header.csv"))

    parent_id = 40 #np_node_id of the plane object is 40. We want to drop all of our things on the plane.
    last_used_id = 40 
    plane_id = 40

    for i in range(0,num_hyperhistoglyphs):

        pin_and_ring = pd.read_csv(os.path.join(os.getcwd(),"resources","histo_glyph","hyperglyph_root_and_ring.csv"))

        #move the base of the hyper histoglyph to proper xyz position in world.
        pin_and_ring = apply_location_to_glyph(pin_and_ring,0,hyper_loc_dict_list[i])

        #change ids, parent ids of pin and ring to be appropriate
        pin_and_ring.loc[pin_and_ring.index[0],["parent_id"]] = plane_id #last used is currently the plane. likely need to save this id.
        last_used_id = last_used_id + 1
        pin_and_ring.loc[pin_and_ring.index[0],['np_node_id','np_data_id','record_id']] = last_used_id
        pin_and_ring.loc[pin_and_ring.index[1],["parent_id"]] = last_used_id
        last_used_id = last_used_id + 1
        pin_and_ring.loc[pin_and_ring.index[1],['np_node_id','np_data_id','record_id']] = last_used_id
        parent_id = last_used_id

        antzfile = pd.concat([antzfile,pin_and_ring])

        for j in range(0,num_histoglyphs_on_hyperhistoglyph):
            working_glyph,last_used_id = generate_single_histoglyph(parent_id,last_used_id,histoglyph_list_scaled[i][j],histoglyph_list_unscaled[i][j],colormap,histoglyph_list_normalized[i][j])
            working_glyph = apply_location_to_glyph(working_glyph,0,angles_loc_dict_list[j])
            antzfile = pd.concat([antzfile,working_glyph])

    antzfile.to_csv(output_node_file_path,index=False,encoding="utf-8")



