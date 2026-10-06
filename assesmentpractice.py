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


def engorfrench():
    sentence = (input("What is your sentence"))
    engcount = 0
    sentence.count
    if "s" or "S":
        engcount +=1
    frenchcount = 0
    if "t" or "T":
        frenchcount +=1
    if engcount > frenchcount:
        print("Your sentence is english")
    if frenchcount > engcount:
        print("Your sentence is french.")
engorfrench()
        

    






