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
            print(f'Index: {page_lines.index(pages)} \n\n {pages} : {rules} \n\n Fails on rule: {rule_l} {rule_r} \n\n')
            return False

    return True

middle_page_sum = 0

for pages in page_lines:
    matching_rules = []
    matching_rules = get_matching_rules(pages)
    
    if pages_match_rules(pages, matching_rules):
        middle_page_sum += int(pages[len(pages) // 2])

print(middle_page_sum)
    