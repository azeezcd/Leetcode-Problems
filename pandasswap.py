import pandas as pd

data = {
    'transaction_id': [1, 2, 3, 4, 5, 6],
    'amount': [150, 200, 75, 300, 50, 120],
    'transaction_date': [
        '2024-07-01',
        '2024-07-01',
        '2024-07-01',
        '2024-07-02',
        '2024-07-02',
        '2024-07-03'
    ]
}


dates_list = [i for i in data['transaction_date']]
amounts_list = [i for i in data['amount']]


ultimate_dic = {
    'transaction_date': [],
    'odd': [],
    'even': []
}


previous_date = ""

for x in range(len(dates_list)):


    if dates_list[x] != previous_date:

        ultimate_dic['transaction_date'].append(dates_list[x])


        ultimate_dic['odd'].append(0)
        ultimate_dic['even'].append(0)

        previous_date = dates_list[x]

    #
    if amounts_list[x] % 2 == 0:
        ultimate_dic['even'][-1] += amounts_list[x]

    else:
        ultimate_dic['odd'][-1] += amounts_list[x]


print(ultimate_dic)