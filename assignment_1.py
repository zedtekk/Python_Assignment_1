from fastapi import FastAPI

app = FastAPI()

# In-memory storage using a Python dictionary
students_db = {}


class Student:
    def __init__(self, name: str, age: int, sex: str, height: float):
        self.id = len(students_db) + 1  # Assigning ID based on the length of the existing students
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height


@app.post("/students/")
async def create_student(name: str, age: int, sex: str, height: float):
    student = Student(name, age, sex, height)
    students_db[student.id] = student
    return student


@app.get("/students/{student_id}")
async def read_student(student_id: int):
    student = students_db.get(student_id)
    if student is None:
        return {"error": "Student not found"}
    return student


@app.get("/students/")
async def read_students():
    return students_db


@app.put("/students/{student_id}")
async def update_student(student_id: int, name: str, age: int, sex: str, height: float):
    student = students_db.get(student_id)
    if student is None:
        return {"error": "Student not found"}
    student.name = name
    student.age = age
    student.sex = sex
    student.height = height
    return student


@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    if student_id not in students_db:
        return {"error": "Student not found"}
    del students_db[student_id]
    return {"message": "Student deleted successfully"}
