
# # 汽車類別
# class Cars:
#     # 建構式
#     def __init__(self, color, seat):
#         self.color = color  # 顏色屬性
#         self.seat = seat  # 座位屬性
# mazda = Cars("blue", 4)



# # 汽車類別
# class Cars:
#     pass
# # 摩托車類別
# class Motorcycle:
#     pass
# # 建立Cars類別的物件
# mazda = Cars()
# mazda.color = "blue"  #顏色屬性 
# mazda.seat = 4  #座位屬性
# print(isinstance(mazda, Cars))  # 執行結果：True
# print(isinstance(mazda, Motorcycle))  # 執行結果：False
#print(mazda.color)  # 執行結果：blue
#print(mazda.seat)  # 執行結果：4





# # 汽車類別
# class Cars:
#     # 建構式
#     def __init__(self, color, seat):
#         self.color = color  # 顏色屬性
#         self.seat = seat  # 座位屬性
#     # 方法(Method)
#     def drive(self):
#         print(f"My car is {self.color} and {self.seat} seats.")


#類別
class cars:
    #建構式
    def __init__(self,color,seat):
        self.color = color
        self.seat = seat

    #方法
    def drive(self):
        print(f"My car is {self.color} and has {self.seat} seats.")

mazda = cars("Red",5)
mazda.drive()
