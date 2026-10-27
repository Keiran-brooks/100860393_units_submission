import copy

def change_list(my_list):
    tempList = copy.copy(my_list)
    tempList.pop(1)
    tempList.append("Banana")
    tempList.sort()

    return tempList
    
    

if __name__ == "__main__":
    fruit_list = ["Pear", "Orange", "Peach", "Apple"]
    print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
    new_fruit_list = change_list(fruit_list)
    print(fruit_list) # prints ["Pear", "Orange", "Peach", "Apple"]
    print(new_fruit_list) # prints ["Apple", "Banana", "Peach", "Pear"]