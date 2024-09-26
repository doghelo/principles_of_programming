print("Hello World")   #Outputs the words "Hello World"

while True:
    def the_squarer(number) :
        square = number*number
        return square

    maths = int(input("Enter a number to be squared:"))
    print(the_squarer(maths))

    word = input("Do you want to retry? (Y/N)")
    if word == "Y":
        True
    elif word == "N":
        break
    else:
        print("Invalid Answer, try again")
        word = input("Do you want to retry? (Y/N)")
