""" x = 3
y = float(3)
print(x,y)
 """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
 """

""" bill = float(input("How much is the bill?"))
service = input("how good was the service (bad okay good great)")
if service == "bad":
    bill = (bill + 0)
    print(f"Your total is {bill}")
elif service == "okay":
    bill = (bill * 1.15)
    print(f"Your total is {bill}")
elif service == "good":
    bill = (bill * 1.20)
    print(f"Your total is  {bill}")
elif service == "great":
    bill = (bill * 1.25)
    print(f"Your total is {bill}")
 """


""" def calculator():
    bill = float(input("How much was the bill?"))
    tip = float(input("How much would you like to tip? (0, 0.10, 0.20, 0.25)"))
    total = bill * (1 + tip)
    print(f"Your total is {total}")
calculator()
 """

""" def oddoreven():
    number = int(input("what is your number"))
    if number % 2 == 0:
        print(f"Your number {number} is even")
    else:
        print(f"Your number {number} is odd")
oddoreven()
 """

""" def factors():
    factors = []
    number = int(input("What is your number"))
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
    print(factors)
factors() """


def sentences():
    sentence = (input("What is your sentence"))
    wordcount = sentence.split()
    wordsnumber = len(wordcount)
    print("There are " + str(wordsnumber) + "words in your sentence")
sentences()
