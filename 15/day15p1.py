from heapq import heappop, heappush
from functools import cmp_to_key

class Player:
    def __init__(self, id, i, ii, symbol) -> None:
        self.HP = 200
        self.AP = 3
        self.id = id
        self.i = i
        self.ii = ii
        self.symbol = symbol

    def __str__(self) -> str:
        return 'HP: {}, AP: {}, Id: {}, I: {}, II: {}, Symbol: {}'.format(self.HP, self.AP, self.id, self.i, self.ii, self.symbol)
    
    def __repr__(self) -> str:
        return self.__str__()

grid = open('input2.txt').read().splitlines()

n = len(grid)
m = len(grid[0])
for i in range(n):
    grid[i] = [x for x in grid[i]]

id = 0
players = {}
players_positions = {}
moves_Q = []
for i in range(n):
    for ii in range(m):
        if grid[i][ii] in 'GE':
            player = Player(id, i, ii, grid[i][ii])
            players[id] = player
            players_positions[(i, ii)] = player
            heappush(moves_Q, (i, ii, id))
            id += 1
directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def try_to_attack(player: Player, players: dict, players_positions: dict, grid: list, directions: list) -> bool:
    enemy = 'G' if player.symbol == 'E' else 'E'
    possible_targets = []
    for di, dii in directions:
        new_i, new_ii = player.i + di, player.ii + dii
        if grid[new_i][new_ii] == enemy:
            possible_targets.append(players_positions[(new_i, new_ii)])

        
    if possible_targets == []:
        return False
    def targets_cmp(player1: Player, player2: Player) -> int:
        if player1.HP == player2.HP:
            if player1.i == player2.i:
                return player1.ii - player2.ii
            return player1.i - player2.i
        return player1.HP - player2.HP
    
    possible_targets.sort(key=cmp_to_key(targets_cmp))
    target = possible_targets[0]
    target.HP -= player.AP
    if target.HP <= 0:
        del players[target.id]
        del players_positions[(target.i, target.ii)]
        grid[target.i][target.ii] = '.'
    return True

def get_next_move(player: Player, grid: list, directions: list) -> tuple:
    enemy = 'G' if player.symbol == 'E' else 'E'
    Q = []
    n = len(grid)
    m = len(grid[0])
    visited = {(player.i, player.ii)}
    for di, dii in directions:
        new_i, new_ii = player.i + di, player.ii + dii
        if grid[new_i][new_ii] == '.':
            heappush(Q, (1, new_i, new_ii, (new_i, new_ii)))
            visited.add((new_i, new_ii))

    while len(Q) > 0:
        distance, i, ii, starting_position = heappop(Q)
        if grid[i][ii] == enemy:
            return starting_position
        
        for di, dii in directions:
            new_i, new_ii, new_distance = i + di, ii + dii, distance + 1
            if grid[i][ii] != '#' and grid[i][ii] != player.symbol and (new_i, new_ii) not in visited:
                visited.add((new_i, new_ii))
                heappush(Q, (new_distance, new_i, new_ii, starting_position))

    return None

def play(player: Player, players: dict, players_positions: dict, grid: list, n: int, m: int, directions: list) -> None:
    attacked = try_to_attack(player, players, players_positions, grid, directions)
    if attacked == True:
        return
    
    move = get_next_move(player, grid, directions)
    if move == None:
        return
    grid[player.i][player.ii] = '.'
    del players_positions[(player.i, player.ii)]
    player.i, player.ii = move[0], move[1]
    players_positions[move] = player
    grid[move[0]][move[1]] = player.symbol

    _ = try_to_attack(player, players, players_positions, grid, directions)

def count_types(players: dict) -> tuple:
    elves, goblins = 0, 0
    for player in players.values():
        if player.symbol == 'E':
            elves += 1
        else:
            goblins += 1

    return (elves, goblins)

rounds = 0
while True:
    new_moves_Q = []
    while len(moves_Q) > 0:
        _, _, player_id = heappop(moves_Q)
        if player_id not in players:
            continue
        all_types = count_types(players)
        if all_types[0] == 0 or all_types[1] == 0:
            break
        player = players[player_id]
        play(player, players, players_positions, grid, n, m, directions)
        heappush(new_moves_Q, (player.i, player.ii, player.id))
    else:
        rounds += 1
        moves_Q = new_moves_Q
        continue
    break

result = 0
for player in players.values():
    result += player.HP

result *= rounds
print(result)