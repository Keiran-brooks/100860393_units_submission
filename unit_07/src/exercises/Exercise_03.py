import random

def coin_tosses(n):
    tosses = []

    for i in range(n):
        tosses.append(random.randint(0,1))

    return tosses

#1 is heads 0 is tails
def count(tosses):
    zeros = 0
    ones = 0
    for i in range(len(tosses)):
        if(tosses[i]==0):
            zeros += 1
        else:
            ones += 1

    return (zeros, ones)


def percentage(count_of_tosses):
    percent = lambda count, total : (count/total)*100
    totalTosses = count_of_tosses[0]+count_of_tosses[1]

    return (percent(count_of_tosses[0], totalTosses), percent(count_of_tosses[1], totalTosses))


def main():
    x = input("How many coin tosses would you like to simulate?\n")

    countOfTosses = count(coin_tosses(int(x)))


    print(f"\nNo. of Heads: {countOfTosses[1]}")
    print(f"No. of Tails: {countOfTosses[0]}")

    percentages = percentage(countOfTosses)
    print(f"\n%   of Heads: {percentages[1]}")
    print(f"%   of Tails: {percentages[0]}")


if __name__ == "__main__":
    main()