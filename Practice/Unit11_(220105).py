#프로그래머스 www.programmers.co.kr _코딩테스트 기출 및 문제들
#LeetCode www.leetcode.com _국외 코딩테스트 기출

#part2

#실습

def getMax(val):
    val.sort()
    val.reverse()
    return val[0]


def getMin(val):
    val.sort()
    return val[0]


def getSum(val):
    hap = 0
    for i in val:
        hap+= i
    return hap


def getAvg(val):
    return getSum(val)/len(val)



if __name__=="__main__":

    value = [15, 7, 10, 4, 27]

    print("리스트 : %s\n" % value)

    print("최대값 : %d" % getMax(value))

    print("최소값 : %d" % getMin(value))

    print("합계 : %d" % getSum(value))

    print("평균 : %.2f" % getAvg(value))



#강의 구현

def getMax(val):
    maxValue = val[0]

    for v in val:
        if v > maxValue:
            maxValue = v

    return maxValue


def getMin(val):
    minValue = val[0]

    for v in val:
        if v < minValue:
            minValue = v

    return minValue


def getSum(val):
    sumValue = 0
    
    for v in val:
        sumValue += v
        
    return sumValue


def getAvg(val):
    return getSum(val)/len(val)



if __name__=="__main__":

    value = [15, 7, 10, 4, 27]

    print("리스트 : %s\n" % value)

    print("최대값 : %d" % getMax(value))

    print("최소값 : %d" % getMin(value))

    print("합계 : %d" % getSum(value))

    print("평균 : %.2f" % getAvg(value))


#part3

covid = [[3, 5], [7, 9], [17, 17], [21, 28], [30, 30]]

print("7월 서울, 경기 코로나 발생일 : %s" %covid)

result = 0

days = [False]* 31


for c in covid : #c = [3. 5] -> [7, 9]....
     start = c[0]
     end = c[1]

     for i in range(start-1, end):
         days[i] = True

#print("%s" %days)

#result += days.count(True)

for day in days:
    if day == True:
        result += 1

print("7월 서울, 경기 코로나 총 발생일 : %d일" %result)


#part4

def updateQty(age):
    global fare_qty
    
    if age >= 65:
        fare_qty[0] += 1

    elif age >= 18:
        fare_qty[1] += 1

    elif age >= 8:
        fare_qty[2] += 1

    else:
        fare_qty[3] += 1



def showQty():
    for i in range(0, num_type):
        print("%s %d원 : %d명" %(fare_type[i], fare[i], fare_qty[i]))



if __name__ == "__main__":
                               
    fare_type = ["경로", "성인", "청소년", "아동"]
    num_type = len(fare_type) #num_type = 4

    fare = [3000, 5000, 2000, 1000]
    fare_qty = [0, 0, 0, 0]

    total_fare = 0

    print("======= 입장료 =======")
    for i in range(0, num_type):
        print("%s : %d원" %(fare_type[i], fare[i]))
    #print("%s : %d원" %(fare_type[0], fare[0]))
    #print("%s : %d원" %(fare_type[1], fare[1]))
    #print("%s : %d원" %(fare_type[2], fare[2]))
    #print("%s : %d원" %(fare_type[3], fare[3]))
    print("======================")

    while True:
        age = int(input("\n나이를 입력하세요 (종료 버튼 -1) : "))
        if age == -1:
            break
        
        updateQty(age)
        showQty()

    for i in range(0, num_type):
        total_fare += fare[i] * fare_qty[i]

    print("총 금액은 %d원 입니다." %total_fare)

