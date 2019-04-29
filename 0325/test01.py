print("Hello")
print(7/4)
print(7//4)

p = int(input("분자를 입력하시오 : "))
q = int(input("분모를 입력하시오 : "))
print("나눗셈의 몫 = ", p//q)
print("나눗셈의 나머지 = ", p%q)

number = int(input("정수를 입력하시오 : "))
print(number % 2)

if (number % 2 == 0) :
    print("짝수입니다.")
else:
    print("홀수입니다.")

sec = 1000
min = 1000//60
remainder = 1000 % 60
print(min, remainder)