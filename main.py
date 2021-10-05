#WRITE YOUR CODE IN THIS FILE
def hasL(w):
    w = w.lower()
    for i in range(0, len(w)):
        if w[i] == "l":
            return True
    else:
        False

hasL("hassle")