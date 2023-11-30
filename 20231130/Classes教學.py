#類別
class cars:
    #建構式
    def __init__(self,color,seat):
        self.color = color
        self.seat = seat

    #方法
    def drive(self):
        print(f"My car is {self.color} and has {self.seat} seats.")



mazda = cars() #建立物件類別
mazda.color = "blue" #顏色屬性
mazda.seat = 4  #座位屬性
