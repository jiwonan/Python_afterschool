num = int(input("원하는 단은 : "))
print("for문 사용")
for i in range(9):
    print("%d * %d = %2d" % (num,i+1,num*(i+1)))
i = 1
print("while문 사용")
while i <= 9:
    print("%d * %d = *2d" % (num,i,num*i))
    i=i+11