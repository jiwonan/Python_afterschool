a = int(input("정수를 입력하시오 : "))
b = int(input("정수를 입력하시오 : "))
if (a > b) :
    print(a,"을 ",b,"로 나눈 목 = ",a/b,", 나머지 = ",a%b)
else:
    print(b, "을 ", a, "로 나눈 목 = ", b // a, ", 나머지 = ", b % a)

n = int(input("정수하나 입력 >> "))
if (n>0):
    print(n,"은 양수!")
elif (n<0):
    print(n,"은 음수!")
else:
    print(n,"은 0!")