class Car :
    color = ""
    speed = 0

    def upSpeed(self, value) :
        if self.speed + value > 150:
            self.speed = 150
        else:
            self.speed += value

    def downSpeed(self, value) :
        self.speed -= value


myCar = Car()
myCar.color = "검정"
myCar.speed = 100

myCar.upSpeed(200)  
print("자동차의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar.color, myCar.speed))
