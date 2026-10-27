def write_nums(n):
  with open("Lesson_04_nums.txt", "w") as file:
    for i in range(1, n+1):
      file.write(str(i)+'\n')


if __name__ == "__main__":
  write_nums(10) 
  # writes out the first 10 positive numbers to nums.txt