menu1 = "아메리카노"
menu2 = "카페라떼"

price1 = 4100
price2 = 4600

tall = 0
grande = 500
venti = 1000

total_price = 0

print("===== 2021 Starbucks Menu ========")
print("1. %s : %d원" %(menu1, price1))
print("2. %s : %d원" %(menu2, price2))
print()
print("사이즈 : Tall +%d원, Grande +%d원, Venti +%d원" %(tall, grande, venti))
print("===================================")

menu = int(input("메뉴를 선택해주세요 : "))
if menu == 1:
    print("%s를 선택하셨습니다." %menu1)
    total_price += price1
elif menu == 2:
    print("%s를 선택하셨습니다." %menu1)
    total_price += price1
else:
    print("잘못 입력하셨습니다.")

print("현재 주문 금액 : %d\n" %total_price)

size = int(input("사이즈를 선택해주세요 (1. Tall, 2. Grande, 3. Venti) : "))
if size == 1:
    total_price += 0
elif size == 2:
    total_price += 500
elif size == 3:
    total_price += 1000
else:
    print("잘못 입력하셨습니다.")

print("현재 주문 금액 : %d\n" %total_price)

cash = int(input("현금을 넣어주세요 : "))
change =  cash - total_price
print("잔돈 %d원 입니다. 안녕히 가십시오." % change)
