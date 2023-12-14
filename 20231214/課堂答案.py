import json
import os
 
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}
 
    def add_course(self, course_code, course_name, semester):
        if semester not in self.courses:
            self.courses[semester] = []
        self.courses[semester].append({"code": course_code, "name": course_name})
 
    def delete_course(self, course_code, semester):
        if semester in self.courses and any(course["code"] == course_code for course in self.courses[semester]):
            self.courses[semester] = [course for course in self.courses[semester] if course["code"] != course_code]
            print(f"Course {course_code} deleted for {self.name} in semester {semester}.")
        else:
            print(f"Course {course_code} not found for {self.name} in semester {semester}.")
 
    def get_courses_by_semester(self, semester):
        return self.courses.get(semester, [])
 
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            data = {
                "student_id": self.student_id,
                "name": self.name,
                "courses": self.courses
            }
            json.dump(data, file)
 
    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self.student_id = data["student_id"]
                self.name = data["name"]
                self.courses = data["courses"]
        else:
            print(f"File {filename} not found. Creating a new student profile.")
 
# Example usage:
student_id = "123456"
student_name = "John Doe"
student_filename = f"{student_id}_profile.json"
 
# Create or load student profile
student = Student(student_id, student_name)
student.load_from_file(student_filename)
 
# Add courses
student.add_course("CS101", "Introduction to Computer Science", "Fall 2023")
student.add_course("ENG201", "English Literature", "Fall 2023")
 
# Save the updated profile to file
student.save_to_file(student_filename)
 
# Display courses for a specific semester
semester_to_search = "Fall 2023"
courses_taken = student.get_courses_by_semester(semester_to_search)
print(f"Courses taken by {student_name} in {semester_to_search}:")
for course in courses_taken:
    print(f"{course['code']}: {course['name']}")
 
# Delete a course
course_to_delete = "CS101"
student.delete_course(course_to_delete, semester_to_search)
 
# Save the updated profile after course deletion
student.save_to_file(student_filename)