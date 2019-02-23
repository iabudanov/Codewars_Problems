#https://www.codewars.com/kata/523b4ff7adca849afe000035
def greet():
    return "hello world!"


#https://www.codewars.com/kata/50654ddff44f800200000004
def multiply(a, b):
  return a * b


#https://www.codewars.com/kata/5aa736a455f906981800360d
def feast(beast, dish):
    return(beast[0] == dish[0]) and (beast[-1] == dish[-1])


#https://www.codewars.com/kata/568dcc3c7f12767a62000038
def set_alarm(employed, vacation):
    if (employed, vacation) == (True, True):
        return False
    if (employed, vacation) == (False, True):
        return False
    if (employed, vacation) == (False, False):
        return False
    else:
        return True


#https://www.codewars.com/kata/53af2b8861023f1d88000832
def areYouPlayingBanjo(name):
    if name[0] == "r" or name[0] == "R":
        return(name + " plays banjo")
    else:
        return(name + " does not play banjo")


#https://www.codewars.com/kata/595970246c9b8fa0a8000086
def capitalizeWord(word):
    wordlist = list(word)
    letterone = wordlist[0]
    wordlist[0] = letterone.upper()
    result = "".join(wordlist)
    return result


#https://www.codewars.com/kata/55d24f55d7dd296eb9000030
def summation(num):
    hi = 0
    for i in range(0, num+1):
        hi += i
    return hi







