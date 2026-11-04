import json

def load(filename):
  with open(filename) as file:
    return json.load(file)


if __name__ == "__main__":
  print(load("./src/lessons/Lesson_05_items.json"))
  