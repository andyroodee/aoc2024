import re

input = ''.join(open("input.txt").readlines())
pattern = re.compile(r'mul\(((\d{1,3}),(\d{1,3}))\)')
sum = 0
do_string = "do()"
dont_string = "don't()"

# cut out the don't() parts
while True:
    dont = input.find(dont_string)
    if dont == -1:
        break
    do = input.find(do_string, dont)
    if do != -1:
        input = input[:dont] + input[do+len(do_string):]

for match in pattern.findall(input):
    product = int(match[1]) * int(match[2])
    sum += product

print(sum)
