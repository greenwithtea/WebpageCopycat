for i in range(0, 3, 1):
    print("안녕하세요? for 문을 공부 중 입니다. ^^")

for x in [0, 1, 2, 3, 4]:
    print(x, end="")

print()

for i in range(0,3,1):
    print(i, ": 안녕하세요?")

for i in range(0, 3, 1):
    print("%d : 안녕하세요?" %i)

for i in range(2, -1, -1):
    print("%d : 안녕하세요? for 문을 공부 중입니다.^^" %i)

for i in range(1,6,1):
    print(i, end = " ")

hap = 0
for i in range(1,11,1):
    hap += i

print("1부터 10까지의 합계 : %d" %hap)

hap = 0
for i in range(501, 1001, 2):
    hap +=i
print("500과 1000 사이에 있는 홀수의 합계 : %d" %hap)



단 = int(input("단을 입력하세요 : "))

for i in range(1 ,10, 1):
    print("%d X %d = %d" %(단, i, 단*i))


for i in range(0, 3, 1):
    for k in range(0, 2, 1):
        print("파이썬은 꿀잼입니다.^^ (i값 : %d, k값 : %d)" %(i, k))


for _ in range(0, 3, 1):
    for _ in range(0, 2, 1):
        print("파이썬은 꿀잼입니다.^^")

#과제
for i in range(1, 10, 1):
    for k in range(2, 10, 1):
        print("%d x %d = %d" %(k, i, i*k), end = "\t")
    print()


i = 0
while i < 3 :
    print("%d : 안녕하세요? while 문을 공부 중입니다.^^" %i)
    i += 1



hap = 0

i = 1
while i < 11:
    hap = hap + i
    i = i+1
    
print("1에서 10까지의 합계 : %d" %hap)


hap, i = 0, 0

for i in range(1,101):
    if i %3 == 0 :
        continue

    hap += i

print("1~100의 합계(3의 배수 제외) : %d" %hap)


