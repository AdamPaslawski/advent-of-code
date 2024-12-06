def read_file_to_report_list(f_name: str , max_lines = None):

    reports = []

    f = open(f_name, "r")

    for index, line in enumerate(f.readlines()):

        report = line.split(" ")
        report = [int(val.rstrip("\n")) for val in report]
        reports.append(report)

    return reports

def remove_ith_element(report: list[int], i:int):

    new_list = report[0:i] + report[i+1: len(report)]

    return new_list


def check_report(report: list[int], depth = 0):

    if depth > 1:
        return False


    if len(report) <= 1:
        return True

    increasing = report[1] - report[0]    

    if increasing == 0:
        if check_report(remove_ith_element(report, 0), depth + 1) or check_report(remove_ith_element(report, 1), depth + 1):
            return True
        return False
    else:
        increasing = increasing > 0

    for i in range(1 , len(report)):
        diff = report[i] - report[i-1]

        if abs(diff) > 3 or abs(diff) == 0:
            if check_report(remove_ith_element(report, i), depth + 1) or check_report(remove_ith_element(report, i-1), depth + 1) or check_report(remove_ith_element(report, 0), depth + 1):
                return True
            return False

        if increasing:
            if report[i] - report[i-1] < 0:
                if check_report(remove_ith_element(report, i), depth + 1) or check_report(remove_ith_element(report, i-1), depth + 1) or check_report(remove_ith_element(report, 0), depth + 1):
                    return True
                return False
        
        if not increasing:
            if report[i] - report[i-1] > 0:
                if check_report(remove_ith_element(report, i), depth + 1) or check_report(remove_ith_element(report, i-1), depth + 1) or check_report(remove_ith_element(report, 0), depth + 1):
                    return True
                return False
    return True


reports = read_file_to_report_list("input2.txt")
counter = 0
for report in reports:
    if check_report(report):
        #print(f"Report passed {report}")
        counter += 1
    else:
    #print(f"Report failed: {report}")
        pass

print(counter)

#assert check_report([7,6,4,2,1])
#assert not check_report([1,2,7,8,9])
#assert not check_report([0,0,0,0,0])
