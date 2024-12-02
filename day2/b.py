def sign(val):
    if val < 0:
        return -1
    elif val > 0:
        return 1
    else:
        return 0

def is_safe_report(diffs):
    dir = sign(diffs[0])
    for i in range(len(diffs)):
        valid_diff = abs(diffs[i]) >= 1 and abs(diffs[i]) <= 3
        seq = dir == sign(diffs[i])
        if not valid_diff or not seq:
            return False
    return True

def get_diffs(vals):
    diffs = []
    for i in range(len(vals) - 1):
        diffs.append(vals[i] - vals[i+1])
    return diffs

lines = open("input.txt").readlines()

safe_count = 0
for report in lines:
    vals = [ int(val) for val in report.split() ]
    diffs = get_diffs(vals)
    if is_safe_report(diffs):
        safe_count += 1
    else:
        # no-brain mode: just delete a single element and see if that makes the report safe
        for i in range(len(vals)):
            mod = vals[:]
            del mod[i]
            diffs = get_diffs(mod)
            if is_safe_report(diffs):
                safe_count += 1
                break

print(safe_count)
