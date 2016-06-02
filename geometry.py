from shapely.geometry import Polygon
from shapely.geometry import Point

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
        camerasArray[i].disableCamera()
        if (isGalleryCovered(camerasArray)):
            indexArray.append(i)
        camerasArray[i].enabled = True
    return indexArray


def isGalleryCovered(camerasArray):
    return True