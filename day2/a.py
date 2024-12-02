def is_safe_report(vals):
    inc = vals[0] < vals[1]
    for i in range(len(vals) - 1):
        diff = vals[i+1] - vals[i]
        valid_diff = abs(diff) >= 1 and abs(diff) <= 3
        seq = inc and diff > 0 or not inc and diff < 0
        if not valid_diff or not seq:
            return False
    return True

lines = open("input.txt").readlines()

safe_count = 0
for report in lines:
    vals = [ int(val) for val in report.split() ]
    if is_safe_report(vals):
        safe_count += 1

print(safe_count)
