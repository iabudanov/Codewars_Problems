#https://www.codewars.com/kata/where-my-anagrams-at
def anagrams(first_word, word_list):
    emptylist = []
    for word in word_list:
        if sorted(list(first_word)) == sorted(list(word)):
            emptylist.append(word)
            print('lol')
        else:
            print('ham')
            pass
    return emptylist


#https://www.codewars.com/kata/simple-pig-latin
def pig_it(text):
    emptylist = []
    for word in text.split():
        if (word == '.') or (word == '!') or (word == '?'):
            emptylist.append(word)
        else:
            word = list(word)
            word.append(word[0])
            del word[0]
            word.append('ay')
            word = ''.join(word)
            emptylist.append(word)
    result = ' '.join(emptylist)
    return result


#https://www.codewars.com/kata/530e15517bc88ac656000716
import string
from codecs import encode as _dont_use_this_
def rot13(message):
    dict = {'a':'n','b':'o','c':'p','d':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 
    'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m',
    'A':'N','B':'O','C':'P','D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 
    'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M', ' ':' ', '!':'!', 
    '.':'.', '?':'?', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '0':'0', '+':'+'}
    
    emptylist = []
    if len(message) == 0:
        return False
    else:
        for letter in message:
                emptylist.append(dict[letter])
    result = ''.join(emptylist)
    return result


#https://www.codewars.com/kata/525c65e51bf619685c000059
def cakes(recipe, available):
    if len(recipe) > len(available):
        return 0
    emptylist = []
    for ingredient in recipe:
        emptylist.append(available[ingredient]/recipe[ingredient])
    result = round(min(emptylist))
    return result


#https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
def zeros(n):
    sum = 0
    divisor_list = [5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125,
    9765625,  48828125, 244140625, 1220703125]
    for divisor in divisor_list:
	    sum += int(n/divisor)
    return sum


