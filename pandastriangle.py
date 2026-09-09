import pandas as pd

df = pd.DataFrame({
    "x": [13, 10],
    "y": [15, 20],
    "z": [30, 15]
})




def identifytriangle(data):


        triangle = pd.DataFrame(data)


        triangle['triangle'] = (
                (triangle['x'] + triangle['y'] > triangle['z']) &
                (triangle['x'] + triangle['z'] > triangle['y']) &
                (triangle['y'] + triangle['z'] > triangle['x'])
        ).map({True: 'Yes', False: 'No'})

        return triangle





print(identifytriangle(df))


