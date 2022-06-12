def printTheResult(repetitions):
    for i in range (0,repetitions) :
        print("Current number is : " + str(i))
        print("Previous number was :" + str(i-1))
        print("Sum of : " , str(i) , " and " , str(i-1) ," is : ", str(i+(i-1)))



numOfRepetitions = int(input("How many repetitions should i execute ? "));

printTheResult(numOfRepetitions)
