import re, math, collections
input = open('input.txt', 'r').read()

matches = re.finditer('(mul\()\d+\,\d+\)', input, re.DOTALL)
enabled = re.finditer('(do\(\))', input, re.DOTALL)
disabled = re.finditer('don\'t\(\)', input, re.DOTALL)

ranges = {}

for match in enabled:
    ranges[match.span()] = True

for match in disabled:
    ranges[match.span()] = False

ranges[(0,0)] = True
ranges = collections.OrderedDict(sorted(ranges.items()))

def should_process_instruction(span):
    for prev_range, curr_range in zip(list(ranges.keys()), list(ranges.keys())[1:]):
        if span[0] >= prev_range[1] and span[0] <= curr_range[0]:
            return ranges[prev_range]


results_p1 = 0
results_p2 = 0

for match in matches:
    digits = re.finditer('\d+', match.group(), re.DOTALL)
    digits = [int(i.group()) for i in digits]
    results_p1 += math.prod(digits)

    if should_process_instruction(match.span()):
        results_p2 += math.prod(digits)
    
print(f"Part 1 : {results_p1}")
print(f"Part 2 : {results_p2}")