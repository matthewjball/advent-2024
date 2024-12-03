import re, math
input = open('input.txt', 'r').read()

matches = re.finditer('(mul\()\d+\,\d+\)', input, re.DOTALL)

results = 0

for match in matches:
    digits = re.finditer('\d+', match.group(), re.DOTALL)
    digits = [int(i.group()) for i in digits]
    results += math.prod(digits)
    
print(results)  