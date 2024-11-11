E = ""
print('''Let's play a game, if you give me 5 numbers
and  I will choose the greatest number.
The number has to be whole, no words or special characters.
''')
N1 = int(input("What is your first number? "))
print(E)
N2 = int(input("What is your second number? "))
print(E)
N3 = int(input("What is your third number? "))
print(E)
N4 = int(input("What is your fourth number? "))
print(E)
N5 = int(input("What is your fifth number? "))
print(E)
numbers = [N1, N2, N3, N4, N5]

A = 0
A = numbers[0]
if A < numbers[1]:
  A = numbers[1]
if A < numbers[2]:
  A = numbers[2]
if A < numbers[3]:
  A = numbers[3]
if A < numbers[4]:
  A = numbers[4]
print(f"This is the biggest number you put: {A}")
