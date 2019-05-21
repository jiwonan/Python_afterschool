def sum(a, b):
    sum = a+b
    sentence = "정수 "+str(a)+"+"+str(b)+"의 값은?"+(a+b)
    print(sentence)

a = int(input("첫 번째 정수 : "))
b = int(input("두 번째 정수 : "))
sum(a,b)