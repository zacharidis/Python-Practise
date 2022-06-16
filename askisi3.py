#by georgios zachariidis 

def sliceThemAll(word):
    wordlen = len(word)
    print(wordlen)
    list =  [char for char in word]
    return (list[1::2]);


#apisteuto to ti mporeis na kaneis me ta iterators tis python !!!!

inputWord = input("Please give me a word or phrase and magic will happen : ");

print(sliceThemAll(inputWord));
