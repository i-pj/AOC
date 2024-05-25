import re
input = []
with open("input.txt", "r") as file:
    for line in file:
         input.append(line.strip())
 #print(input)
# 
# test = "threerznlrhtkjp23mtflmbrzq395three"
# def get_num(st):
#     num = ""
#     for ch in st:
#         if ch.isdigit():
#             num += ch
#     return int(num[0] +num[-1])
# 
# s = 0
# for _ in input:
#    s += get_num(_)
# print(s)

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
   'six': '6',
   'seven': '7',
    'eight': '8',
    'nine': '9',
}

result = 0
for line in input:
    digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    value = ''.join([numbers[d] if d.isalpha() else d for d in [digits[0], digits[-1]]])
    result += int(value)

print(result)
