
def highest_profit_weight_item(list_item):
    best_item = None
    for i in list_item: 
        if best_item:
            if  i.profit_by_weight>best_item.profit_by_weight and i.portion<1:
                best_item = i
        else:    
              if i.portion<1:
                  best_item = i
    return best_item              