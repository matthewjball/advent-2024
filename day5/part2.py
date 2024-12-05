inputs = open('input.txt', 'r').read().split('\n\n')

rules = [tuple(i.split('|')) for i in inputs[0].split('\n')]
page_lines = [ i.split(',') for i in inputs[1].split('\n')]

def get_matching_rules(pages):
    temp_list = []
    for rule_l, rule_r in rules:
        if rule_l in pages and rule_r in pages:
            temp_list.append((rule_l, rule_r))
    return temp_list

def pages_match_rules(pages, rules):
    for rule_l, rule_r in rules:
        if pages.index(rule_l) > pages.index(rule_r):
            return False

    return True

def fix_page_order(pages, rules):
    temp_pages=[''] * len(pages)

    #order pages based on the number of times they occur on the left side of a rule. i.e No left-sides should come last.
    for page in pages:
        index = [l for l,r in rules].count(page)
        temp_pages[len(pages) - 1 - index] = page

    return temp_pages

middle_page_sum_p1 = 0
middle_page_sum_p2 = 0

for pages in page_lines:
    matching_rules = []
    matching_rules = get_matching_rules(pages)
    
    # int(pages[len(pages) // 2] gives middle index in a list with odd number of elements
    if pages_match_rules(pages, matching_rules):
        middle_page_sum_p1 += int(pages[len(pages) // 2])
    else:
        pages = fix_page_order(pages, matching_rules)
        middle_page_sum_p2 += int(pages[len(pages) // 2])

print(middle_page_sum_p1)
print(middle_page_sum_p2)
    