s = 0
n = 0
x = int(input("Number: "))
m = x
numbers = []

while x!=-1:
    numbers.append(x)
    n += 1
    s += x
    if x < m:
        m = x
    x = int(input("Number: "))


if n == 0:
    m = -1
    a = -1
    print("There are no numbers in the list.")
else:
    a = s/n
    print(f"\nList of numbers: {numbers}")
    print(f"The minimum value is {m}\nThe average value is {a}\nThe sum of all the values is {s}\nThe number of values is {n}")

