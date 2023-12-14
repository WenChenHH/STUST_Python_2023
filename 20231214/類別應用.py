class Student:
    def __init__(self, name, id, mojor, course):
        self.name = name
        self.id = id
        self.mojor = mojor
        self.course = course  

    @property
    def student_name(self):
        return self.name

    @student_name.setter
    def student_name(self, value):
        self.name = value

    @property
    def student_id(self):
        return self.id

    @student_id.setter
    def student_id(self, value):
        self.id = value

    @property
    def student_mojor(self):
        return self.mojor
    
    @student_mojor.setter
    def student_mojor(self, value):
        self.mojor = value

    class Student_Course:
        def __init__(self, course):
            self._course = [course]

        def student_course(self, value):
            self._course.append(value)

        def delete_course(self):
            print("已刪除")
            del self._course

# 測試
test = Student("Wen", "4b0g0045", "資工系", Student.Student_Course("Python"))
test.course.student_course("計算機數學")
test.course.student_course("C++")
print(test.student_name, "  ", test.student_id, "  ", test.student_mojor)
print(test.course._course)  # 注意這裡直接訪問 _course，因為 student_course 是一個方法

# 刪除課程
test.course.delete_course()
