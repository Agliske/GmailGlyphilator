import requests
import numpy as np
import os
from geopy.distance import geodesic

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
    print("minlat,maxlat,minlong,maxlong = ", (minLong,maxLong,minLat,maxLat))
    latdistance = geodesic((minLat, minLong), (maxLat, minLong)).km

    longdistance = geodesic((minLat, minLong), (minLat, maxLong)).km

    print("(latdistance,longdistance) = ", (latdistance,longdistance))

    centerLat = (minLat + maxLat) / 2
    centerLong = (minLong + maxLong) / 2

    if latdistance > longdistance:
        # midpoint = (minLong + maxLong)/2 #find midpoint on shorter side of bounding rectangle
        # longExpansion = (latdistance - longdistance) / 2
        # print("longExpansion = ",longExpansion)
        # minLong = midpoint - (latdistance/2)
        # maxLong = midpoint + (latdistance/2)
        minLong = geodesic(kilometers=latdistance/2).destination((centerLat, centerLong), 270).longitude
        maxLong = geodesic(kilometers=latdistance/2).destination((centerLat, centerLong), 90).longitude
  
    if longdistance > latdistance:
        # midpoint = (minLat + maxLat)/2
        # latExpansion = (longdistance - latdistance) / 2
        # print("latExapnsion = ", latExpansion)
        minLat = geodesic(kilometers=longdistance/2).destination((centerLat, centerLong), 180).latitude
        maxLat = geodesic(kilometers=longdistance/2).destination((centerLat, centerLong), 0).latitude
    
    # max_distance = max(latdistance, longdistance)

    # latExpansion = (max_distance - latdistance) / 2
    # longExpansion = (max_distance - longdistance) / 2

    # minLat = geodesic(kilometers=latExpansion).destination((centerLat, centerLong), 180).latitude
    # maxLat = geodesic(kilometers=latExpansion).destination((centerLat, centerLong), 0).latitude
    # minLong = geodesic(kilometers=longExpansion).destination((centerLat, centerLong), 270).longitude
    # maxLong = geodesic(kilometers=longExpansion).destination((centerLat, centerLong), 90).longitude

   # minLat = midpoint - (longdistance/2)
        # maxLat = midpoint + (longdistance/2)
    # print("midpoint =", midpoint)
    print("new minlat,maxlat,minlong,maxlong = ", (minLong,maxLong,minLat,maxLat))
    print("new longdistance,latdistance = ",(geodesic((minLat, (minLong + maxLong) / 2), (maxLat, (minLong + maxLong) / 2)).km,geodesic(((minLat + maxLat) / 2, minLong), ((minLat + maxLat) / 2, maxLong)).km))

    # latPadAmt = latdistance * buffer
    # longPadAmt = longdistance * buffer
    # aspectRatio = longdistance/latdistance

    # minLat = minLat - latPadAmt
    # maxLat = maxLat + latPadAmt
    # minLong = minLong - longPadAmt
    # maxLong = maxLong + longPadAmt
    buffer_km = max(latdistance, longdistance) * buffer
    minLat = geodesic(kilometers=buffer_km).destination((minLat, centerLong), 180).latitude
    maxLat = geodesic(kilometers=buffer_km).destination((maxLat, centerLong), 0).latitude
    minLong = geodesic(kilometers=buffer_km).destination((centerLat, minLong), 270).longitude
    maxLong = geodesic(kilometers=buffer_km).destination((centerLat, maxLong), 90).longitude

    # if latdistance >= longdistance:
    #     ratio = longdistance/latdistance
    #     requestedResolution = (1280,1280*ratio)
    
    # if longdistance > latdistance:
    #     ratio = latdistance/longdistance
    #     requestedResolution = (1280*ratio,1280)

    requestedResolution = (1280,1280)
    
    markerString = "pin-s+000(" + str(float(latitudes[0])) +","+ str(float(longitudes[0])) + ")"
    for i in range(1,latitudes.shape[0]):
        markerString = markerString + ",pin-s+000(" + str(float(longitudes[i])) + "," + str(float(latitudes[i])) + ")"

    cornerstring = "pin-s+000(" + str(float(minLong)) +","+ str(float(minLat)) + ")" + ",pin-s+000(" + str(float(minLong)) +","+ str(float(maxLat)) + ")" ",pin-s+000(" + str(float(maxLong)) +","+ str(float(minLat)) + ")"",pin-s+000(" + str(float(maxLong)) +","+ str(float(maxLat)) + ")"
    cornerstring = cornerstring + "/"
    markerString = markerString + "/"
    request_url = r"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/" + str([float(minLong),float(minLat),float(maxLong),float(maxLat)]) + "/" + str(int(requestedResolution[0])) + "x" + str(int(requestedResolution[1])) + "@2x?access_token=" + str(api_key)
    
    return request_url,[minLong,maxLong,minLat,maxLat]

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