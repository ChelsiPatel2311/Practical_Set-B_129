# practical 4A code 
rows = 5

for i in range(1, rows + 1):
    
    # Print spaces (for right alignment)
    print(" " * (rows - i), end="")
    
    # Print alphabets
    for j in range(i):
        print(chr(65 + j), end=" ")
    
    print()
# Full Pyramid (Inverted)

rows = 5

for i in range(rows, 0, -1):
    print("* " * i)
# practical 4A code 
rows = 5

for i in range(1, rows + 1):
    
    # Print spaces (for right alignment)
    print(" " * (rows - i), end="")
    
    # Print alphabets
    for j in range(i):
        print(chr(65 + j), end=" ")
    
    print()
