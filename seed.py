from datetime import datetime
from random import randint

import faker

from models_tables import Group, Student, Teacher, Subject, StudentGrade
from db_connection import session
from sqlalchemy.exc import SQLAlchemyError

#переменные константы для создания БД
NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 5
NAME_GROUPS = ['First', 'Second', 'Third']
FACULTY = 'Engeneering'
NAME_SUBJECTS = ['Математика', 'Фізика', 'Программування', 'Англійська мова', 'Українська мова']

fake = faker.Faker('uk-UA')


#функция заполнения БД данными
def insert_data_to_db():
    def seed_groups():
        for group in NAME_GROUPS:
            session.add(Group(group_name=group, faculty=FACULTY))
        session.commit()

    def seed_students():
        for _ in range(NUMBER_STUDENTS):
            student = Student(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email(), group_id = randint(1,NUMBER_GROUPS))
            session.add(student)
        session.commit()

    def seed_teachers():
        for _ in range(NUMBER_TEACHERS):
            teacher = Teacher(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.email())
            session.add(teacher)
        session.commit()

    def seed_subjects():
        for sub in NAME_SUBJECTS:
            session.add(Subject(subject_name=sub, teacher_id = NAME_SUBJECTS.index(sub) + 1 ))
        session.commit()

    def seed_student_grades():
        for _ in range(NUMBER_STUDENTS):
            data = datetime(2023, randint(1, 6), randint(1, 27)).date()
            student_grade = StudentGrade(student_id=randint(1,NUMBER_STUDENTS), subject_id=randint(1, NUMBER_SUBJECTS), grade=randint(1, 12), date_received = data)
            session.add(student_grade)
        session.commit()
    
    seed_groups()
    seed_students()
    seed_teachers()
    seed_subjects()
    seed_student_grades()

if __name__ == '__main__':
    try:
        insert_data_to_db()
    except SQLAlchemyError as err:
        session.rollback()
        print(err)
    finally:
        session.close()