class Myshape:
    def __init__(self,length,width,side,radius):
        self.length=int(length)
        self.width=int(width)
        self.side=int(side)
        self.radius=float(radius)
    def __rectangle__(self):
        area = self.length*self.width
        return print(f"長方形面積={area}")
    def __square__(self):
       area=self.side*self.side
       return print(f"正方形面積={area}")
    def __round__(self):
        area=self.radius**2*3.14
        return print(f"圓形形面積={area}")
#-----------------用另一種方式寫---------------
class test :
    def rectangle(length,width):
        area = float(length)*float(width)
        return print(f"長方形面積={area}")
    def square(side):
       area=float(side)*float(side)
       return print(f"正方形面積={area}")
    def round(radius):
        area=float(radius)**2*3.14
        return print(f"圓形形面積={area}")
E =Myshape(input("請輸入長(CM):"),input("請輸入寬(CM):"),input("請輸入正方形邊長(CM):"),input("請輸入半徑(CM):"))

E.__rectangle__()
E.__square__()
E.__round__()

A=test
A.rectangle(input("請輸入長(CM):"),input("請輸入寬(CM):"))
A.square(input("請輸入正方形邊長(CM):"))
A.round(input("請輸入半徑(CM):"))




    
        

