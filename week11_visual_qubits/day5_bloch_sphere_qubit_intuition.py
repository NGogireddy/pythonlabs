def apply_hadamard_to_coordinate(coordiantes):
    x, y, z = coordiantes
    return z, -y, x


coordinate_list = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

for coordinate in coordinate_list:
    print(f"H {coordinate}:{apply_hadamard_to_coordinate(coordinate)}")
