'''
input.txt structure:

radius net_density
x1  y1
x2  y2
... ...
xn  yn
'''

from shapely.geometry import Polygon
from shapely.geometry import Point
import geometry
import a_star


def read_data_from_file():
    with open('input.txt') as file:
        radius, net_density = [float(x) for x in next(file).split()]
        gallery_coordinates = [[float(x) for x in line.split()] for line in file]
    return radius, net_density, gallery_coordinates


#def isGalleryCovered()

def main():
    radius, net_density, gallery_coordinates = read_data_from_file()
    gallery_polygon = Polygon(gallery_coordinates)
    cameras_coordinates=geometry.get_cameras_coordinates(net_density, gallery_coordinates)
    geometry.testCameraClass(cameras_coordinates,radius)
    print("Pole całkowite galerii: {}".format(gallery_polygon.area))
    a_star.aStar()

if __name__ == "__main__":
    main()
