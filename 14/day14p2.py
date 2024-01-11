target_recipie = [int(x) for x in open('input2.txt').read().strip()]

all_recipies = [3, 7]
N = len(target_recipie)
player_1, player_2 = 0, 1
current_match = 0
while True:
    players_sum = all_recipies[player_1] + all_recipies[player_2]
    recipies_to_insert = [players_sum % 10]
    if players_sum >= 10:
        players_sum //= 10
        recipies_to_insert.append(players_sum)
    while len(recipies_to_insert) > 0:
        new_num = recipies_to_insert.pop()
        all_recipies.append(new_num)
        if new_num == target_recipie[current_match]:
            current_match += 1
            if current_match == N - 1:
                result = len(all_recipies) - N + 1
                break
        elif new_num == target_recipie[0]:
            current_match = 1
        else:
            current_match = 0
    else:
        n = len(all_recipies)
        player_1 = (player_1 + 1  + all_recipies[player_1]) % n
        player_2 = (player_2 + 1 + all_recipies[player_2]) % n
        continue
    break

print(result)