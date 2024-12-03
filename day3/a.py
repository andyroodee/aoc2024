import re

input = ''.join(open("input.txt").readlines())
pattern = re.compile(r'mul\(((\d{1,3}),(\d{1,3}))\)')
sum = 0
for match in pattern.findall(input):
    product = int(match[1]) * int(match[2])
    sum += product

print(sum)
