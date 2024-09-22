calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    if isinstance(string, str):
        cortege = (len(string), string.upper(), string.lower())
        count_calls()
        return cortege
    else:
        print('Функция не сработала, потому что введённый аргумент не является строкой.')

def is_contains(string,list_to_search):
    if isinstance(string,str) and isinstance(list_to_search, list):
        count_calls()
        string = string.lower()
        for i in list_to_search:
            if isinstance(i, str):
                i = i.lower()
                if i == string:
                    return True
        return False
    else:
        print('Функция не сработала: 1ый аргумент должен быть строкой, а 2ой - списком.')

print(string_info("Арбуз"))
print(string_info('Здравствуйте'))
print(is_contains('КоллЕКция',[5,'Цикл','Путеводный', 'коллекция']))
print(is_contains('КоллЕКция',[5,'Цикл','Путеводный']))
print(f'Количество вызовов функций string_info и is_contains: {calls}.')