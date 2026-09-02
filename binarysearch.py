nums="marisol is good "


new=""





start=False
for i in nums:
    for x in range(len(i) - 1, -1, -1):



        if i[x]!= " " :
            start=True



        if start:
            if i[x]== " ":
                break
            new+=i[x]




print(new[::-1])

    


