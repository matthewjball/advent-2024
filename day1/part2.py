lines = [i.strip('\n').split() for i in open('input.txt', 'r').readlines()]
left = sorted([int(i[0]) for i in lines])
right = sorted([int(i[1]) for i in lines])

total_similarity = 0

for l in left:
    total_similarity += l * right.count(l)

print(total_similarity)