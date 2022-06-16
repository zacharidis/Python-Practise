#by georgios zachariidis 

print("******************************************************")
print("Hello and Welcome to Python's most advanced calculator");
print("******************************************************");

def do_the_math(firstNum , secondNum):
    if (firstNum * secondNum < 1000):
        print( "The numbers will be multiplied ")
        return (firstNum*secondNum)
    else:
            print("The numbers will be added ")
            return (firstNum+secondNum);

numberOne = int(input("Please enter the first number "))
numberTwo = int(input("Please enter the second number"))

print(do_the_math(numberOne,numberTwo));

