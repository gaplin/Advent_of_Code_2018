def get_power_level(x: int, y: int, serial_number: int) -> int:
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level //= 100
    power_level %= 10
    power_level -= 5

    return power_level

def power_level_of_square(i: int, ii: int, grid: list, n: int) -> int:
    result = 0
    for y in range(i, i + n):
        for x in range(ii, ii + n):
            result += grid[y][x]

    return result 

serial_number = int(open('input2.txt').read().strip())

n = 300
grid = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for ii in range(n):
        grid[i][ii] = get_power_level(ii + 1, i + 1, serial_number)


current_max = -1
current_cords = (-1, -1)
for i in range(n - 2):
    for ii in range(n - 2):
        square_value = power_level_of_square(i, ii, grid, 3)
        if square_value > current_max:
            current_max = square_value
            current_cords = (ii + 1, i + 1)

print('{},{}'.format(*current_cords))
