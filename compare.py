import json
import itertools

class Compare:
    def __init__(self, obj1, obj2, outfile):
        self.obj1 = obj1
        self.obj2 = obj2
        self.modifications = []
        self.outfile = outfile
        self.find_diff(obj1, obj2)


    def find_diff(self, obj1, obj2, path=""):
        #Objects are completly different / not from the same type
        if not isinstance(obj1, type(obj2)):
           self._print_report_dict(path, obj1) if path is not "" else self._print_report(obj1)
           return
        
        obj1t = type(obj1)
        #Fisrt check top level item is list
        if obj1t is list:
           self._diff_list(obj1, obj2, path)
           return
        
        if obj1t is dict:
           self._diff_dict(obj1, obj2, path)
           return
        
        #assumming string or int just report
        self._print_report_dict(path, obj1) if path is not "" else self._print_report(obj1)
    
    
    def _diff_dict(self, dict1, dict2, path):
        if dict1 == dict2:
           return
        for k in dict1.keys():
            if(path == ""):
               deep_path = k
            else:
               deep_path = f"{path}->{k}"
            if not k in dict2:
                self._print_report_dict(k, dict2.values())            
            else:
                #dict2 has the key
                self.find_diff(dict1[k], dict2[k], deep_path) 

    def _diff_list(self, lst1, lst2, path):
        #lists are the same
        if lst1 == lst2:
           return
        for (index, item) in enumerate(lst1):
            item2 = None
            #Check if list2 has the same index number 
            try:
                item2 = lst2[index]
            except IndexError:
                #found mising list item
                self.find_diff(item,None, path)
                continue
            if item == item2:
                continue
            #if not the same instance - elements are differents
            if not isinstance(item, type(lst2[index])):
                self._print_report()
                continue
            #the same type with a different values send it back
            self.find_diff(item, item2, path)
    
    #output primitive values
    def _print_report(self, item1):
        s = f"{item1} ({type(item1).__name__})"
        self.outfile.write(s + "\n")
        print(s)
    #output nested collections 
    def _print_report_dict(self, key, elem):
        s = f"{key}->{elem}({type(elem).__name__})"
        self.outfile.write(s + "\n")
        print(s)
       