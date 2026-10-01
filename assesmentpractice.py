""" def spaces():
    Y = ["C","C",".",".","C"]
    T = [".","C","C",".","."]
    N = 5
    count = 0
    for i in range (N):
        if Y[i] == "C" and T[i] == "C":
            count += 1
            print(count)
spaces() """


def englishfrench():
    sentence = (input("What is your sentence"))
    engfrench = sentence.split()
    typeofletter = len(engfrench)
    engcount = 0
    frecount = 0
    if "t" or "T":
        engcount +=1
    if engfrench == "t" or "T" > "s" or "S":
        print("Your sentence is english")
    if "s" or "S":
        frecount +=1  
    if engfrench == "s" or "S" > "t" or "T":
        print("Your sentence is french")
englishfrench()

