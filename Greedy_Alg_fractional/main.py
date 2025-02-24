from parameters import *
from get_item import *
from highest_profit_weight_item import highest_profit_weight_item




# Item Class 
class Item :
    def __init__(self , profit , weight): 
        self.profit = profit
        self.weight = weight 
        self.profit_by_weight = profit/weight
        self.portion = 0.0  # %item
        

# Main      
if __name__ == '__main__' : 
    print(f'Max Weight is : {MAX_WEIGHT}')
    print('=============================')
    items = get_items(N , input_item=OBJECTS , verbos=0)
    bag = []
    OFS = MAX_WEIGHT  # free space in bag
    while OFS > 0: 
        best_case = highest_profit_weight_item(items)
        if best_case:
                if best_case.weight <= OFS:
                    best_case.portion = 1 
                    bag.append(best_case)
                    OFS -= best_case.weight
                else :
                    best_case.portion = ((OFS*100) / best_case.weight)/100
                    bag.append(best_case)
                    OFS = 0 
                     
        else :
            break    
    
    total_profit = 0
    weight = ''
    profits = ''
    for i in bag :
        total_profit += i.portion * i.profit
        weight += f'{i.weight * i.portion} + '
        profits += f'{i.profit * i.portion} + '
    print('Total Profit :' , total_profit )  
    print(f'Weights : , {weight[:len(weight)-3]}')
    print(f'Profits : , {profits[:len(profits)-3]}')    
            