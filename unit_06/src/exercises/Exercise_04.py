def main():
    notFinished = True
    amount = int(input("Please enter the amount inserted (1 to 100):\n"))
    if amount > 100 or amount < 1:
        print("Invalid amount")
        return
    cost = int(input("Please enter the cost of the item:\n"))
    change = amount-cost
    if change < 0:
        print("Item costs more than amount inserted")
        return
    fiftyCoins, twentyCoins, tenCoins, fiveCoins, twoCoins, oneCoins = (0,)*6
    #HOLY SH*T THIS CODE FINNA STINK

    while notFinished:
        if change-50 >= 0:
            change -= 50
            fiftyCoins += 1
        elif change-20 >= 0:
            change -= 20
            twentyCoins += 1
        elif change-10 >= 0:
            change -= 10
            tenCoins += 1
        elif change-5 >= 0:
            change -= 5
            fiveCoins += 1
        elif change - 2 >= 0:
            change -= 2
            twoCoins +=1 
        elif change - 1 >= 0:
            change -= 1
            oneCoins += 1
        else:
            notFinished = False
    print(f'''Number of 50p coins is {fiftyCoins}\nNumber of 20p coins is {twentyCoins}\nNumber of 10p coins is {tenCoins}\nNumber of 5p coins is {fiveCoins}\nNumber of 2p coins is {twoCoins}\nNumber of 1p coins is {oneCoins}''')





if __name__ == "__main__":
    main()
