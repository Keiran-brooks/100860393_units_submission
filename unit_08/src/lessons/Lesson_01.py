def is_palindrome(s):
    s = s.lower()
  
    reversedString = ''.join(reversed(s))
    if s == reversedString:
        return True

    return False




def filter_palindromes(items):
    newList = []
    for item in items:
      
      reversedString = ''.join(reversed(item))
      if item.lower() == reversedString.lower():
          # You could append both foward and reversed here since they are the same 
          newList.append(item)

    return newList



if __name__ == "__main__":
    # main program when decomposed
    str_list = ["ABBA", "snake", "Peep", "this"]
    pal_list = filter_palindromes(str_list)
    print(pal_list)  # prints ['ABBA', 'Peep']
