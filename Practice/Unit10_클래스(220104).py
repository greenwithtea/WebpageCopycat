class Car:
    #자동차의 필드
    
    color = ""
    speed = 0 #3행

    #자동차의 메서드
    def upSpeed(self, value) : #self.speed는 3행의 speed 의미, 즉 자신의 클래스에 있는 speed 변
        #현재 속도에서 증가할_속도량만큼 속도를 올리는 코드
        self.speed += value #self = car가 여러 개일 때 무엇이 저장된 value 함수에 다녀갔는지 주소 저


    def downSpeed(self, value) :
        #현재 속도에서 감소할_속도량만큼 속도를 내리는 코드
        self.speed -= value

#->지금까지 한 것은 그냥 그릇을 설계한 것 뿐이다. 템플릿만 정의한 것과 같다.


myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 10

myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 20

myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 30

print("myCar1 : %s, %d" %(myCar1.color, myCar1.speed))
print("myCar2 : %s, %d" %(myCar2.color, myCar2.speed))
print("myCar3 : %s, %d" %(myCar3.color, myCar3.speed))

myCar1.upSpeed(10)
myCar2.downSpeed(20)
myCar3.upSpeed(30)

print("myCar1 : %s, %d" %(myCar1.color, myCar1.speed))
print("myCar2 : %s, %d" %(myCar2.color, myCar2.speed))
print("myCar3 : %s, %d" %(myCar3.color, myCar3.speed))


class Car:

    
    color = ""
    speed = 0 

    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2
    
    def upSpeed(self, value) :
        self.speed += value


    def downSpeed(self, value) :

        self.speed -= value



myCar1 = Car("빨강", 10)

myCar2 = Car("파랑", 20)

myCar3 = Car("노랑", 30)


print("myCar1 : %s, %d" %(myCar1.color, myCar1.speed))
print("myCar2 : %s, %d" %(myCar2.color, myCar2.speed))
print("myCar3 : %s, %d" %(myCar3.color, myCar3.speed))

myCar1.upSpeed(10)
myCar2.downSpeed(20)
myCar3.upSpeed(30)

print("myCar1 : %s, %d" %(myCar1.color, myCar1.speed))
print("myCar2 : %s, %d" %(myCar2.color, myCar2.speed))
print("myCar3 : %s, %d" %(myCar3.color, myCar3.speed))


#과제_클래스 오버라이딩

class Car:

    
    color = ""
    speed = 0 

    
    def upSpeed(self, value) :
        self.speed += value


    def downSpeed(self, value) :

        self.speed -= value

class Sedan(Car):
    seat = 0

    def getSeat(self):
        return seat

    def upSpeed(self, value):
        self.speed += value + 30

mySedan = Sedan()

mySedan.color = "빨강"
mySedan.speed = 10
mySedan.seat = 5

print("mySedan : %s, %d, %d" %(mySedan.color, mySedan.speed, mySedan.seat))

mySedan.upSpeed(50)

print("mySedan : %s, %d, %d" %(mySedan.color, mySedan.speed, mySedan.seat))
