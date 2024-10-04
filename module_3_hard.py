def Sum_data(Data=None):
    global list_
    Sum = 0
    if Data == None or isinstance(Data, bool):
        return 0
    elif isinstance(Data, str):
        list_.append(len(Data))
        return
    elif isinstance(Data, int) or isinstance(Data, float):
        list_.append(Data)
        return
    elif isinstance(Data, list) or isinstance(Data, tuple) or isinstance(Data, set):
        for i in Data:
            Sum_data(i)
    elif isinstance(Data, dict):
        for i in list(Data.items()):
            Sum_data(i)
    return sum(list_)

list_=[]
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(Sum_data(data_structure))

