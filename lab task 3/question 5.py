n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("\nTable of", i)

    for j in range(1, 10):
        print(i, "x", j, "=", i * j)
