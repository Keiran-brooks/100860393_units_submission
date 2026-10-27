def initials(*args):
    return '.'.join(args[0][0], args[1][0], args[][0])

    


if __name__ == "__main__":
    print(initials("James", "Marshall", "Hendrix"))  # should print the return value of "J.M.H"
    print(initials("John", "Ronald", "Reuel", "Tolkien"))  # should print the return value of "J.R.R.T"