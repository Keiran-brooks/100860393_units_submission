import random

def coin_tosses(n):
    tosses = []

    for i in range(n):
        tosses.append(random.randint(0,1))

    return tosses

#1 is heads 0 is tails
def count(tosses):
    heads = 0
    tails = 0
    for i in range(len(tosses)):
        if(tosses[i]==0):
            tails += 1
        else:
            heads += 1

    return (heads, tails)


def percentage(count_of_tosses):
    percent = lambda count, total : (count/total)*100
    totalTosses = count_of_tosses[0]+count_of_tosses[1]

    return (percent(count_of_tosses[0], totalTosses), percent(count_of_tosses[1], totalTosses))


def format_percentage(value):
    if value.is_integer():
        return f"{value:.1f}"
    return f"{value:.2f}"


def main():
    x = input("How many coin tosses would you like to simulate?\n")

    countOfTosses = count(coin_tosses(int(x)))


    print(f"\nNo. of Heads: {countOfTosses[0]}")
    print(f"No. of Tails: {countOfTosses[1]}")

    percentages = percentage(countOfTosses)
    print(f"\n%   of Heads: {format_percentage(percentages[0])}")
    print(f"%   of Tails: {format_percentage(percentages[1])}")


if __name__ == "__main__":
    main()