def returnSum(Dict):
    list = []
    for i in Dict:
        list.append(Dict[i])
    result = sum(list) 
    return result
dict = {'a': 456, 'b': 789, 'c':520}
print("Total: ", returnSum(dict))
       