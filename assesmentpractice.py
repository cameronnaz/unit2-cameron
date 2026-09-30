def spaces():
    Y = ["C","C",".",".","C"]
    T = [".","C","C",".","."]
    N = 5
    count = 0
    for i in range (N):
        if Y[i] == "C" and T[i] == "C":
            count += 1
            print(count)
spaces()