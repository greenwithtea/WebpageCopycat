print(100/200)
print(100%200)
print(100//200)

a=10
print(a%2)

a=7
print(a%2)

sec = int(input("초를 입력하세요. : "))
min = sec//60
remainder = sec%60

print("%d초는 %d분 %d초 이다." %(sec, min, remainder))


money = int(input("교환할 돈은 얼마? : "))
w500 = money//500
w100 = (money%500)//100
w50 = (money%500%100)//50
w10 = (money%500%100%50)//10

print("\n500원 짜리 ==> %d개" % w500)
print("100원 짜리 ==> %d개" % w100)
print("50원 짜리 ==> %d개" % w50)
print("10원 짜리 ==> %d개" % w10)
print("바꾸지 못한 잔돈 ==> %d개" % (money%500%100%50%10))

print(10==100)
