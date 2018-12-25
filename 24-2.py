import copy

class Group:
    def __init__(self, name, count, hit_points, immune_set, weak_set, dmg, atk_type, initiative):
        self.name = name
        self.unit_count = count
        self.unit_hit_point = hit_points
        self.immune_to = immune_set
        self.weak_to = weak_set
        self.atk_dmg = dmg
        self.atk_type = atk_type
        self.initiative = initiative
        self.target = None
        self.is_target = False
        return

    def calculate_effective_power(self):
        return self.unit_count * self.atk_dmg

    def calculate_dmg(self, group):
        if group.immune_to is not None and self.atk_type in group.immune_to:
            return 0
        elif group.weak_to is not None and self.atk_type in group.weak_to:
            return self.calculate_effective_power() * 2
        else:
            return self.calculate_effective_power()

    def __repr__(self):
        return "{} {} units".format(self.name, self.unit_count)

immune_system = [
    # TEST
#     Group("Imn1", 17, 5390, None, {'radiation', 'bludgeoning'}, 4507, 'fire', 2),
#     Group("Imn2", 989, 1274, {'fire'}, {'bludgeoning', 'slashing'}, 25, 'slashing', 3),
    Group("Imn1", 4592, 2061, {'slashing', 'radiation'}, {'cold'}, 4, 'fire', 9),
    Group("Imn2", 1383, 3687, None, None, 26, 'radiation', 15),
    Group("Imn3", 2736, 6429, {'slashing'}, None, 20, 'slashing', 2),
    Group("Imn4", 777, 3708, {'radiation', 'cold'}, {'slashing', 'fire'}, 39, 'cold', 4),
    Group("Imn5", 6761, 2792, {'bludgeoning', 'fire', 'cold', 'slashing'}, None, 3, 'radiation', 17),
    Group("Imn6", 6028, 5537, {'slashing'}, None, 7, 'radiation', 6),
    Group("Imn7", 2412, 2787, None, None, 9, 'bludgeoning', 20),
    Group("Imn8", 6042, 7747, {'radiation'}, None, 12, 'slashing', 12),
    Group("Imn9", 1734, 7697, None, {'radiation', 'cold'}, 38, 'cold', 10),
    Group("Imn0", 4391, 3250, None, None, 7, 'cold', 19),
]

infection = [
    # TEST
#     Group("Inf1", 801, 4706, None, {'radiation'}, 116, 'bludgeoning', 1),
#     Group("Inf2", 4485, 2961, {'radiation'}, {'fire', 'cold'}, 12, 'slashing', 4),
    Group("Inf1", 820, 46229, {'cold', 'bludgeoning'}, None, 106, 'slashing', 18),
    Group("Inf2", 723, 30757, None, {'bludgeoning'}, 80, 'fire', 3),
    Group("Inf3", 2907, 51667, {'bludgeoning'}, {'slashing'}, 32, 'fire', 1),
    Group("Inf4", 2755, 49292, None, {'bludgeoning'}, 34, 'fire', 5),
    Group("Inf5", 5824, 24708, {'cold', 'bludgeoning', 'radiation', 'slashing'}, None, 7, 'bludgeoning', 11),
    Group("Inf6", 7501, 6943, {'slashing'}, {'cold'}, 1, 'radiation', 8),
    Group("Inf7", 573, 10367, None, {'cold', 'slashing'}, 30, 'radiation', 16),
    Group("Inf8", 84, 31020, None, {'cold'}, 639, 'slashing', 14),
    Group("Inf9", 2063, 31223, {'bludgeoning'}, {'radiation'}, 25, 'cold', 13),
    Group("Inf0", 214, 31088, None, {'fire'}, 271, 'slashing', 7)
]
#assert infection[0] == copy.deepcopy(infection[0])
def target_selection(attackers, defenders):
    attackers = sorted(attackers, key=lambda t: (t.calculate_effective_power(), t.initiative), reverse=True)
    for attacker in attackers:
        defenders.sort(key=lambda t: (attacker.calculate_dmg(t), t.calculate_effective_power(), t.initiative), reverse=True)
#        print(" | ".join(["{} {} {}".format(repr(t), t.is_target, attacker.calculate_dmg(t)) for t in defenders]))
        for t in defenders:
            if not t.is_target and attacker.calculate_dmg(t) > 0:
#                print('-->', attacker, t, attacker.calculate_dmg(t))
                t.is_target = True
                attacker.target = t
                break
    return

def remove_defeated(a):
    s = set([t for t in a if t.unit_count <= 0])
    for t in s:
        if t.target is not None:
            t.target.is_target = False
        a.remove(t)
    return a

boost = 0
while True:
    boost += 1
    if boost == 11:
        continue
    print('\nBOOST:', boost, '\n')
    before_imn = None
    immune_groups = copy.deepcopy(immune_system)
    for t in immune_groups:
        t.atk_dmg += boost
#        print(t, t.atk_dmg)
    before_inf = None
    infection_groups = copy.deepcopy(infection)
    while len(immune_groups) > 0 and len(infection_groups) > 0:
        target_selection(immune_groups, infection_groups)
        target_selection(infection_groups, immune_groups)
        if sum(t.is_target for t in immune_groups) == 0 and sum(t.is_target for t in infection_groups) == 0:
            break
        for attacker in sorted(immune_groups + infection_groups, key=lambda t: t.initiative, reverse=True):
            if attacker.target is not None and\
               attacker.target.unit_count > 0 and\
               attacker.unit_count > 0:
                target = attacker.target
                dmg = attacker.calculate_dmg(target)
#               print('\t', attacker.initiative, attacker, '|', dmg, '|', target, '|', dmg // target.unit_hit_point)
                target.unit_count -= dmg // target.unit_hit_point
                attacker.target = None
                target.is_target = False
        before_imn, before_inf, immune_groups, infection_groups = \
        copy.deepcopy(immune_groups),\
        copy.deepcopy(infection_groups),\
        remove_defeated(immune_groups),\
        remove_defeated(infection_groups)
        if before_imn == immune_groups  and before_inf == infection_groups:
            break
        #print(immune_groups)
        #print(infection_groups)
    if len(immune_groups) > 0 and len(infection_groups) == 0:
        break

print(sum(t.unit_count for t in immune_groups))

