input = open(0).read().split()

def is_in_order(rules, update):
    for i, item in enumerate(update):
        if item not in rules:
            continue
        dependencies = rules[item]
        for d in dependencies:
            if d not in update:
                continue
            if update.index(d) > i:
                return False
    return True

def put_in_order(rules, update):
    for i, item in enumerate(update):
        if item not in rules:
            continue
        dependencies = rules[item]
        for d in dependencies:
            if d not in update:
                continue
            where = update.index(d)
            if where > i:
                update[where], update[i] = update[i], update[where]

# Build all the rule dependencies
# If a|b then the rules[b] set will contain a
raw_rules = [ entry.split('|') for entry in input if entry.find('|') != -1 ]
rules = {}
for raw_rule in raw_rules:
    a, b = int(raw_rule[0]), int(raw_rule[1])
    if b in rules:
        rules[b].add(a)
    else:
        rules[b] = {a}

middle_sum = 0
updates = [ list(map(int, entry.split(','))) for entry in input if entry.find(',') != -1 ]
for update in updates:
    if not is_in_order(rules, update):
        while not is_in_order(rules, update):
            put_in_order(rules, update)
        middle_sum += update[len(update) // 2]    

print(middle_sum)