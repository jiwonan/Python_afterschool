from random import randint

print("*****가위바위보게임*****")
while True:
    x = randint(0, 2)
    print("다음 중 하나를 선택하세요.")
    user = int(input("가위(0), 바위(1), 보(2), 종료(3) : "))
    if user==3:
        print("종료합니다.")
        break
    if x==0:
        print("컴퓨터는 가위를 냈습니다.")
        if user==0:
            print("비겼습니다.")
        elif user==1:
            print("이겼습니다.")
        elif user==2:
            print("졌습니다.")
    elif x==1:
        print("컴퓨터는 바위를 냈습니다.")
        if user==0:
            print("졌습니다.")
        elif user==1:
            print("비겼습니다.")
        elif user==2:
            print("이겼습니다.")
    elif x==2:
        print("컴퓨터는 보를 냈습니다.")
        if user==0:
            print("이겼습니다.")
        elif user==1:
            print("졌습니다.")
        elif user==2:
            print("비겼습니다.")