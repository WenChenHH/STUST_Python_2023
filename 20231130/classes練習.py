class Student:
    schoolName = "南台科技大學"
    schoolAddress="南台街1號"

    def __init__(self,major,grade,name,id,credit,score,student_Address):
        self._major=major
        self._grade=grade
        self._credit=credit
        self._score=score
        self._name=name
        self._student_Address=student_Address
        self._id=id
    
    def getSchoolName(self):
        return self.schoolName
    
    def setSchoolName(self,new_school):
        self.schoolName=new_school
    # @property
    # def school_name(self):
    #     return self._school
    # @school_name.setter
    # def school_name(self,value):
    #     self._school = value
    # @school_name.deleter
    # def school_name(self):
    #     del self._school

    def getmajor(self):
        return self._major

    def setmajor(self,new_major):
        self._major=new_major


    def getGrade(self):
        return self._grade

    def setGrade(self,new_grade):
        self._grade=new_grade
    
    def getName(self):
        return self._name
    
    def setName(self,new_name):
        self._name=new_name

    def getID(self,):
        return self._id

    def setID(self,new_id):
        self._id=new_id

    def getCredit(self):
        return self._credit
    
    def setCredit(self,new_credit):
        self._credit=new_credit

    def getScore(self):
        return self._score
    
    def setScore(self,new_score):
        self._score=new_score

    def getSchoolAddress(self):
        return self.schoolAddress
    
    def setSchoolAddress(self,new_schoolAddress):
        self.schoolAddress=new_schoolAddress

    def getStudentAddress(self):
        return self._student_Address
    
    def setStudentAddress(self,new_stuedntAddress):
        self._student_Address=new_stuedntAddress

st1=Student("資訊工程系","三年乙班","黃文震","4B0G0045",40,100,"台南市")
print(st1.getSchoolName())
print(st1.getSchoolAddress())
st1.setSchoolName("stust")
print(st1.getSchoolName())
