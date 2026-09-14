import pandas as pd

customer = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "name": ["Will", "Jane", "Alex", "Bill", "Zack", "Mark"],
    "referee_id": [None, None, 2, None, 1, 2]
})





names=[x for x in customer["name"]]
referee_id=[x for x in customer["referee_id"]]

new_names=[]



for i in range(len(referee_id)):
    if referee_id[i] !=2:
        new_names.append(names[i])





