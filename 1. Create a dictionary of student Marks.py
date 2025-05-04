# Task 1 : Create a Dictionary of Student Marks
""" 
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

"""
def students_marks ():
    marks_dict = {
    'Ram' : 100,
    'Laxman' : 99,
    'Sita' : 100,
    'Bharat' : 98,
    'Hanuman': 100
  }
    student_name = input('Enter the sutdent\'s name: ')
    if(student_name in marks_dict):
      print (f"{student_name}'s marks: {marks_dict[student_name]}")
    else: 
      print('Student not found.')

students_marks()