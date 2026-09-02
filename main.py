l=["[","{","}","]"]

stack=[]
stack = []

pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

def isopening(ch):
    if ch=="[" or ch=="(" or ch=="{":
        return True

    else:
        return False

for i in l:

    if isopening(i):
        stack.append(i)


    else:

        if not stack:
            return False

        if pairs[i] != stack[-1]:
            return False

        stack.pop()



    if not stack:
        print("finish")
        break
