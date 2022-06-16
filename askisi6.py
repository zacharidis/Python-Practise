#by georgios zachariidis 


def sliceEmAll(intArray , intSlicer):
    for num in intArray:
        if(int(num)%intSlicer==0):
            print(num)

sentence = input("Please enter the numbers seperated by a , ( comma ) :  ")
slicer = int(input("Please enter the number to slice the sentence : "))
intsentence = sentence.split(",")


sliceEmAll(intsentence,slicer);


