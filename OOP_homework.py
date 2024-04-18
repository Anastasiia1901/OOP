class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def get_average_grade(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
            if all_grades != 0:
                return sum(all_grades) / len(all_grades)
            else:
                return 0

    def __lt__(self, student):
        if self.get_average_grade() < student.get_average_grade():
            return True
        else:
            return False

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        res += f'Средняя оценка за домашние задания: {self.get_average_grade()}\n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []
    def get_average_grade(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
            if all_grades != 0:
                return sum(all_grades) / len(all_grades)
            else:
                return 0

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        res += f'Средняя оценка за лекции: {self.get_average_grade()}\n'
        return res
    def __lt__(self, lecturer):
        if self.get_average_grade() < lecturer.get_average_grade():
            return True
        else:
            return False

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res

student_1 = Student('Иван', 'Денисов', 'мужчина')
student_1.courses_in_progress += ['Java-разработчик']
student_1.courses_in_progress += ['Python-разработчик']
student_1.finished_courses += ['Основы языка программирования Python']

student_2 = Student('Елена', 'Белова', 'женщина')
student_2.courses_in_progress += ['Fullstack-разработчик на Python']
student_2.courses_in_progress += ['Frontend-разработчик']
student_2.finished_courses += ['Основы языка программирования Python']

student_3 = Student('Василий', 'Петров', 'мужчина')
student_3.courses_in_progress += ['Java-разработчик']
student_3.courses_in_progress += ['Frontend-разработчик']
student_3.finished_courses += ['Основы языка программирования Python']

lecturer_1 = Lecturer('Кирилл', 'Булатов')
lecturer_1.courses_attached += ['Java-разработчик']
lecturer_1.courses_attached += ['Python-разработчик']

lecturer_2 = Lecturer('Александр', 'Титов')
lecturer_2.courses_attached += ['Fullstack-разработчик на Python']
lecturer_2.courses_attached += ['Основы языка программирования Python']
lecturer_2.courses_attached += ['Frontend-разработчик']

reviewer_1 = Reviewer('Василий', 'Соколов')
reviewer_1.courses_attached += ['Java-разработчик']
reviewer_1.courses_attached += ['Python-разработчик']

reviewer_2 = Reviewer('Филипп', 'Ежов')
reviewer_2.courses_attached += ['Fullstack-разработчик на Python']
reviewer_2.courses_attached += ['Frontend-разработчик']

student_1.rate_lecturer(lecturer_1, 'Java-разработчик', 9)
student_1.rate_lecturer(lecturer_1, 'Java-разработчик', 8)
student_1.rate_lecturer(lecturer_1, 'Python-разработчик', 7)
student_1.rate_lecturer(lecturer_1, 'Python-разработчик', 10)

student_2.rate_lecturer(lecturer_2, 'Fullstack-разработчик на Python', 10)
student_2.rate_lecturer(lecturer_2, 'Fullstack-разработчик на Python', 9)
student_2.rate_lecturer(lecturer_2, 'Frontend-разработчик', 8)
student_2.rate_lecturer(lecturer_2, 'Frontend-разработчик', 7)

student_3.rate_lecturer(lecturer_1, 'Java-разработчик', 10)
student_3.rate_lecturer(lecturer_1, 'Java-разработчик', 7)
student_3.rate_lecturer(lecturer_2, 'Frontend-разработчик', 8)
student_3.rate_lecturer(lecturer_2, 'Frontend-разработчик', 6)

reviewer_1.rate_hw(student_1, 'Java-разработчик', 7)
reviewer_1.rate_hw(student_1, 'Java-разработчик', 8)
reviewer_1.rate_hw(student_1, 'Python-разработчик', 9)
reviewer_1.rate_hw(student_1, 'Python-разработчик', 10)
reviewer_1.rate_hw(student_3, 'Java-разработчик', 6)
reviewer_1.rate_hw(student_3, 'Java-разработчик', 9)

reviewer_2.rate_hw(student_2, 'Fullstack-разработчик на Python', 7)
reviewer_2.rate_hw(student_2, 'Fullstack-разработчик на Python', 9)
reviewer_2.rate_hw(student_2, 'Frontend-разработчик', 8)
reviewer_2.rate_hw(student_2, 'Frontend-разработчик', 9)
reviewer_2.rate_hw(student_3, 'Frontend-разработчик', 10)
reviewer_2.rate_hw(student_3, 'Frontend-разработчик', 8)


print(student_1)
print(student_2)
print(student_3)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

list_of_lecturers = [lecturer_1, lecturer_2]
list_of_students = [student_1, student_2, student_3]

def average_rating_hw(list_of_students, course_name):
  all_grades = []
  for student in list_of_students:
    if course_name in student.grades:
      all_grades += student.grades[course_name]
      if all_grades != 0:
        return sum(all_grades) / len(all_grades)
      else:
        return 0

print(f"Средняя оценка за домашние задания по всем студентм по курсу {'Java-разработчик'}: {average_rating_hw(list_of_students, 'Java-разработчик')}")
print(f"Средняя оценка за домашние задания по всем студентм по курсу {'Python-разработчик'}: {average_rating_hw(list_of_students, 'Python-разработчик')}")
print(f"Средняя оценка за домашние задания по всем студентм по курсу {'Fullstack-разработчик на Python'}: {average_rating_hw(list_of_students, 'Fullstack-разработчик на Python')}")
print(f"Средняя оценка за домашние задания по всем студентм по курсу {'Frontend-разработчик'}: {average_rating_hw(list_of_students, 'Frontend-разработчик')}")

def average_rating_lecture(list_of_lecturers, course_name):
  all_grades = []
  for lecture in list_of_lecturers:
    if course_name in lecture.grades:
      all_grades += lecture.grades[course_name]
      if all_grades != 0:
        return sum(all_grades) / len(all_grades)
      else:
        return 0

print(f"Средняя оценка за лекции всех лекторов по курсу {'Java-разработчик'}: {average_rating_lecture(list_of_lecturers, 'Java-разработчик')}")
print(f"Средняя оценка за лекции всех лекторов по курсу {'Python-разработчик'}: {average_rating_lecture(list_of_lecturers, 'Python-разработчик')}")
print(f"Средняя оценка за лекции всех лекторов по курсу {'Fullstack-разработчик на Python'}: {average_rating_lecture(list_of_lecturers, 'Fullstack-разработчик на Python')}")
print(f"Средняя оценка за лекции всех лекторов по курсу {'Frontend-разработчик'}: {average_rating_lecture(list_of_lecturers, 'Frontend-разработчик')}")


