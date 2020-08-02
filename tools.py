def removeNestings(nested_list, output): 
    for i in nested_list: 
        if type(i) == list: 
            removeNestings(i, output) 
        else: 
            output.append(i) 
# TODO aвd OOP :----D
