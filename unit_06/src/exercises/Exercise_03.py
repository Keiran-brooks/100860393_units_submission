

def main():
    running = True
    numbers = []

    while running:
        userInput = input("Please enter the next number: ")
        
        if(userInput=='q' or len(numbers)>=9):
            if(not userInput=='q'):
                numbers.append(int(userInput)) 
            running = False

        else:
            numbers.append(int(userInput))

    if not len(numbers):
        print("No numbers entered.")
    else:
        numbers.reverse()
        print("The reverse of the numbers entered is:")
        for i in numbers:
            print(i)


# This is the entry point of the program
if __name__ == "__main__":
    main()  # call the main function