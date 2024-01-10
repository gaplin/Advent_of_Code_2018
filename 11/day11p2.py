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
    result = grid[i + n - 1][ii + n - 1] - grid[i - 1][ii + n - 1] - grid[i + n - 1][ii - 1] + grid[i - 1][ii - 1]

    return result 

def fill_pref_sum(grid: int, n: int):
    for i in range(1, n):
        for ii in range(1, n):
            grid[i][ii] += grid[i - 1][ii] + grid[i][ii - 1] - grid[i - 1][ii - 1]

serial_number = int(open('input2.txt').read().strip())

n = 301
grid = [[0 for _ in range(n)] for _ in range(n)]
for i in range(1, n):
    for ii in range(1, n):
        grid[i][ii] = get_power_level(ii, i, serial_number)

fill_pref_sum(grid, n)

current_max = -1
current_cords = (-1, -1, -1)

for k in range(1, n):
    for i in range(1, n - k + 1):
        for ii in range(1, n - k + 1):
            square_value = power_level_of_square(i, ii, grid, k)
            if square_value > current_max:
                current_max = square_value
                current_cords = (ii, i, k)

print('{},{},{}'.format(*current_cords))
