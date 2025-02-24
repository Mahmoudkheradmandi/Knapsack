
def fitness(bag):
    total_profit = 0
    for item in bag:
        total_profit += item.profit
    return total_profit    