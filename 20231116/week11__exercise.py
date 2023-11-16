class Myshape:
    def __init__(self,length,width,side,radius):
        self.length=length
        self.width=width
        self.side=side
        self.radius=radius
    def __rectangle__(self):
        area = self.length*self.width
        return print(f"長方形面積={area}")
    def __square__(self):
       area=self.side*self.side
       return print(f"正方形面積={area}")
    def __round__(self):
        area=self.radius**2*3.14
        return print(f"圓形形面積={area}")
    
E =Myshape(4,3,5,6)

E.__rectangle__()
E.__square__()
E.__round__()

    

    
        

