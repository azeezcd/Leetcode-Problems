import pandas as pd


import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5, 6],
    "email": [
        "a@gmail.com",
        "b@gmail.com",
        "a@gmail.com",
        "c@gmail.com",
        "b@gmail.com",
        "d@gmail.com"
    ]
}

df = pd.DataFrame(data)




all=list(df["email"])

new=[]



for i in all:
    if i not in new:
        new.append(i)

    else:
        continue




print(new)


