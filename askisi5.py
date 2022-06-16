#by georgios zachariidis 

from cmath import phase
from urllib.request import ProxyHandler


def checkTheIntegers(phrase):
    firstElement = (phrase[0])
    lastElement = (phrase[len(phrase)-1])
    if (firstElement==lastElement):
        return "ACCEPTED"
    else:
        return "NOT ACCEPTED"



print("PLEASE ENTER A SERIES OF INTEGERS SEPPERATED BY AN EMPTY SPACE AND PRESS ENTER  :  ");
phrase = input();
print(checkTheIntegers(phrase));

