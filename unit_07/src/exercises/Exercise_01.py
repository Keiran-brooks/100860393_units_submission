def count_words(filename):
    with open(filename, "r") as f:
        return len(f.read().split())

def main():
    print(count_words("./src/exercises/Exercise_01_example.txt"))  # should print 15

if __name__ == "__main__":
    
    main()