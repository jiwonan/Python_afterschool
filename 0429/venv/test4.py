num = int(input("임의의 정수 입력 : "))
i = 1
sum = 0
for i in range(num+1):
    sum += i
print("1~",num,"까지의 합 : ",sum)