import pprint
from sqlalchemy import func, desc, and_, select

from models_tables import Group, Student, Teacher, Subject, StudentGrade
from db_connection import session

def select_1():
    result = session.query(Student.first_name, Student.last_name, func.round(func.avg(StudentGrade.grade), 2).label('avg_grade'))\
                           .select_from(Student).join(StudentGrade).group_by(StudentGrade.student_id, Student.first_name, Student.last_name)\
                            .order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2(subject_id):
    result = session.query(Subject.subject_name, Student.first_name, Student.last_name, func.round(func.avg(StudentGrade.grade), 2).label('avg_grade'))\
                            .select_from(StudentGrade).join(Student).join(Subject).filter(Subject.subject_id == subject_id).group_by(Student.student_id, Subject.subject_name)\
                            .order_by(desc('avg_grade')).limit(1).all() #
    return result
  

def select_3():
    result = session.query(Group.group_name, Subject.subject_name, func.round(func.avg(StudentGrade.grade), 2).label('avg_grade'))\
                          .select_from(Student).join(Group).join(StudentGrade).join(Subject).group_by(Subject.subject_name, Group.group_name)\
                          .order_by(desc(Group.group_name)).all()
    return result


def select_4():
    result = session.query(func.avg(StudentGrade.grade).label('avg_grade')).select_from(StudentGrade).all()
    return result

def select_5():
    result = session.query(Subject.subject_name, Teacher.first_name, Teacher.last_name)\
                            .select_from(Subject).join(Teacher).all()
    return result

def select_6():
    result = session.query(Student.first_name, Student.last_name, Group.group_name)\
                            .select_from(Student).join(Group).order_by(Group.group_name).all()
    return result

def select_7():
    result = session.query(Student.first_name, Student.last_name, Group.group_name, Subject.subject_name, StudentGrade.grade)\
                            .select_from(Student).join(Group).join(StudentGrade).join(Subject).order_by(Group.group_name).order_by(Subject.subject_name).all()
    return result
 
def select_8():
    result = session.query(Subject.subject_name, Teacher.first_name, Teacher.last_name, func.round(func.avg(StudentGrade.grade), 2).label('avg_grade'))\
                            .select_from(Subject).join(Teacher).join(StudentGrade).group_by(Subject.subject_name, Teacher.first_name, Teacher.last_name)\
                            .order_by(Subject.subject_name).all()
    return result

def select_9():
    result = session.query(Student.first_name, Student.last_name, Subject.subject_name).select_from(Student)\
                            .join(StudentGrade).join(Subject).order_by(Student.first_name).all()
    return result

def select_10():
    result = session.query(Student.first_name, Student.last_name, Subject.subject_name, Teacher.first_name, Teacher.last_name)\
                            .select_from(Student).join(StudentGrade).join(Subject).join(Teacher).order_by(Student.first_name).all()
    return result


#Дополнительное задание часть 1
def select_add_1():
    result = session.query(Student.first_name, Student.last_name, func.round(func.avg(StudentGrade.grade), 2).label('avg_grade'),\
                    Teacher.first_name, Teacher.last_name).select_from(Student).join(StudentGrade).join(Subject).join(Teacher)\
                    .group_by(Subject.subject_name, Student.first_name, Student.last_name, Teacher.first_name, Teacher.last_name)\
                    .order_by(Student.first_name).all()
    return result

def select_add_2():
    subquery = (select(StudentGrade.subject_id, func.max(StudentGrade.date_received).label('max_date')).group_by(StudentGrade.subject_id).subquery())
    result = session.query(Student.first_name, Student.last_name, Group.group_name, Subject.subject_name, StudentGrade.grade, StudentGrade.date_received)\
            .select_from(Student).join(Group).join(StudentGrade).join(Subject)\
            .join(subquery, and_(Subject.subject_id == subquery.c.subject_id, StudentGrade.date_received == subquery.c.max_date))\
            .order_by(desc(StudentGrade.date_received), Subject.subject_name).all()
    return result



if __name__ == '__main__':
    pprint.pprint(select_add_2())

