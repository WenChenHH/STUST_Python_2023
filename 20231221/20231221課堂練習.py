import sys
import json
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTabWidget, QTextBrowser, QMessageBox
from PyQt6.QtCore import Qt
from openpyxl import Workbook

class Student:
    def __init__(self, student_id, name, connection):
        self.student_id = student_id
        self.name = name
        self.courses = {}
        self.connection = connection

    def add_course(self, course_code, course_name, semester):
        if semester not in self.courses:
            self.courses[semester] = []
        self.courses[semester].append({"code": course_code, "name": course_name})

    def query_course_info(self, semester):
        if semester in self.courses:
            courses_in_semester = self.courses[semester]
            return f"{self.name}在{semester}學期修過的課程:", courses_in_semester
        else:
            return f"{self.name}在{semester}學期沒有找到任何課程。", None

    def get_all_courses_info(self):
        all_courses_info = []
        for semester, courses in self.courses.items():
            for course in courses:
                all_courses_info.append({
                    "學號": self.student_id,
                    "姓名": self.name,
                    "學期": semester,
                    "課程代碼": course["code"],
                    "課程名稱": course["name"]
                })
        return all_courses_info

    def save_to_database(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO students (student_id, name) VALUES (?, ?)", (self.student_id, self.name))

        for semester, courses in self.courses.items():
            for course in courses:
                cursor.execute("INSERT INTO courses (student_id, semester, course_code, course_name) VALUES (?, ?, ?, ?)",
                               (self.student_id, semester, course["code"], course["name"]))

        self.connection.commit()

    def load_from_database(self):
        cursor = self.connection.cursor()

        # 載入學生資訊
        cursor.execute("SELECT * FROM students WHERE student_id=?", (self.student_id,))
        student_data = cursor.fetchone()
        if student_data:
            self.name = student_data[1]

        # 載入課程資訊
        cursor.execute("SELECT * FROM courses WHERE student_id=?", (self.student_id,))
        courses_data = cursor.fetchall()
        for course_data in courses_data:
            semester = course_data[1]
            course_code = course_data[2]
            course_name = course_data[3]
            self.add_course(course_code, course_name, semester)

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            student_id TEXT,
            semester TEXT,
            course_code TEXT,
            course_name TEXT,
            PRIMARY KEY (student_id, semester, course_code),
            FOREIGN KEY (student_id) REFERENCES students (student_id)
        )
    ''')
    connection.commit()

def generate_sample_data(connection):
    sample_students = []
    for i in range(10):
        student_id = f"STUST{i+1:03d}"
        name = f"學生{i+1}"
        student = Student(student_id, name, connection)
        for course_code, course_name in [("Python", "Python程式設計"), ("Java", "Java程式設計"),
                                         ("C++", "C++程式設計"), ("JavaScript", "JavaScript程式設計"),
                                         ("Database", "資料庫管理"), ("OS", "作業系統")]:
            semester = "2023年秋季"
            student.add_course(course_code, course_name, semester)

        student.save_to_database()
        sample_students.append(student)

    return sample_students

class StudentGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.connection = sqlite3.connect('students.db')
        create_tables(self.connection)

        self.init_ui()

    def init_ui(self):
        self.tabs = QTabWidget()

        self.add_course_tab = self.create_add_course_tab()
        self.query_course_tab = self.create_query_course_tab()
        self.display_all_tab = self.create_display_all_tab()

        self.tabs.addTab(self.add_course_tab, "新增課程")
        self.tabs.addTab(self.query_course_tab, "查詢課程")
        self.tabs.addTab(self.display_all_tab, "顯示所有學生")

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('STUST 學生資訊及課程查詢工具')

    def create_add_course_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.student_id_label_add = QLabel('學號:')
        self.student_id_edit_add = QLineEdit()
        self.name_label_add = QLabel('姓名:')
        self.name_edit_add = QLineEdit()

        self.course_code_label_add = QLabel('課程代碼:')
        self.course_code_edit_add = QLineEdit()
        self.course_name_label_add = QLabel('課程名稱:')
        self.course_name_edit_add = QLineEdit()
        self.add_course_button_add = QPushButton('新增課程')

        self.add_course_button_add.clicked.connect(self.add_course)

        layout.addWidget(self.student_id_label_add)
        layout.addWidget(self.student_id_edit_add)
        layout.addWidget(self.name_label_add)
        layout.addWidget(self.name_edit_add)
        layout.addWidget(self.course_code_label_add)
        layout.addWidget(self.course_code_edit_add)
        layout.addWidget(self.course_name_label_add)
        layout.addWidget(self.course_name_edit_add)
        layout.addWidget(self.add_course_button_add)

        tab.setLayout(layout)
        return tab

    def create_query_course_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.student_id_label_query = QLabel('學號:')
        self.student_id_edit_query = QLineEdit()
        self.semester_label_query = QLabel('學期:')
        self.semester_edit_query = QLineEdit()
        self.query_button_query = QPushButton('查詢課程')
        self.result_browser_query = QTextBrowser()

        self.query_button_query.clicked.connect(self.query_courses)

        layout.addWidget(self.student_id_label_query)
        layout.addWidget(self.student_id_edit_query)
        layout.addWidget(self.semester_label_query)
        layout.addWidget(self.semester_edit_query)
        layout.addWidget(self.query_button_query)
        layout.addWidget(self.result_browser_query)

        tab.setLayout(layout)
        return tab

    def create_display_all_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        self.query_button_display_all = QPushButton('顯示所有學生')
        self.result_browser_display_all = QTextBrowser()

        self.query_button_display_all.clicked.connect(self.display_all_students)

        layout.addWidget(self.query_button_display_all)
        layout.addWidget(self.result_browser_display_all)

        tab.setLayout(layout)
        return tab

    def add_course(self):
        student_id = self.student_id_edit_add.text()
        name = self.name_edit_add.text()
        course_code = self.course_code_edit_add.text()
        course_name = self.course_name_edit_add.text()

        # 檢查缺少的輸入資料
        if not student_id or not name or not course_code or not course_name:
            self.show_alert("缺少資料", "請填寫所有欄位。")
            return

        # 創建或載入學生檔案
        student = Student(student_id, name, self.connection)
        student.load_from_database()

        semester = "2023年"  # 簡單起見，將預設學期設為2023年秋季

        # 將課程新增至學生檔案
        student.add_course(course_code, course_name, semester)

        # 將學生課程資訊儲存至資料庫
        student.save_to_database()

        # 顯示成功的訊息視窗
        self.show_success_message("課程已新增", "課程已成功新增。")

    def query_courses(self):
        student_id = self.student_id_edit_query.text()
        semester = self.semester_edit_query.text()

        # 檢查缺少的輸入資料
        if not student_id or not semester:
            self.show_alert("缺少資料", "請填寫所有欄位。")
            return

        # 創建或載入學生檔案
        student = Student(student_id, "", self.connection)
        student.load_from_database()

        # 查詢課程資訊
        result_message, courses_info = student.query_course_info(semester)

        # 在QTextBrowser中顯示結果
        self.result_browser_query.setPlainText(result_message)
        if courses_info:
            for course in courses_info:
                self.result_browser_query.append(f"{course['課程代碼']}: {course['課程名稱']}")

    def display_all_students(self):
        # 產生至少10位STUST學生的範例資料
        sample_students = generate_sample_data(self.connection)

        # 在QTextBrowser中顯示所有學生課程資訊
        self.result_browser_display_all.clear()
        for student in sample_students:
            courses_info = student.get_all_courses_info()
            for info in courses_info:
                self.result_browser_display_all.append(f"{info['學號']} - {info['姓名']}:")
                self.result_browser_display_all.append(f"  學期: {info['學期']}")
                self.result_browser_display_all.append(f"  {info['課程代碼']}: {info['課程名稱']}")

    def show_alert(self, title, message):
        alert = QMessageBox()
        alert.setWindowTitle(title)
        alert.setText(message)
        alert.exec()

    def show_success_message(self, title, message):
        success_message = QMessageBox()
        success_message.setWindowTitle(title)
        success_message.setText(message)
        success_message.exec()

def main():
    app = QApplication(sys.argv)
    gui = StudentGUI()
    gui.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
