import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    new_list = employee['salary'].sort_values(ascending=False).drop_duplicates().tolist()

    if len(new_list) >= 2:
        second_highest = {"SecondHighestSalary": [new_list[1]]}
    else:
        second_highest = {"SecondHighestSalary": [None]}

    return pd.DataFrame(second_highest)