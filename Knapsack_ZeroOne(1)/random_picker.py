from random import randint as rnd


def random_picker(items , max_weight): 
    offset  = max_weight 
    bag = []
    items = [item for item in items if item.weight<=offset]
    while any(map(lambda x:True if x.weight < offset else False , items)):
        lenght = len(items)-1
        random_item = rnd(0 , lenght)
        offset -= items[random_item].weight
        bag.append(items[random_item])
        items.remove(items[random_item])
        items = [item for item in items if item.weight<=offset]
    return bag