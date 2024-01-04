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
    
    def limbs_combo(self):
        print(f"你已成功點了套餐 {self.drumsitck}, {self.chicken_wings}, {self.breast}")
    
    def whole_chicken_combo(self):
        print(f"你已成功點了套餐 {self.whole_chicken}")
    
    def half_chicken_combo(self):
        print(f"你已成功點了套餐 {self.half_chicken}")

# 建立三個物件
chicken1 = FrieChicken("雞胸", "雞腿", "雞翅", "半隻雞", "整隻雞")
chicken2 = FrieChicken("辣炸雞胸", "香烤雞腿", "孜然雞翅", "半隻香烤雞", "香烤整隻雞")
chicken3 = FrieChicken("椒鹽雞胸", "蜜汁雞腿", "檸檬雞翅", "半隻椒鹽雞", "椒鹽整隻雞")

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