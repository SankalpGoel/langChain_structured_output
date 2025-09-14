from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str = "Sankalp Goel"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0.0, lt=10.0, default=5, description="CGPA should be between 0.0 and 10.0")

new_student={"age":"32", "email":"abc@gmail.com", "cgpa":9.1}

student = Student(**new_student)

print(student)

student_dict = student.model_dump()
print(student_dict) 

student_json = student.model_dump_json()
print(student_json)
