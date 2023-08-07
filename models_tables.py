from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship

from db_connection import engine

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(50), nullable=True)
    faculty = Column(String(50), nullable=False)


class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    email = Column(String(100), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.group_id', ondelete='CASCADE'))
    group = relationship(Group)


class Teacher(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    email = Column(String(100), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String(100), nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id', ondelete='CASCADE') )
    teacher = relationship(Teacher)

class StudentGrade(Base):
    __tablename__ = 'student_grades'
    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id', ondelete='CASCADE'))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id', ondelete='CASCADE'))
    student = relationship(Student)
    subject = relationship(Subject)
    grade = Column(Integer, nullable=True)
    date_received = Column(Date)
