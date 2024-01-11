num_of_recipies = int(open('input2.txt').read().strip())

all_recipies = [3, 7]

player_1, player_2 = 0, 1

while len(all_recipies) < num_of_recipies + 10:
    players_sum = all_recipies[player_1] + all_recipies[player_2]
    recipies_to_insert = [players_sum % 10]
    if players_sum >= 10:
        players_sum //= 10
        recipies_to_insert.append(players_sum)
    while len(recipies_to_insert) > 0:
        all_recipies.append(recipies_to_insert.pop())
    
    n = len(all_recipies)
    player_1 = (player_1 + 1  + all_recipies[player_1]) % n
    player_2 = (player_2 + 1 + all_recipies[player_2]) % n

result = ''.join([str(x) for x in all_recipies[num_of_recipies:num_of_recipies + 10]])
print(result)