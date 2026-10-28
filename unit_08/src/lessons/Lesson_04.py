from tracer import trace

@trace
def string_list_concat(string_list):
  """ Concatenates a list of strings into a single string
  eg. ["This", "is", "a", "list", "of", "strings"] 
  returns
  "Thisisalistofstrings"
  """
  if len(string_list) == 1:
    return string_list[0]

  return string_list[0] + string_list_concat(string_list[1:])

@trace
def string_list_concat_with_space(string_list):
  """ Concatenates a list of strings into a single string
  eg. ["This", "is", "a", "list", "of", "strings"] 
  returns
  "This is a list of strings"
  """
  if len(string_list) == 1:
      return string_list[0]
  
  return string_list[0] + ' '  + string_list_concat_with_space(string_list[1:])

if __name__ == "__main__":
  str_list = ["This", "is", "a", "list", "of", "strings"]
  print(string_list_concat(str_list)) # prints the return value of "Thisisalistofstrings"
  print(string_list_concat_with_space(str_list)) # prints the return value of "This is a list of strings"