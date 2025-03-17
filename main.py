from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name:str
    age:int
    major:str

dataset = [
    {"name":"ali","age":24,"major":"cs"},
    {"name":"reze","age":24,"major":"cs"}
]

@app.get("/all/")
async def all():
    return {"message":dataset}

@app.get("/students/{student_id}")
async def get_by_id(student_id:int):
    index = student_id -1
    if 0<= index <= len(dataset):
        return {"student":dataset[index]}
    return {"error":"student not found"}

@app.post("/post/")
async def add_student(student:Student):
    new_student = student.model_dump()
    dataset.append(new_student)
    return {"message":"new student created",
            "data":dataset}

@app.delete("/del/{student_id}")
async def del_student(student_id:int):
    index = student_id -1
    if 0<= index <= len(dataset):
        del dataset[index]
        return {"message":"successfully deleted",
                "data":dataset}
    return {"error":"student not found "}
