#WRITE YOUR CODE IN THIS FILE
def hasL(w):
    for i in range(0, len(w)):
        print(w[i])
        if i == "l":
            return True
        else:
            return False
hasL("hassle")
