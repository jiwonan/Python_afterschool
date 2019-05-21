sum = 0;
while True:
    print("손님 주문하시겠습니까?")
    x = int(input("<1> 카페라떼 <2> 카푸치노 <3> 아메리카노 <4> 그만시킬래요 ==> "))
    if x==4:
        print("주문하신 커피 준비하겠습니다.")
        break
    elif x==1:
        print("카페라떼 주문하셨습니다.")
    elif x == 2:
        print("카푸치노 주문하셨습니다.")
    elif x == 3:
        print("아메리카노 주문하셨습니다.")