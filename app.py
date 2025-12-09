from flask import Flask, jsonify

# Student data
students = [
    {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
    {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
    {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
    {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
    {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
    {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
    {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
    {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
    {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
    {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
]

# Create Flask application
app = Flask(__name__)

# Route: /students/ - Returns all students
@app.route('/students/')
def get_all_students():
    return jsonify(students)

# Route: /old_students/ - Returns students older than 20
@app.route('/old_students/')
def get_old_students():
    old_students = [student for student in students if student['age'] > 20]
    return jsonify(old_students)

# Route: /young_students/ - Returns students younger than 21
@app.route('/young_students/')
def get_young_students():
    young_students = [student for student in students if student['age'] < 21]
    return jsonify(young_students)

# Route: /advance_students/ - Returns students younger than 21 with grade 'A'
@app.route('/advance_students/')
def get_advance_students():
    advance_students = [
        student for student in students 
        if student['age'] < 21 and student['grade'] == 'A'
    ]
    return jsonify(advance_students)

# Route: /student_names/ - Returns only first_name and last_name
@app.route('/student_names/')
def get_student_names():
    student_names = [
        {
            'first_name': student['first_name'],
            'last_name': student['last_name']
        }
        for student in students
    ]
    return jsonify(student_names)

# Route: /student_ages/ - Returns student_name (full name) and age
@app.route('/student_ages/')
def get_student_ages():
    student_ages = [
        {
            'student_name': f"{student['first_name']} {student['last_name']}",
            'age': student['age']
        }
        for student in students
    ]
    return jsonify(student_ages)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)