import random

def rand_num_list_gen(num=100, lower=1, upper=50):
    rand_num_list = [random.randint(lower, upper) for _ in range(num)]
    return rand_num_list

def main():
    rand_num_list = rand_num_list_gen()
    print("I have generated 100 random numbers between 1 and 50.")
    print("The count in the given ranges is:")

    rand_num_list.sort()
    count = {"10": 0,"20": 0, "30": 0, "45": 0, "50": 0}
    for i in range(len(rand_num_list)):
        if rand_num_list[i] <= 10:
            count["10"] += 1
        elif rand_num_list[i] <= 20:
            count["20"] += 1
        elif rand_num_list[i] <= 30:
            count["30"] += 1
        elif rand_num_list[i] <= 45:
            count["45"] += 1
        elif rand_num_list[i] <= 50:
            count["50"] += 1

    print(f"""1..10: {count["10"]}
11..20: {count["20"]}
21..30: {count["30"]}
31..40: {count["45"]}
41..50: {count["50"]}
""")

def advanced_main():
    num_to_gen = input(
        "Please enter the number of integers to generate from the range:\n\n"
    )
    ranges = input(
        "Please enter the ranges in the following format 1..5,6..10,11..20\n\n"
    )
    
    print("The count in the given ranges is:\n")
    
    rand_num_list = rand_num_list_gen(num=int(num_to_gen))

    rand_num_list.sort()

    count = {"20": 0, "30": 0, "45": 0, "50": 0}
    for i in range(len(rand_num_list)):
        if rand_num_list[i] <= 20:
            count["20"] += 1
        elif rand_num_list[i] <= 30:
            count["30"] += 1
        elif rand_num_list[i] <= 45:
            count["45"] += 1
        elif rand_num_list[i] <= 50:
            count["50"] += 1

    print(f"""1..20: {count["20"]}
21..30: {count["30"]}
31..45: {count["45"]}
46..50: {count["50"]}
""")
    

if __name__ == "__main__":
    main()
    #advanced_main()