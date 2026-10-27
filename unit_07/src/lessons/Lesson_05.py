import json

def load(filename):
  with open(filename) as file:
    json.dump(file)

if __name__ == "__main__":
  print(load("./src/lessons/Lesson_05_items.json"))
  