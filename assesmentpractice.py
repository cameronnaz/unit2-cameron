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



def wizards(N,start,duels):
    owner = start
    changedhands = 1
    print(duels[N][0])
    if duels[N][0] == owner:
        owner = duels[N][0]
        changedhands +=1
    print(owner)
wizards(3, "A", ["BA", "CB", "DA"])

