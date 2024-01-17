import re
from heapq import heappop, heappush

def clamp(value, min_value, max_value) -> int:
    if value > max_value:
        return max_value
    elif value < min_value:
        return min_value
    else:
        return value

def distance(P1, P2) -> int:
    return abs(P1[0] - P2[0]) + abs(P1[1] - P2[1]) + abs(P1[2] - P2[2])

def closest_point_from_cube_to_point(cube, P) -> tuple:
    x = clamp(P[0], cube[0], cube[3])
    y = clamp(P[1], cube[1], cube[4])
    z = clamp(P[2], cube[2], cube[5])
    return (x, y, z)

def cube_circle_intersection(cube: list, circle: list) -> bool:
    circle_center = (circle[0], circle[1], circle[2])
    closest_to_center = closest_point_from_cube_to_point(cube, circle_center)
    distance_to_center = distance(closest_to_center, circle_center)
    return distance_to_center <= circle[3]

def get_sub_cubes(cube: list) -> list:
    half_x = (cube[0] + cube[3]) // 2
    half_y = (cube[1] + cube[4]) // 2
    half_z = (cube[2] + cube[5]) // 2
    result = []
    result.append((cube[0], cube[1], cube[2], half_x, half_y, half_z))

    result.append((half_x + 1, cube[1], cube[2], cube[3], half_y, half_z))
    result.append((cube[0], half_y + 1, cube[2], half_x, cube[4], half_z))
    result.append((cube[0], cube[1], half_z + 1, half_x, half_y, cube[5]))

    result.append((half_x + 1, half_y + 1, cube[2], cube[3], cube[4], half_z))
    result.append((half_x + 1, cube[1], half_z + 1, cube[3], half_y, cube[5]))
    result.append((cube[0], half_y + 1, half_z + 1, half_x, cube[4], cube[5]))
    
    result.append((half_x + 1, half_y + 1, half_z + 1, cube[3], cube[4], cube[5]))

    return result

input = open('input2.txt').read().splitlines()

nanobots = []
for line in input:
    x, y, z, r = [int(x) for x in re.findall(r'[0-9-]+', line)]
    nanobots.append((x, y, z, r))
n = len(nanobots)

max_x = max([abs(x[0]) - x[3] for x in nanobots])
max_y = max([abs(x[1]) - x[3] for x in nanobots])
max_z = max([abs(x[2]) - x[3] for x in nanobots])

max_dim = max([max_x, max_y, max_z])

edge_half = 1
while edge_half < max_dim:
    edge_half <<= 1

edge_size = edge_half << 1
current_cube = (-edge_half, -edge_half, -edge_half, edge_half - 1, edge_half - 1, edge_half - 1)

intersections = 0
for circle in nanobots:
    if cube_circle_intersection(current_cube, circle) == True:
        intersections += 1
assert intersections == n

current_max = None
max_points = []
Q = [(-n, current_cube)]
while len(Q) > 0:
    current_intersections, cube = heappop(Q)
    current_intersections *= -1
    if current_max != None and current_intersections < current_max:
        continue
    if cube[0] == cube[3] and cube[1] == cube[4] and cube[2] == cube[5]:
        current_max = current_intersections
        max_points.append((current_intersections, (cube[0], cube[1], cube[2])))
        continue
    
    sub_cubes = get_sub_cubes(cube)
    for cube in sub_cubes:
        intersections = 0
        for circle in nanobots:
            if cube_circle_intersection(cube, circle) == True:
                intersections += 1
        heappush(Q, (-intersections, cube))

result = 9999999999
max_points.sort(key=lambda x: x[0], reverse=True)
max_intersections = max_points[0][0]
for intersections, point in max_points:
    if intersections != max_intersections:
        break
    dist = distance(point, (0, 0, 0))
    result = min(dist, result)

print(result)