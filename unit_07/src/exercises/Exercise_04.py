import string

def load_file(filename):
  pass

def count_letters(filename):


  chars = string.ascii_lowercase + string.ascii_uppercase
  

  words = load_file(filename)
  for i in range(48):
    words.contains(chars[i])

if __name__ == "__main__":
  count_letters("./src/exercises/Exercise_04_words.txt")