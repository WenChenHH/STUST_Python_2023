class stust_csie_drink:
    def __init__(self, name, seniority, work_hours):
        self.name = name #員工名字
        self.seniority = seniority #年薪
        self.work_hours = work_hours #工作的時數
        self.drink = None  

    def query_name(self):
        return self.name#查詢名字的時候可以躑回參數

    def query_seniority(self):
        return self.seniority#查詢年薪的時候可以躑回

    def query_work_hours(self):
        return self.work_hours#工時

    def calculate_monthly_salary(self):
        # 假設每小時工資為200元
        hourly_wage = 200
        return hourly_wage * self.work_hours

    def add_work_hours(self, additional_hours):
        self.work_hours += additional_hours

    def add_seniority(self, additional_years):
        self.seniority += additional_years

    def assign_drink(self, drink):
        self.drink = drink

class Drink:
    def __init__(self, price, is_large, is_small):
        self.price = price
        self.is_large = is_large
        self.is_small = is_small


class ColdDrink(Drink):#冷飲
    def __init__(self, name, ice_level, sweetness):
        super().__init__(price=0, is_large=False, is_small=False)
        self.name = name
        self.ice_level = ice_level
        self.sweetness = sweetness


class HotDrink(Drink):#熱飲
    def __init__(self, name, ice_level, sweetness):
        super().__init__(price=0, is_large=False, is_small=False)
        self.name = name
        self.ice_level = ice_level
        self.sweetness = sweetness



# 給一個stust_csie_drink的參數
employee1 = stust_csie_drink("John",5,80)

# 給一個 ColdDrink 的參數
cold_drink1 = ColdDrink("冰紅茶","少冰","中糖")

# 將飲料指派給員工
employee1.assign_drink(cold_drink1)

# 列印員工資訊和所選擇的飲料資訊
print(f"員工姓名：{employee1.query_name()}")
print(f"員工年資：{employee1.query_seniority()} 年")
print(f"員工工時：{employee1.query_work_hours()} 小時")
print(f"員工月薪：{employee1.calculate_monthly_salary()} 元")

if employee1.drink is not None:
    print("\n所選擇的飲料資訊:")
    print(f"飲料名稱：{employee1.drink.name}")
    print(f"冰量：{employee1.drink.ice_level}")
    print(f"甜度：{employee1.drink.sweetness}")
else:
    print("\n員工尚未選擇飲料。")
