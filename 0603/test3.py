import random
bindo=[0,0,0,0,0,0]

for x in range (1000):
    value = random.randint(0,5)
    bindo[value]=bindo[value]+1

for x in range(6):
    print(x+1,"의 빈도: ",bindo[x])