class FrieChicken:
    def __init__(self, chicken_breast, drumsitck, chicken_wings, half_chicken, whole_chicken):
        # 雞胸
        self.breast = chicken_breast
        # 雞腿
        self.drumsitck = drumsitck
        # 雞翅
        self.chicken_wings = chicken_wings
        # 半雞
        self.half_chicken = half_chicken
        # 全雞
        self.whole_chicken = whole_chicken
    
    def limbs_combo(self):#套餐選擇
        print(f"你已成功點了套餐 {self.drumsitck}, {self.chicken_wings}, {self.breast}")
    
    def whole_chicken_combo(self):
        print(f"你已成功點了套餐 {self.whole_chicken}")
    
    def half_chicken_combo(self):
        print(f"你已成功點了套餐 {self.half_chicken}")

# 建立三個物件
chicken1 = FrieChicken("原味雞胸", "原味雞腿", "原味雞翅", "原味半隻雞", "原味全雞")
chicken2 = FrieChicken("孜然雞胸", "孜然雞腿", "孜然雞翅", "半隻香草雞", "香草全雞")
chicken3 = FrieChicken("椒鹽雞胸", "椒鹽雞腿", "椒鹽雞翅", "半隻椒鹽雞", "椒鹽全雞")
chicken4 = FrieChicken("麻辣雞胸", "麻辣雞腿", "麻辣雞翅", "半隻麻辣雞", "麻辣全雞")

# 呼叫物件方法
chicken1.limbs_combo()
chicken1.half_chicken_combo()
chicken1.whole_chicken_combo()
print("")
chicken2.limbs_combo()
chicken2.half_chicken_combo()
chicken2.whole_chicken_combo()
print("")
chicken3.limbs_combo()
chicken3.half_chicken_combo()
chicken3.whole_chicken_combo()
print("")
chicken4.limbs_combo()
chicken4.half_chicken_combo()
chicken4.whole_chicken_combo()