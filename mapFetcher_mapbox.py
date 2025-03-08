import requests
import numpy as np
import os

#steps
# 1.calculate max and min of my lat and long
# 2.add a 10% padding on either side of my lat and long, to get bounding box
# 3.calculate aspect ratio of bounding box
# 4.find the max resolution that fits in a width<1280,height<1280 box that matches the aspect ratio

# 4.1 find if latitude or longitude distance is larger, and make that one 1280.
# 4.2 calculate both lat/long and longover lat.
# 4.3 multiply the smaller fraction by 1280 to get the other one.
# 
# 5.make the request to api
# 6.return the image
latlonglist = [
    (51.5074, -0.1278),   # London
    (53.4808, -2.2426),   # Manchester
    (52.2053, 0.1218),    # Cambridge
    (51.4545, -2.5879),   # Bristol
    (54.9783, -1.6174)    # Newcastle upon Tyne
]

def fetchMapImage(latitudes,longitudes,buffer,api_key):
    """
    fetchMapImage returns a png image to the specified path

    Args:
        coordsList (list of 2-tuple): list of coordinates in Decimal Degrees (DD) in (latitude,longitude) format
        buffer (float): decimal buffer to apply to either side of area of interest. A value of 0.1 returns an map that extends 10% past points of interest
    """
    # coordsArray = np.array(coordsList)
    # latitudes = coordsArray[:,1] 
    # longitudes = coordsArray[:,0]

    minLat = np.min(latitudes)
    maxLat =  np.max(latitudes)
    minLong = np.min(longitudes)
    maxLong = np.max(longitudes)
    print("minlat,maxlat,minlong,maxlong = ", (minLat,maxLat,minLong,maxLong))
    latdistance = maxLat - minLat
    longdistance = maxLong - minLong
    print("(latdistance,longdistance) = ", (latdistance,longdistance))
    if latdistance > longdistance:
        midpoint = (minLong - maxLong)/2 #find midpoint on shorter side of bounding rectangle
        minLong = midpoint - (latdistance/2)
        maxLong = midpoint + (latdistance/2)
    if longdistance > latdistance:
        midpoint = (minLat - maxLat)/2
        minLat = midpoint - (longdistance/2)
        maxLat = midpoint + (longdistance/2)
    print("midpoint =", midpoint)
    print("new minlat,maxlat,minlong,maxlong = ", (minLat,maxLat,minLong,maxLong))
    print("new latdistance,longdistance = ",(maxLat - minLat,maxLong - minLong))

    latPadAmt = latdistance * buffer
    longPadAmt = longdistance * buffer
    aspectRatio = longdistance/latdistance

    minLat = minLat - latPadAmt
    maxLat = maxLat + latPadAmt
    minLong = minLong - longPadAmt
    maxLong = maxLong + longPadAmt

    # if latdistance >= longdistance:
    #     ratio = longdistance/latdistance
    #     requestedResolution = (1280,1280*ratio)
    
    # if longdistance > latdistance:
    #     ratio = latdistance/longdistance
    #     requestedResolution = (1280*ratio,1280)

    requestedResolution = (1280,1280)
    
    markerString = "pin-s+000(" + str(float(latitudes[0])) +","+ str(float(longitudes[0])) + ")"
    for i in range(1,latitudes.shape[0]):
        markerString = markerString + ",pin-s+000(" + str(float(latitudes[i])) + "," + str(float(longitudes[i])) + ")"

    
    markerString = markerString + "/"
    request_url = r"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/" + markerString + str([float(minLat),float(minLong),float(maxLat),float(maxLong)]) + "/" + str(int(requestedResolution[0])) + "x" + str(int(requestedResolution[1])) + "@2x?access_token=" + str(api_key)
    
    return request_url,[minLat,maxLat,minLong,maxLong]

def saveMap(request_url):
    cwd = os.getcwd()
    
    images_dir_path = os.path.join(cwd,"antz","antz","User","_Global_","images")
    fileCount = 1
    for entry in os.scandir(images_dir_path):
        if entry.is_file() == True:
            fileCount = fileCount + 1
        else: continue
    
    # print(fileCount)
    filename = os.path.join(cwd,"antz","antz","User","_Global_","images",str(fileCount) + "_geospacial_map.jpg")
    response = requests.get(request_url)
    with open(filename,"wb") as file:
        file.write(response.content)
    return fileCount #filecount is going to be our texture_id in-viz


# saveMap("hello","goodbye")
# mapbox_api_key = r"pk.eyJ1IjoiYWdsaXNrZSIsImEiOiJjbTd4eWkybzEwNDN3MmpwbzE3MW04eTFoIn0.nbkkTpDhyG4WcG5xf-Sr0A"
# url,cornerCoords = fetchMapImage(latlonglist,0.1,api_key=mapbox_api_key)
# filecount = saveMap(url)
# print(url)