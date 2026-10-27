def longest_word(string_list):

    #Made vague on purpose lol better solution string_list == []
    if not string_list:
        return None
    longestIndex = (0,0)
    longestSoFar = 0
    for outerindex in range(len(string_list)):
        
        for innerindex in range(len(string_list[outerindex])):
            
            if len(string_list[outerindex][innerindex]) > longestSoFar:
                longestSoFar = len(string_list[outerindex][innerindex])
                longestIndex = (outerindex, innerindex)

    return string_list[longestIndex[0]][longestIndex[1]]

  
def num_characters(string_list):
    total = 0
    for i in range(len(string_list)):
        for j in range(len(string_list[i])):
            total += len(string_list[i][j])

    return total
  
if __name__ == "__main__":
    test_string = [["Hello", "World"], ["You", "say", "you", "want", "a", "revolution"], ["It's", "fine", "to", "celebrate", "success", "but", "it", "is", "more", "important", "to", "heed", "the", "lessons", "of", "failure"]]
    test_string2 = [["Hello", "World"], ["Apple", "Pears"]]
    print(longest_word(test_string)) # should print revolution
    print(num_characters(test_string)) # should print 105
    print(longest_word(test_string2)) # should print hello
    print(num_characters(test_string2)) # should print 20