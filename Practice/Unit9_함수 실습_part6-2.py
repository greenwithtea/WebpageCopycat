def showMenu():
    print("===== 2021 Starbucks Menu ========")
    print("0. 주문종료")
    print("1. %s : %d원" %(menu1, price1))
    print("2. %s : %d원" %(menu2, price2))
    print()
    print("사이즈 : Tall +%d원, Grande +%d원, Venti +%d원" %(tall, grande, venti))
    print("===================================")

def selectMenu():
    global coffee
    global breakFlag
    global continueFlag
    
    menu = int(input("메뉴를 선택해주세요 : "))
    if menu == 1:
        print("%s를 선택하셨습니다." %menu1)
        coffee += price1
    elif menu == 2:
        print("%s를 선택하셨습니다." %menu1)
        coffee += price1
    elif menu == 0:
        print("주문을 종료합니다.")
        breakFlag = True
        
    else:
        print("잘못 입력하셨습니다.")
        continueFlag = True
    

def selectSize():
    global total_price
    global coffee
    
    size = int(input("사이즈를 선택해주세요 (1. Tall, 2. Grande, 3. Venti) : "))
    if size == 1:
        coffee += 0
        total_price += coffee
        
    elif size == 2:
        coffee += 500
        total_price += coffee
        
    elif size == 3:
        coffee += 1000
        total_price += coffee
        
    else:
        print("잘못 입력하셨습니다.")
        
    print("현재 주문 금액 : %d\n" %total_price)
    
def payment():
    cash = int(input("현금을 넣어주세요 : "))
    change =  cash - total_price #이 total_price는 위에 처럼 어딘가에 또 포함되어 있는 것은 아니기 때문에 global 붙일 필요는 없음.
    print("잔돈 %d원 입니다. 안녕히 가십시오." % change)
    
if __name__=="__main__": #프로그램은 항상 main 함수에서 시작됨. 프로그램의 시작점을 알려줌. 다른 함수들과 구분짓는 역할도 함.
    menu1 = "아메리카노"
    menu2 = "카페라떼"

    price1 = 4100
    price2 = 4600

    tall = 0
    grande = 500
    venti = 1000

    total_price = 0

    breakFlag = False #한 번만 실행

while True:
    continueFlag = False #계속 반복
    coffee = 0 #음료 단가 +사이즈 추가금
    
    showMenu()

    selectMenu()
    if breakFlag == True:#반복문 진행 중 딱 한 번만 true 찾으면 탈출
        break

    if continueFlag == True:
        continue

    selectSize()
    

payment()

