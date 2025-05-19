def plus(num1, num2):
    return num1 + num2

print(plus(1, 6))


def plus (v1, v2):
    #result = 0
    result = v1+ v2
    return result

#hap = 0

hap = plus(100, 200)
print("100과 200의 plus() 함수 결과는 %d" %hap)


def triangle(a, b):
    return a * b / 2

def square (a, b):
    return a * b

num1= int(input("첫번째 정수를 입력하세요 : "))
num2= int(input("두번째 정수를 입력하세요 : "))

tri = triangle(num1, num2)
squ = square (num1, num2)

print("삼각형 넓이는 %.2f 이고, 사각형 넓이는 %d 입니다."%(tri, squ))


coffee = 0
coffee = int(input("어떤 커피 드릴까요? (1: 보통, 2: 설탕, 3: 블랙)"))

print()
print('#1. 뜨거운 물을 준비한다.');
print('#2. 종이컵을 준비한다.');

if coffee == 1 :
    print('#3. 보통커피를 탄다.')
elif coffee == 2 :
    print('#3. 설탕커피를 탄다.')
elif coffee == 3 :
    print('#3. 블랙커피를 탄다.')
else :
    print('#3. 아무거나 탄다.\n')

print('#4. 물을 붓는다.');
print('#5. 스푼으로 젓는다.')
print()
print('손님~커피 여기 있습니다.');


def coffee_machine (coffee):
    print('#1. 뜨거운 물을 준비한다.')
    print('#2. 종이컵을 준비한다.')
    if coffee == 1 :
        print('#3. 보통커피를 탄다.')
    elif coffee == 2 :
        print('#3. 설탕커피를 탄다.')
    elif coffee == 3 :
        print('#3. 블랙커피를 탄다.')
    else :
        print('#3. 아무거나 탄다.\n')

    print('#4. 물을 붓는다.')
    print('#5. 스푼으로 젓는다.')
    print()

coffee = int(input("어떤 커피 드릴까요? (1: 보통, 2: 설탕, 3: 블랙)"))
coffee_machine(coffee)
print("손님~ 커피 여기 있습니다.")



def calculater (operater, num1, num2):
    if operater == '+' :
        return num1 + num2
    elif operater == '-':
        return num1 - num2
    elif operater == '*' :
        return num1 * num2
    else:
        return num1 / num2
        

operater = input("계산을 입력하세요 (+, -, *, /)  : ")
num1 = int(input("첫 번째 수를 입력하세요 : "))
num2 = int(input("두 번째 수를 입력하세요 : "))

cal = calculater(operater, num1, num2)

print("## 계산기 : %d %c %d = %.2f" %(num1, operater, num2,cal))



def func1():
    a=10
    print("func1()에서 a 값 %d" %a)

def func2():
    print("func2()에서 a 값 %d" %a)

a=20

func1()
func2()

import Module

Module.a()

from Module import a, b

a()
b()
#c()


from Module import *
a()
c()




