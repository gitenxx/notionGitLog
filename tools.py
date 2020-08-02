class TextHandler():
    @staticmethod
    def removeNestings(nested_list, output): 
        for i in nested_list: 
            if type(i) == list: 
                TextHandler.removeNestings(i, output) 
            else: 
                output.append(i) 
