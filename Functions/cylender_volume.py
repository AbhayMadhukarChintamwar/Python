def find_Cylender_volume(radius, height):
    print('radius:', radius)
    print('height:', height)
    volume = 3.14 * (radius ** 2) * height
    return volume



r = 10
h = 7
v = find_Cylender_volume(r, h)
print("Volume of the cylinder:", v)