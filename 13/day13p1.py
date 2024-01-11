from heapq import heappop, heappush

rotations = {
    '/': lambda x, y: (-y, -x),
    "\\": lambda x, y: (y, x)
}

turns = [
    lambda x, y: (-y, x),
    lambda x, y: (x, y),
    lambda x, y: (y, -x)
]

grid = open('input2.txt').read().splitlines()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
n = len(grid)
m = len(grid[0])
for i in range(n):
    grid[i] = [x for x in grid[i]]

carts = [] # [i, ii, turn(0-2), di, dii]
for i in range(n):
    for ii in range(m):
        symbol = grid[i][ii]
        if symbol in '^>v<':
            carts.append([i, ii, 0, *directions['^>v<'.index(symbol)]])
            if symbol in '><':
                grid[i][ii] = '-'
            else:
                grid[i][ii] = '|'

moves_Q = []
for idx, cart in enumerate(carts):
    heappush(moves_Q, (cart[0], cart[1], idx))

def move(cart: list, grid: list, rotations: dict, turns: list) -> None:
    i, ii, turn_count, di, dii = cart
    symbol = grid[i][ii]
    if symbol in '|-':
        cart[0] += di
        cart[1] += dii
        return
    
    if symbol in '/\\':
        new_direction = rotations[symbol](di, dii)
    else:
        turn = turns[turn_count]
        turn_count = (turn_count + 1) % 3
        new_direction = turn(di, dii)
        cart[2] = turn_count

    cart[0] += new_direction[0]
    cart[1] += new_direction[1]
    cart[3], cart[4] = new_direction[0], new_direction[1]

def collision(carts: list, i: int, ii: int) -> bool:
    same_position_count = 0
    for cart in carts:
        if cart[0] == i and cart[1] == ii:
            same_position_count += 1
            if same_position_count == 2:
                return True
            
    return False

result = ()
while True:
    new_moves_Q = []
    while len(moves_Q) > 0:
        _, _, cart_id = heappop(moves_Q)
        cart = carts[cart_id]
        move(cart, grid, rotations, turns)
        if collision(carts, cart[0], cart[1]) == True:
            result = (cart[1], cart[0])
            break
        heappush(new_moves_Q, (cart[0], cart[1], cart_id))
    else:
        moves_Q = new_moves_Q
        continue
    break

print('{},{}'.format(*result))