# Place your answer to Exercise_04 in this file
# Do not rename or remove this file


# Example,
# Please enter your first name:
# john
# Please enter your middle name:
# walter
# Please enter your last name:
# smith
# Hi, your initials are J.W.S

firstname = input("Please enter a first name: \n")  # leave this alone!
surname = input("Please enter a surname: \n")  # leave this alone!
lastname = input("Please enter a lastname: \n")

print(f"Hi, your initials are {'.'.join([firstname[0].upper(), surname[0].upper(), lastname[0].upper()])}")