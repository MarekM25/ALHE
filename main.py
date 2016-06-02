'''
input.txt structure:

radius net_density
x1  y1
x2  y2
... ...
xn  yn
'''

from shapely.geometry import Polygon
import geometry
import codecs
import a_star
import sys

def read_data_from_file():
    with open(sys.argv[1]) as file:
        radius, net_density = [float(x) for x in next(file).split()]
        gallery_coordinates = [[float(x) for x in line.split()] for line in file]
    return radius, net_density, gallery_coordinates

def print_results(cameras,node):
    output = codecs.open(sys.argv[2], 'w', "utf-8")
    print("LISTA WSZYSTKICH DOSTĘPNYCH KAMER: ")
    output.write("LISTA WSZYSTKICH DOSTĘPNYCH KAMER: \n")
    print_cameras_coordinates(cameras,output)
    print("\nKAMERY, KTÓRE NALEŻY WŁĄCZYĆ: ")
    output.write("\nKAMERY, KTÓRE NALEŻY WŁĄCZYĆ: \n")
    print_cameras_to_turn_on(node, output)

def print_cameras_coordinates(cameras,output):
    for (i, camera) in enumerate(cameras):
        output.write("Kamera nr {} o współrzędnych {}\n".format(i,camera.point))
        print("Kamera nr {} o współrzędnych {}".format(i,camera.point))

def print_cameras_to_turn_on(node, output):
    counter=0
    for (i, camera) in enumerate(node.cameras):
        if (camera.enabled == True):
            counter=counter+1
            output.write("Kamera nr {} o współrzędnych {}\n".format(i,camera.point))
            print("Kamera nr {} o współrzędnych {}".format(i,camera.point))
    output.write("\nMINIMALNA LICZBA KAMER DO POKYCIA OBSZARU: {}".format(counter))
    print("\nMINIMALNA LICZBA KAMER DO POKYCIA OBSZARU: {}".format(counter))

def main():
    radius, net_density, gallery_coordinates = read_data_from_file()
    gallery_polygon = Polygon(gallery_coordinates)
    cameras_coordinates=geometry.get_cameras_coordinates(net_density, gallery_coordinates)
    cameras = geometry.get_cameras_array(cameras_coordinates,radius)
    node = a_star.aStar(cameras, gallery_polygon)
    print_results(cameras,node)

if __name__ == "__main__":
    main()
