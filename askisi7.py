#by georgios zachariidis 

from re import A

def checkPalindrome(sentence):
    sentence = list(sentence);
    sentence2 = [i for i in sentence] #deepcopy 
    sentence2.reverse();

    if (sentence2 == sentence) : 
        return "PALINDROME"
    else:
         return "not a palindrome"

  



word = input("PLEASE ENTER A STRING TO BE CHECKED FOR BEING A PALINDROME:   ");
print(checkPalindrome(word))