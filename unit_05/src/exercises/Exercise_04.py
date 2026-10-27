def arithmetic_sum(a,b,n):
    total = a
    
    for i in range(1, n, 1):
        total += (b*i)+a

    return total
    


if __name__ == "__main__":
    print(arithmetic_sum(1,1,100))   # prints the return value - 5050
    print(arithmetic_sum(3,2,15))    # prints the return value -  255
    print(arithmetic_sum(10,4,5))    # prints the return value -  90
    print(arithmetic_sum(-5, -2, 20))    # prints the return value -  -480
