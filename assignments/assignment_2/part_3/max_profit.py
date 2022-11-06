def price_to_profit(L): pass


# brute force solution, for reference
def max_profit_brute(L):
    """Finds maximum profit. Assumes L is a list of profits (i.e. change in price every day), not raw prices"""
    n = len(L)
    max_sum = 0 # assume we can at least break even - buy and sell on the same day

    # outer loop finds the max profit for each buy day
    for i in range(n):
       # total profit if we bought on day i and sold on day j
        total = L[i]
        if total > max_sum: max_sum = total

        for j in range(i+1, n):
            total += L[j] # total profit if we sell on day j
                          # we assume L[j] is the profit if we bought on day j-1 and sold on day j
                          # i.e., L is the change in value each day, relative to the day before
            if total > max_sum: max_sum = total

    return max_sum


# you can use a helper function or add parameters, your choice
def max_profit(L): pass

# you will need a separate function to find the "center sum"
def _max_profit_center(L, left, right, med): pass





# some test cases, and an example of reading CSVs
if __name__ == '__main__':
    # some basic tests of the necessary functions
    assert price_to_profit([100, 105, 97, 200, 150]) == [0, 5, -8, 103, -50]
    assert max_profit([0, 5, -8, 103, -50]) == 103
    assert max_profit([0, -1, 3, 4, -5, 9, -2]) == 11


    ##### Import and read values from associated csvs, then check if you can become a bitcoin-optimaire
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


    # find the profits for each year
    year_profits = []
    for year in vals:
        year_profits.append([])
        year_profits[-1] = price_to_profit(year)

    # correct max profits per year, 2015-2020, rounded to ints
    max_profits = [298, 604, 18561, 4476, 9665, 24052]

    # test that max_profit returns the correct profit for each year
    for i, year in enumerate(year_profits):
        assert round(max_profit(year), 0) == max_profits[i]
