#WRITE YOUR CODE IN THIS FILE
def hasL(w):
    x = 0
    while x < len(w):
        if w == "l":
            return True
        else:
            return False
        x = x + 1
print(hasL("alligator"))
