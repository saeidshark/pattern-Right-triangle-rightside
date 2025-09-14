x = 10

for i in range(x):
    for j in range(x - i - 1):
        print(" ", end=" ")
    for y in range(i + 1):
        print("*", end=" ")
    print()
