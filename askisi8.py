#by Georgios zacharidis


def reverseTheString(word):
    listA = word
    listB = [i for i in listA];
    listB.reverse();
    listC = ' '.join(listB);

    return listC

word = input("PLEASE ENTER A STRING AND PRESS ENTER : ")
print(reverseTheString(word))    