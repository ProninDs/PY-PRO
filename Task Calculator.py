# Calculator
what = input()

a = float( input() )
b = float( input() )

if what == "+":
    c = a + b
    print(str(c))
elif what == "-":
    c = a - b
    print(str(c))
elif what == "*":
    c = a * b
    print(str(c))
elif what == "/":
    c = a / b
    print(str(c))  
elif what == "//":
    c = a // b
    print(str(c))
elif what == "%":
    c = a % b
    print(str(c))
elif what == "**":
    c = a ** b
    print(str(c))
else: 
    print("Error")