reports = [i.strip('\n').split() for i in open('input.txt', 'r').readlines()]

def is_report_safe(report):
    report = list(map(int, report))

    #throw away lists not in ascending or descending order
    if not((report == sorted(report)) or (report == list(reversed(sorted(report))))):
        return False

    #check distance between elements
    for current, next in zip(report[:-1], report[1:]):
        if not(1 <= abs(current - next) <= 3):
            return False
        continue

    #print(f"Found valid report {report}")
    return True


safe_reports = []

for report in reports:
    if is_report_safe(report):
        safe_reports.append(report)

print(len(safe_reports))
