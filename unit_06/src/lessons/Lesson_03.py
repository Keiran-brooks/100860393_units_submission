def tuple_search(t, search_index):
    amount = 0
    firstIndex = 0
    for i in range(len(t)):
        itemToCheck = t[i]
        if itemToCheck == search_index:
            if amount == 0:
                firstIndex = i
            amount += 1 


    return (amount, firstIndex)
            

if __name__ == "__main__":
    # main code
    spaghetti_soup = ("a", "b", "g", "c", "a", "z", "g", "a", "g", "y")
    print(tuple_search(spaghetti_soup, "g")) # should print (3, 2)