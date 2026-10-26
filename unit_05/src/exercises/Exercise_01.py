
# Please enter a wholesale cost:
# 5.00
# Please enter a markup percentage:
# 50
# The retail price is £7.50.

def calc_retail_price(price, markup):
    return price + (price * markup / 100)

def main():
    wholesalePrice = float(input("Please enter a wholesale cost:\n"))
    markupAmount = float(input("Please enter a markup percentage:\n"))

    print(f"The retail price is £{calc_retail_price(wholesalePrice,markupAmount):.2f}.")

# This is needed for the tests. This is now the first bit of code Python will run.
# Please ask if you are curious, but it is enough to understand that this calls the main() function and runs whatever code you have in there.
if __name__ == "__main__":
    main()  # calls the main function

    # uncomment the following lines to test calc_retail_price when you run the program.You will need to comment out main()
    # print(calc_retail_price(3.00, 100)) # should print 6.0
    # print(calc_retail_price(5.00, 50)) # should print 7.5
