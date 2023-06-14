#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) <= 0:
        return 0
    else:
        sum = 0
        div = 0
        for row in my_list:
            sum += row[0] * row[1]
            for i in range(len(row)):
                if i == 1:
                    div += float(row[i])
                    break
        return sum / div
