from shapely.geometry import Polygon
from shapely.geometry import Point
from shapely.ops import cascaded_union

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

class Gallery:
    gallery_polygon = None
    cameras = None
    camerasAmount = 0

def get_cameras_array(cameras_coordinates,radius):
    cameras = []
    for (i, coordinate) in enumerate(cameras_coordinates):
        camera = Camera(coordinate, radius)
        cameras.append(camera)
    return cameras

def getIndexOfCamerasToTurnOff(camerasState,index):
    indexArray = []
    hScore = 0

    for (i, camera) in enumerate(camerasState):
        if camerasState[i]:
            camerasState[i] = False
            if i>index:
                galleryCovered = isGalleryCovered(camerasState)
                if galleryCovered:
                    hScore +=1
                    indexArray.append(i)
            camerasState[i] = True


    return (indexArray, hScore)

def isGalleryCovered(camerasState):
    circles_array=[]
    for (i, camera) in enumerate(camerasState):
        if(camerasState[i]):
            circles_array.append(Gallery.cameras[i].circle)
    circles_union=cascaded_union(circles_array)
    return (circles_union.intersection(Gallery.gallery_polygon)==Gallery.gallery_polygon)