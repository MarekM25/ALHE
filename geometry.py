from shapely.geometry import Polygon
from shapely.geometry import Point
from shapely.ops import cascaded_union

import time

def get_cameras_coordinates(net_density, gallery_coordinates):
    min_x, max_x, min_y, max_y = get_extremes_from_coordinates(gallery_coordinates)
    gallery_polygon=Polygon(gallery_coordinates)
    cameras_coordinates=[]
    step=1.0/net_density
    current_y=min_y
    while(current_y<max_y):
        current_x=min_x
        while(current_x<max_x):
            point=Point(current_x,current_y)
            if(point.within(gallery_polygon)):
                cameras_coordinates.append(point)
            current_x+=step
        current_y+=step
    return cameras_coordinates

def get_extremes_from_coordinates(gallery_coordinates):
    min_x=gallery_coordinates[0][0]
    max_x=gallery_coordinates[0][0]
    min_y=gallery_coordinates[0][1]
    max_y=gallery_coordinates[0][1]
    for i in range(1,len(gallery_coordinates)):
        if gallery_coordinates[i][0] < min_x:
            min_x=gallery_coordinates[i][0]
        if gallery_coordinates[i][0] > max_x:
            max_x=gallery_coordinates[i][0]
        if gallery_coordinates[i][1] < min_y:
            min_y = gallery_coordinates[i][1]
        if gallery_coordinates[i][1] > max_y:
            max_y = gallery_coordinates[i][1]
    return min_x,max_x,min_y,max_y

class Camera:
    def __init__(self,point,radius):
        self.point=point
        self.radius=radius
        self.enabled=True
        self.circle=point.buffer(radius)
    def disableCamera(self):
        self.enabled=False

def get_cameras_array(cameras_coordinates,radius):
    cameras = []
    for (i, coordinate) in enumerate(cameras_coordinates):
        camera = Camera(coordinate, radius)
        cameras.append(camera)
    return cameras

def getIndexOfCamerasToTurnOff(camerasArray, gallery_polygon,index):
    indexArray = []
    hScore = 0

    for (i, camera) in enumerate(camerasArray):
        if camera.enabled == True:
            camera.disableCamera()
            if i>index:
                start = time.time()
                galleryCovered = isGalleryCovered(camerasArray,gallery_polygon)
                end = time.time()
                a_star_time = end - start
                print(a_star_time)
                if galleryCovered:
                    hScore +=1
                    indexArray.append(i)
            camera.enabled = True


    return (indexArray, hScore)

def isGalleryCovered(camerasArray, gallery_polygon):
    circles_array=[]
    for (i, camera) in enumerate(camerasArray):
        if(camera.enabled):
            circles_array.append(camera.circle)
    circles_union=cascaded_union(circles_array)
    return (circles_union.intersection(gallery_polygon)==gallery_polygon)