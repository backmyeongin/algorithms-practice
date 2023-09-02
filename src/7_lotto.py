import random

lotto_number = []

# for _ in range(6):
#     value = random.randint(1, 46)
#     lotto_number.append(value)
    
# print(lotto_number)



while True:
    value = random.randint(1, 46)
    lotto_number.append(value)
    if value in lotto_number:
        continue
    lotto_number.append(value)
    if len(lotto_number) == 6:
        break
    

print(lotto_number)





