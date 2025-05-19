나이 = int(input("나이를 입력하세요. : "))

if 나이>=20 :
    print("\n투표를 할 수 있습니다.")

a=200

if a < 100 :
    print("100보다 작군요.")

print("거짓이므로 이 문장은 안 보이겠죠?")
print("프로그램 끝")


a = 400

if a <100 :
    print("100보다 작군요")
    print("거짓이므로 이 문장은 안보이겠죠?")

print("프로그램 끝")


#part2

나이 = int(input("나이를 입력하세요. : "))

if 나이>=20 :
    print("\n투표를 할 수 있습니다.")
    
else:
    print("\n투표를 할 수 없습니다.")


a = 200

if a < 100 :
    print("\n100보다 작군요.")

else :
    print("\n100보다 크군요.")


#실습_과제
num = int(input("정수를 입력하세요 : "))
remainder = num%2

if remainder==1 :
    print("홀수를 입력했군요.")

else:
    print("짝수를 입력했군요.")


a = 75

if a >50 :
    if a < 100 :
        print("50보다 크고 100보다 작군요.")
    else:
        print("와~~100보다 크군요.")

else:
    print("에고~50보다 작군요.")


#실습_과제
a = int(input("값을 입력하세요 : "))

if a >= 90 :
    print("A", end ='')

else :
    if a >= 80 :
        print ("B", end = '')

    else:
        if a >= 70:
            print("C", end = '')

        else:
            if a >= 60:
                print("D", end = '')
            else:
                print("F", end = '')

print("학점입니다.^^")



a = int(input("값을 입력하세요 : "))


if a >= 90 :
    print("A", end ='')

elif a >= 80 :
    print ("B", end = '')

elif a >= 70:
    print("C", end = '')

elif a >= 60:
    print("D", end = '')

else:
    print("F", end = '')


print("학점입니다.^^")
