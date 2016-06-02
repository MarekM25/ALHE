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

def testCameraClass(cameras_coordinates,radius):
    camera = Camera(cameras_coordinates[0], radius)
    print (camera.point)
    print (camera.radius)
    print (camera.enabled)
    print(camera.circle)
    camera.disableCamera()
    print(camera.enabled)

def getIndexOfCamerasToTurnOff(camerasArray):
    indexArray = []
    for (i, camera) in enumerate(camerasArray):
        if camerasArray[i].enabled == True:
            camerasArray[i].disableCamera()
            if isGalleryCoveredMock(camerasArray,[]):
                indexArray.append(i)
            camerasArray[i].enabled = True
    return indexArray

def isGalleryCoveredMock(cameras,gallery):
    if cameras[1].enabled == True:
        return True
    if cameras[0].enabled == True and cameras[2].enabled == True:
        return True
    return False


def isGalleryCovered(camerasArray, gallery_polygon):
    circles_array=[]
    for (i, camera) in enumerate(camerasArray):
        if(camera.enabled):
            circles_array.append(camera.circle)
    circles_union=cascaded_union(circles_array)
    return (circles_union.intersection(gallery_polygon)==gallery_polygon)
