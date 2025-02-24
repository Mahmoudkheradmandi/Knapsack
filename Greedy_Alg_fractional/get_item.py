from main import Item

def get_items(n , input_item = None , verbos=0): 
    items = []
    if input_item == None:
        for i in range(n):
            print(f'Items #{i+1}')
            item_profit = int(input('Please Enter the Profit of the item : '))
            item_weight = int(input('Please Enter the Weight of the item : '))
            items.append(Item(item_profit , item_weight))
        print('===========================')   
    else: 
        for item in input_item:
            items.append(Item(item[0] , item[1]))
    if verbos :         
        for item in items:
            print(f'Item #{items.index(item)+1} : Profit:{item.profit} , weight:{item.weight}')
            
    return items  