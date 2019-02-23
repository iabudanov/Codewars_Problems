#https://www.codewars.com/kata/585a1a227cb58d8d740001c3
def repeater(string, n):
    return string * n


#https://www.codewars.com/kata/5b39e3772ae7545f650000fc
def remove_duplicate_words(s):
    listy = s.split()
    emptylist = []
    for word in listy:
        if word in emptylist:
            pass
        else:
            emptylist.append(word)
    return " ".join(emptylist)


#https://www.codewars.com/kata/55f2b110f61eb01779000053
def get_sum(a,b):
    if a == b:
        return a
    if a < b:
        listy = range(a, b+1)
    else:
        listy = range(a, b-1, -1)
    return sum(listy)
print(get_sum(0, 1))


#https://www.codewars.com/kata/56b7251b81290caf76000978
def get_last_digit(index):
    a, b = 1, 1
    for x in range(index-1):
        a, b = a+b, a
    return(int(str(b)[-1]))


#https://www.codewars.com/kata/56541980fa08ab47a0000040
def printer_error(s):
    totall = 0
    for letter in s:
        if letter > 'm':
            totall +=1
    return( str(totall) + "/" + str(len(s)))
