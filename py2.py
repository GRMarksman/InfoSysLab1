a_dict = {"a": 10, "b": 12, "c": 14, "d": 14, "e": 16, "f": 28, "g": 28, "h": 30}

def sortDict():
        sortedDict = sorted(a_dict.values())
        print(sortedDict)

print("Sorted dictionary is: ")
sortDict()


result={}

def removeDups():
        for key,value in a_dict.items():
                if value not in result.values():
                        result[key]=value
        print(result)

print("Clean dictionary is: ")
removeDups()