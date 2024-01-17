import re
from heapq import heappop, heappush

class Group:
    def __init__(self, id, unit_type, units, HP_per_unit, AD, attack_type, initiative) -> None:
        self.id = id
        self.unit_type = unit_type
        self.units = units
        self.HP_per_unit = HP_per_unit
        self.AD = AD
        self.attack_type = attack_type
        self.initiative = initiative
        self.weaknesses = []
        self.immunes = []

    def __str__(self) -> str:
        return 'id: {}; type: {}; units: {}; HP: {}; AD: {}; Attack_type: {}; initiative: {}; Weak: {}; immune: {}'\
        .format(self.id, self.unit_type, self.units, self.HP_per_unit, self.AD, self.attack_type, self.initiative, self.weaknesses, self.immunes)
    
    def __repr__(self) -> str:
        return self.__str__()

def add_groups(army: dict, unit_type: int, lines: list, idx: int, n: int, id_start) -> tuple:
    while idx < n and lines[idx] != '':
        line = lines[idx]
        units, HP, AD, initiative = [int(x) for x in re.findall(r'[0-9-]+', line)]
        attack_type = re.findall(r'[a-z]+ damage', line)[0].split(' ')[0]
        group = Group(id_start, unit_type, units, HP, AD, attack_type, initiative)
        army[id_start] = group
        id_start += 1
        weaknesses = re.findall(r'weak to [^);]+', line)
        if weaknesses != []:
            weaknesses = weaknesses[0][8:].split(', ')
            for weakness in weaknesses:
                group.weaknesses.append(weakness)

        immunes = re.findall(r'immune to [^);]+', line)
        if immunes != []:
            immunes = immunes[0][10:].split(', ')
            for immune in immunes:
                group.immunes.append(immune)
        idx += 1
    return (idx, id_start)

def calculate_damage(source: Group, target: Group) -> int:
    if source.attack_type in target.immunes:
        return 0
    
    effective_power = source.units * source.AD
    if source.attack_type in target.weaknesses:
        return effective_power * 2

    return effective_power

def target_selection(groups: dict) -> list:
    result = []
    groups_Q = []
    for id, group in groups.items():
        effective_power = group.AD * group.units
        heappush(groups_Q, (-effective_power, -group.initiative, id))

    attacked_groups = set()
    while len(groups_Q) > 0:
        _, _, id = heappop(groups_Q)
        group = groups[id]
        target_type = 1 - group.unit_type
        targets = []
        for potential_target in groups.values():
            if potential_target.id in attacked_groups or potential_target.unit_type != target_type:
                continue
            dmg = calculate_damage(group, potential_target)
            if dmg == 0:
                continue
            target_effective_power = potential_target.units * potential_target.AD
            heappush(targets, (-dmg, -target_effective_power, -potential_target.initiative, potential_target.id))
        if targets == []:
            continue
        _, _, _, target_id = heappop(targets)
        result.append((id, target_id))
        attacked_groups.add(target_id)

    return result

def Two_armys(groups: dict) -> bool:
    occurs = [False, False]
    for group in groups.values():
        occurs[group.unit_type] = True
        if occurs[0] == True and occurs[1] == True:
            return True
        
    return False
    
def attack(groups: dict, attacks: list) -> None:
    attacks_with_order = []
    for source, target in attacks:
        attacks_with_order.append((groups[source].initiative, source, target))
    
    attacks_with_order.sort(key=lambda x: x[0], reverse=True)

    for _, source, target in attacks_with_order:
        if source not in groups:
            continue
        source_group = groups[source]
        target_group = groups[target]
        dmg = calculate_damage(source_group, target_group)
        units_to_remove = dmg // target_group.HP_per_unit
        target_group.units -= units_to_remove
        if target_group.units <= 0:
            del groups[target_group.id]

def play(groups: dict) -> None:
    while Two_armys(groups) == True:
        attacks = target_selection(groups)
        attack(groups, attacks)

input = open('input2.txt').read().splitlines()
n = len(input)

groups = {}
current_army = 0 # 0 Immune, 1 Infection
if input[0].startswith('Infection'):
    current_army = 1
i = 1
id = 0
i, id = add_groups(groups, current_army, input, i, n, id)
i += 2
current_army = 1 - current_army
_, _ = add_groups(groups, current_army, input, i, n, id)

play(groups)

result = 0
for group in groups.values():
    result += group.units

print(result)