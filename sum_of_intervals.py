#https://www.codewars.com/kata/52b7ed099cdc285c300001cd/solutions/python

def sum_of_intervals(intervals):
    listy = []
    for i in intervals:
        for num in range(i[0], i[1]):
            listy.append(num)
    listy = set(listy)
    num = len(listy)
    return num
