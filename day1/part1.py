lines = [i.strip('\n').split() for i in open('input.txt', 'r').readlines()]
left = sorted([int(i[0]) for i in lines])
right = sorted([int(i[1]) for i in lines])

total_distance = 0

for l, r in zip(left, right):
    total_distance += abs(l-r)

print(total_distance)