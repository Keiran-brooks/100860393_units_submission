def initials(*args):
    returnString = ''
    for inital in args:
        returnString += inital[0] + '.'

    return returnString[:-1]

    


if __name__ == "__main__":
    print(initials("James", "Marshall", "Hendrix"))  # should print the return value of "J.M.H"
    print(initials("John", "Ronald", "Reuel", "Tolkien"))  # should print the return value of "J.R.R.T"