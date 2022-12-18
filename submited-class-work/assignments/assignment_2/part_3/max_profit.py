def price_to_profit(L):
    profit_values = []

    for price in range(len(L)):

        if price == 0: profit_values.append(0)
        else: profit_values.append(L[price] - L[price - 1])

    return profit_values


def max_profit_brute(L):

    n = len(L)
    max_sum = 0


    for i in range(n):
        total = L[i]
        if total > max_sum: max_sum = total

        for j in range(i+1, n):
            total += L[j]
            if total > max_sum: max_sum = total
    return max_sum

def max_profit(L, left, right):
    if left == right: return 0

    middle_index = (left + right) // 2
    profit_1 = max_profit(L, left, middle_index)
    profit_2 = max_profit(L, middle_index + 1, right)
    profit_3 = _max_profit_center(L, left, right, middle_index)

    return max(profit_1, profit_2, profit_3)


def _max_profit_center(L, left, right, med):

    x, y = 0, 0

    for item in range(med, left - 1, -1): 
        y += L[item]
        if y > x: x = y 

    a, b = 0, 0

    for item in range(med + 1, right + 1):
        b += L[item]
        if b > a: a = b

    z = x + a

    return max(x, a, z)
    
if __name__ == '__main__':

    assert price_to_profit([100, 105, 97, 200, 150]) == [0, 5, -8, 103, -50]
    L = [1, 2, -9, 47, -10]
    assert max_profit(L, 0 , len(L)-1) == 47
    L2 = [0, -1, 3, 4, -5, 9, -2]
    assert max_profit(L2, 0, len(L2)-1) == 11

    import csv
    import os


    val_2015 = []
    val_2016 = []
    val_2017 = []
    val_2018 = []
    val_2019 = []
    val_2020 = []

    vals = [val_2015, val_2016, val_2017, val_2018, val_2019, val_2020]

    for file in os.scandir(r'./bitcoin_prices'):
        if (file.path.endswith(".csv")):
            if file.name == "2015.csv": i = 0
            elif file.name == "2016.csv": i = 1
            elif file.name == "2017.csv": i = 2
            elif file.name == "2018.csv": i = 3
            elif file.name == "2019.csv": i = 4
            elif file.name == "2020.csv": i = 5

            with open(file, 'r') as f:
                reader = csv.reader(f)

                lst = list(reader)[1:]
                for j in range(len(lst)):
                    vals[i].append( float(lst[j][1].replace(",","")))


    year_profits = []
    for year in vals:
        year_profits.append([])
        year_profits[-1] = price_to_profit(year)

    max_profits = [298, 604, 18561, 4476, 9665, 24052]

    for i, year in enumerate(year_profits):
        assert round(max_profit(year, 0, len(year)-1), 0) == max_profits[i]
