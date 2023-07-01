def value_swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

x = 10 
y = 20

# 기대되는 값: x: 20 , y: 10
res1, res2 = value_swap(x, y)
print(f'x: {res1} , y: {res2}')
