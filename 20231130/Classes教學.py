#類別
class cars:
    #建構式
    def __init__(self,color,seat):
        self.color = color
        self.seat = seat

    #方法
    def drive(self):
        print(f"My car is {self.color} and {self.seat} seats.") 



T1=cars("blue",4)

T1.drive

