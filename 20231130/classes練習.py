class Student:

    def __init__(self,School,Department,Grade,Name,ID,Credit,Score,School_Address,student_Address):
        self.school=School
        self.department=Department
        self.grade=Grade
        self.credit=Credit
        self.score=Score
        self.name=Name
        self.school_Address=School_Address
        self.student_Address=student_Address
        self.id=ID

    def getSchoolName(self,School):
        return self.school

    def setSchoolName(self,new_School):
        self.school=new_School
        

    def getDepartment(self,Department):
        return self.department

    def setDepartment(self,new_Department):
        self.department=new_Department


    def getGrade(self,Grade):
        return self.grade

    def setGrade(self,new_Grade):
        self.grade=new_Grade
    
    def getName(self,Name):
        return self.name
    
    def setName(self,new_Name):
        self.name=new_Name

    def getID(self,ID):
        return self.id

    def setID(self,new_ID):
        self.id=new_ID

    def getCredit(self,Credit):
        return self.credit
    
    def setCredit(self,new_Credit):
        self.credit=new_Credit

    def getScore(self,Score):
        return self.score
    
    def setScore(self,new_Score):
        self.score=new_Score

    def getSchoolAddress(self,SchoolAddress):
        return self.school_Address
    
    def setSchoolAddress(self,new_SchoolAddress):
        self.school_Address=new_SchoolAddress

    def getStudentAddress(self,StuedntAddress):
        return self.student_Address
    
    def setStudentAddress(self,new_StuedntAddress):
        self.student_Address=new_StuedntAddress

