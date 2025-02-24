from random import randint as rnd 
from copy import deepcopy
from get_item import get_item
from parameters import *
from random_picker import random_picker
from fitness import fitness


# Item Class 
class Item :
    def __init__(self , profit , weight): 
        self.profit = profit
        self.weight = weight 
                             
# Main      
if __name__ == '__main__' : 
    
    items = get_item(N , input_item=OBJECTS , verbos=0)
    best_profit = 0
    best_bag = []
    while EPOCH:
        new_bag = random_picker(items , MAX_WEIGHT)
        profit = fitness(new_bag) 
        if best_profit < profit: 
            best_profit = profit
            best_bag = deepcopy(new_bag)
              
            print('Best Bag Profit So far : ' , best_profit)
            print('Best Bag Weight So far : ' , sum(map(lambda x:x.weight , best_bag)))
            for item in best_bag:
                print(f'Item #{best_bag.index(item)+1} : Profit:{item.profit} , weight:{item.weight}')
            print('====================================================')    
        EPOCH -= 1    
            
            
            
         
    
          