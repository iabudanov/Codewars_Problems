#https://www.codewars.com/kata/51e0007c1f9378fa810002a9
def parse(data):
    value = 0
    empty_list = []
    for command in data:
        if command == "i":
            value += 1
        if command == "d":
            value -= 1
        if command == "s":
            value *= value
        if command == "o":
            empty_list.append(value)
    return empty_list


#https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq):
    emptylist = []
    for integer in seq:
        if seq.count(integer)%2 == 1:
            emptylist.append(integer)

    return emptylist[0]


#https://www.codewars.com/kata/52efefcbcdf57161d4000091
from collections import Counter as count


#https://www.codewars.com/users/afrostache123/completed_solutions
def count_smileys(arr):
    smileycount = 0
    for smiley in arr:
        if smiley in (':)', ':D',';)',';D',':-)',':~)',':-D',':~D',';-)',';-D',';~)',';~D'):
            smileycount += 1
    return smileycount


#https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
def solution(s):
    storagelist = []
    if len(s) %2 == 1:
        s = s + '_'
    count = 0
    while count < len(s):
        x = s[count]
        y = s[count + 1]
        strin = x + y
        storagelist.append(strin)
        count += 2
    return(storagelist)


#https://www.codewars.com/kata/5266876b8f4bf2da9b000362
def likes(names):
    num_ppl = len(names) 
    if num_ppl == 0:
        return('no one likes this')
    elif num_ppl == 1:
        return(names[0] + ' likes this')
    elif num_ppl == 2:
        return(names[0] + ' and ' + names[1] + ' like this')
    elif num_ppl == 3:
        return(names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this')
    elif num_ppl >= 4:
        return(names[0] + ', ' + names[1] + ' and ' + (str(len(names) - 2)) + ' others like this')


#https://www.codewars.com/kata/5526fc09a1bbd946250002dc
def find_outlier(numbers):
    odd = []
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        elif number % 2 == 1:
            odd.append(number)
    if len(odd) < len(even) and (len(odd) == 1):
        return(odd[0])
    elif len(even) < len(odd) and (len(even) == 1):
        return(even[0])  





