

def number_of_lines(filename):
  with open(filename) as test:
    print(test.lines())
    

def main():
  #Doesnt work on VSC due to running the python file inside of lessons folder and not unit root
  print(number_of_lines("./src/lessons/Lesson_03_example.txt"))  # prints 3
  print(number_of_lines("./src/lessons/Lesson_03_test.txt"))     # prints 25

if __name__ == "__main__":
  main()