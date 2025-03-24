import requests
import numpy as np
import os
from geopy.distance import geodesic,great_circle

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

def coord2proj(coord):
    lat = coord[0]
    long = coord[1]
    R = 6378137
    X = R * np.radians(long)
    Y = R * np.log(np.tan(np.pi / 4 + np.radians(lat) / 2))
    return (X,Y)

def proj2coord(point):
    X = point[0]
    Y = point[1]
    R = 6378137

    D = -Y/R
    lat = np.degrees(np.pi/2 - 2*np.atan(np.e**D))
    long = np.degrees(X / R)
    return (lat,long)



def fetchMapImage(latitudes,longitudes,buffer = 0.1, api_key = ""):
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
    # print("minlat,maxlat,minlong,maxlong = ", (minLong,maxLong,minLat,maxLat))
    (minLatProj,minLongProj) = coord2proj((minLat,minLong))
    (maxLatProj,maxLongProj) = coord2proj((maxLat,maxLong))

    latdistance = maxLatProj - minLatProj
    longdistance = maxLongProj - minLongProj

    latPadAmt = latdistance * buffer
    longPadAmt = longdistance * buffer

    minLatProj = minLatProj - latPadAmt
    maxLatProj = maxLatProj + latPadAmt
    minLongProj = minLongProj - longPadAmt
    maxLongProj = maxLongProj + longPadAmt

    latdistance = maxLatProj - minLatProj
    longdistance = maxLongProj - minLongProj
    
    print("(longdistance,latdistance) = ", (longdistance,latdistance))

    centerLatProj = (minLatProj + maxLatProj) / 2
    centerLongProj = (minLongProj + maxLongProj) / 2

    if latdistance > longdistance:
        print("latdistance is greater!")

        minLongProj = centerLongProj - latdistance/2
        maxLongProj = centerLongProj + latdistance/2


    if longdistance > latdistance:
        print("longdistance is greater!")
        
        minLatProj = centerLatProj - longdistance/2
        maxLatProj = centerLatProj + longdistance/2

        # maxLat = midpoint + (longdistance/2)
    # print("midpoint =", midpoint)
    # print("new minlat,maxlat,minlong,maxlong = ", (minLong,maxLong,minLat,maxLat))
    print("new longdistance,latdistance = ",maxLongProj - minLongProj,maxLatProj - minLatProj,)

    # latPadAmt = latdistance * buffer
    # longPadAmt = longdistance * buffer
    # aspectRatio = longdistance/latdistance

    # minLatProj = minLatProj - latPadAmt
    # maxLatProj = maxLatProj + latPadAmt
    # minLongProj = minLongProj - longPadAmt
    # maxLongProj = maxLongProj + longPadAmt
    # buffer_km = max(latdistance, longdistance) * buffer
    # minLat = great_circle(kilometers=buffer_km).destination((minLat, centerLong), 180).latitude
    # maxLat = great_circle(kilometers=buffer_km).destination((maxLat, centerLong), 0).latitude
    # minLong = great_circle(kilometers=buffer_km).destination((centerLat, minLong), 270).longitude
    # maxLong = great_circle(kilometers=buffer_km).destination((centerLat, maxLong), 90).longitude

    (minLat,minLong) = proj2coord((minLatProj,minLongProj))
    (maxLat,maxLong) = proj2coord((maxLatProj,maxLongProj))
    if minLat < -85.05:
        minLat = -85.05
    if maxLat > 85.05:
        maxLat = 85.05
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
    request_url = r"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/" + cornerstring + str([float(minLong),float(minLat),float(maxLong),float(maxLat)]) + "/" + str(int(requestedResolution[0])) + "x" + str(int(requestedResolution[1])) + "@2x?access_token=" + str(api_key)
    
    print("request url = \n",request_url)
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


# us_cities_coordinates = [
#     (40.7128, -74.0060),  # New York, NY
#     (34.0522, -118.2437), # Los Angeles, CA
#     (41.8781, -87.6298),  # Chicago, IL
#     (29.7604, -95.3698),  # Houston, TX
#     (33.4484, -112.0740), # Phoenix, AZ
#     (39.9526, -75.1652),  # Philadelphia, PA
#     (29.4241, -98.4936),  # San Antonio, TX
#     (32.7157, -117.1611), # San Diego, CA
#     (37.7749, -122.4194), # San Francisco, CA
#     (47.6062, -122.3321)  # Seattle, WA
# ]


# us_cities_coordinates_array = np.array(us_cities_coordinates)
# latitudes = us_cities_coordinates_array[:,0]
# longitudes = us_cities_coordinates_array[:,1]
# api_key = r"pk.eyJ1IjoiYWdsaXNrZSIsImEiOiJjbTg1MGl4Z3MxNGo5MmxvcHozdnVtNHY5In0.CFl_aEsMkieHZOR5_rKv4w"

# request_url, [minLong,maxLong,minLat,maxLat] = fetchMapImage(latitudes=latitudes,longitudes=longitudes,buffer=0.1,api_key=api_key)
# print("hello")
# print(request_url)
