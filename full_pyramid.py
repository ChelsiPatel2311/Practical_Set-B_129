rows = 5

for i in range(rows):
    # Print leading spaces
    print(" " * i, end="")

    # Print stars with space
    for j in range(rows - i):
        print("* ", end="")

    print()
# practical 4A code 
rows = 5

for i in range(1, rows + 1):
    
    # Print spaces (for right alignment)
    print(" " * (rows - i), end="")
    
    # Print alphabets
    for j in range(i):
        print(chr(65 + j), end=" ")
    
    print()
