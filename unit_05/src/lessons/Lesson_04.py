def print_list(listOfNumbers, multiple=1):
    for i in range(len(listOfNumbers)):
        print(listOfNumbers[i]*multiple)


if __name__ == "__main__":
    print_list([4,1,6,7], multiple = 2)
    print_list([4,1,6,7], multiple = 3)
    print_list([4,1,6,7])