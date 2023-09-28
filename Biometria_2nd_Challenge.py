n1 = int(input("First Number:"))

op = input("Operation:")

n2 = int(input("Second Number:"))


allowed_ops= {
"+": lambda n1 , n2: n1 + n2,
"-": lambda n1, n2: n1 - n2,
"*": lambda n1, n2: n1 * n2,
"/": lambda n1, n2: n1 / n2
}

print(allowed_ops[op](n1, n2))


