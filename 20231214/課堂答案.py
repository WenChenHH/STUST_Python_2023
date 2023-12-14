import json
import os

class Student:
    def __init__(self, student_id, name):
        # 初始化學生物件，設定學號、姓名和課程資料結構
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def add_course(self, course_code, course_name, semester):
        # 新增課程至指定學期
        if semester not in self.courses:
            self.courses[semester] = []
        self.courses[semester].append({"code": course_code, "name": course_name})

    def delete_course(self, course_code, semester):
        # 刪除指定學期的課程
        if semester in self.courses and any(course["code"] == course_code for course in self.courses[semester]):
            self.courses[semester] = [course for course in self.courses[semester] if course["code"] != course_code]
            print(f"{self.name} 在 {semester} 學期刪除了課程 {course_code}。")
        else:
            print(f"{self.name} 在 {semester} 學期找不到課程 {course_code}。")

    def get_courses_by_semester(self, semester):
        # 取得指定學期的課程列表
        return self.courses.get(semester, [])

    def save_to_file(self, filename):
        # 將學生物件儲存至檔案
        with open(filename, 'w') as file:
            data = {
                "student_id": self.student_id,
                "name": self.name,
                "courses": self.courses
            }
            json.dump(data, file)

    def load_from_file(self, filename):
        # 從檔案載入學生資訊
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self.student_id = data["student_id"]
                self.name = data["name"]
                self.courses = data["courses"]
        else:
            print(f"檔案 {filename} 不存在。建立新的學生檔案。")

# 範例使用:
student_id = "123456"
student_name = "John Doe"
student_filename = f"{student_id}_profile.json"

# 建立或載入學生檔案
student = Student(student_id, student_name)
student.load_from_file(student_filename)

# 新增課程
student.add_course("CS101", "Introduction to Computer Science", "Fall 2023")
student.add_course("ENG201", "English Literature", "Fall 2023")

# 儲存更新後的檔案
student.save_to_file(student_filename)

# 顯示特定學期的課程
semester_to_search = "Fall 2023"
courses_taken = student.get_courses_by_semester(semester_to_search)
print(f"{student_name} 在 {semester_to_search} 學期修習的課程:")
for course in courses_taken:
    print(f"{course['code']}: {course['name']}")

# 刪除一門課程
course_to_delete = "CS101"
student.delete_course(course_to_delete, semester_to_search)

# 在刪除課程後儲存更新後的檔案
student.save_to_file(student_filename)
