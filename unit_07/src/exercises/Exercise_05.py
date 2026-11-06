def load_grid(filename):

  with open(filename, "r") as f:
    grid = []
    for line in f:
      newLine = []
      for i in range(len(line.strip())):
        newLine.append(line[i])
      grid.append(newLine)
      
  return grid

def max_num_in_rows(grid, num_digits):
    biggestNumber = 0
    for i in range(len(grid)):
      for j in range(len(grid)):
        if int(''.join(grid[i][j:j+num_digits])) > biggestNumber:
          biggestNumber = int(''.join(grid[i][j:j+num_digits]))

    return biggestNumber

def max_num_adv(grid, num_digits):
  # biggestNumber = 0
  # gridWidth = len(grid)
  # for row in range(gridWidth):
    # for col in range(gridWidth):
      # if int(''.join(grid[row][col:row+num_digits])) > biggestNumber:
        # biggestNumber = int(''.join(grid[row][col:col+num_digits]))
      # if row+num_digits<gridWidth:
        # if int(''.join(grid[row][col:col+num_digits])) > biggestNumber:
          # biggestNumber = int(''.join(grid[row][col:col+num_digits]))
  # return biggestNumber
  pass #TODO: finish this function

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