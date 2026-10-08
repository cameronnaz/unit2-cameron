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



# def wizards(N,start,duels):
#     owner = start
#     changedhands = 1
#     print(duels[0][1])
#     if duels[0][1] == owner:
#         owner = duels[0][0]
#         changedhands +=1
#     print(owner)
# wizards(3, "A", ["BA", "CB", "DA"])


""" 
def wizards(N,start,duels):
    owner = start
    numowners = 1
    for i in range(N):
        if duels[i][1] == owner:
            owner = duels[i][0]
            numowners +=1
        print(owner, numowners)
    
wizards(3, "A", ["BA", "CB", "DA"]) """


""" def engorfrench():
    sentence = str(input("What is your sentence"))
    engcount = 0
    frenchcount = 0
    for i in sentence:
        if i.lower() == "s":
            engcount +=1 
        elif i.lower() == "t":
            frenchcount +=1
        elif engcount == frenchcount:
            print ("this sentence is probably french")
    if engcount > frenchcount:
        print("Your sentence is english")
    if frenchcount > engcount:
        print("Your sentence is french.")
engorfrench()
         """


""" def epidemic(P, start, infected):
    today = start
    total = start
    daycount = 0
    while total <= P:
        today *= infected
        total += today
        daycount +=1
    print(daycount)
epidemic(750, 1, 5) """

def wizardbattle(N , start, duels):
    owner = start
    numbofowners = 1
    for i in range(N):
        if duels[i][1] == owner:
            owner = duels[i][0]
            numbofowners +=1
    print(owner, numbofowners)
wizardbattle(3, "E", ["BA","CB", "DA"])

    










def wizards(N, start, duels):
    owner = start
    numbofowners = 0
    for i in range(N):
        if duels [i][1] == owner:
            owner = duels [i][0]
            numbofowners +=1
    print(owner, numbofowners)
wizards(6, "A", ["BA", "BC", "DB", "ED", "EF", "GE"])