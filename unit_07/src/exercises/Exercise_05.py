def load_grid(filename):

  with open(filename, "r") as f:
    grid = []
    for line in f:
      newLine = []
      for i in range(len(line.strip())):
        newLine.append(int(line[i]))
      grid.append(newLine)
      
  return grid

def max_num_in_rows(grid, num_digits):
    biggestNumber = 0
    gridWidth = len(grid)
    for i in range(gridWidth):
      for j in range(gridWidth - num_digits + 1):
        currentNumber = 0
        for k in range(num_digits):
          currentNumber = currentNumber * 10 + grid[i][j + k]
        if currentNumber > biggestNumber:
          biggestNumber = currentNumber

    return biggestNumber

def max_num_adv(grid, num_digits):
  biggestNumber = 0
  gridWidth = len(grid)

  for row in range(gridWidth):
    for col in range(gridWidth):
      if col + num_digits <= gridWidth:
        currentNumber = 0
        for k in range(num_digits):
          currentNumber = currentNumber * 10 + grid[row][col + k]
        if currentNumber > biggestNumber:
          biggestNumber = currentNumber

      if row + num_digits <= gridWidth:
        currentNumber = 0
        for k in range(num_digits):
          currentNumber = currentNumber * 10 + grid[row + k][col]
        if currentNumber > biggestNumber:
          biggestNumber = currentNumber

      if row + num_digits <= gridWidth and col + num_digits <= gridWidth:
        currentNumber = 0
        for k in range(num_digits):
          currentNumber = currentNumber * 10 + grid[row + k][col + k]
        if currentNumber > biggestNumber:
          biggestNumber = currentNumber

      if row - num_digits + 1 >= 0 and col + num_digits <= gridWidth:
        currentNumber = 0
        for k in range(num_digits):
          currentNumber = currentNumber * 10 + grid[row - k][col + k]
        if currentNumber > biggestNumber:
          biggestNumber = currentNumber

  return biggestNumber

def print_grid(grid):
  for line in grid:
    for x in line:
      print(f"{x}  ", end="")
    print("\n")

if __name__ == "__main__":
  filename = "./src/exercises/Exercise_05_grid_5_by_5.txt"
  grid = load_grid(filename)
  print_grid(grid)  # print the grid
  print(max_num_in_rows(grid, 3))  # prints 912
  print(max_num_adv(grid, 3))  # prints 971