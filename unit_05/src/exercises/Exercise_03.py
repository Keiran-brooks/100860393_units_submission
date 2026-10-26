def num_digits(num):
    return len(str(num))

def main():
    i = input("Please enter a positive whole number:")
    digits = num_digits(int(i))
    print(f"{i} has {digits} digits.")

# This is needed for the tests. This is now the first bit of code Python will run.
if __name__ == "__main__":
    main() # calls the main function
