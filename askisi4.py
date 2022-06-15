#Python is fun 
#i can see why people get obsessed with this language. 
#askisi4 


def stringModifier(word , charcounter):
    wordlen = len(word);
    
    
    
    if(charcounter >= wordlen): 
        return word
    else: 
         
         mix = word[charcounter:]
         print(mix)
         return mix


word = input("Please enter a string or a phrase or the story of your life:  ")
counter = int(input("and now enter a positive integer :  "))
print(stringModifier(word,counter))


