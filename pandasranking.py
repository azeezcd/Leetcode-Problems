import pandas as pd

data = {
    'id': [1, 2, 3, 4, 5, 6],
    'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}

scores = pd.DataFrame(data)

points = list(scores['score'])
points = sorted(points, reverse=True)

ranking = []

rank = 1

for i in range(len(points)):

    if i > 0 and points[i] == points[i - 1]:
        ranking.append(ranking[i - 1])

    else:
        ranking.append(rank)
        rank += 1




new=pd.DataFrame({'score':points,'rank':ranking})
print(new)