def find_min_value(list):
    min_value = list[0]
    for i in list:
        if min_value > i:
            min_value = i
    return min_value        

list = [17, 50, 18, 33, 58, 7, 33, 42]
result = find_min_value(list)
print(result)

list_1 = [10, 30 , -50, 33, 327, 42345]
result_1 = find_min_value(list_1)
print(result_1)




     
