from fastapi import FastAPI
from .schemas import Employee
from .storage import Employees

app=FastAPI()

@app.post("/Employees")
def create_employee(employee:Employee):
    Employees.append(employee)
    print(Employees)
    return{
        "message":"employee added successfully",
        "employee":employee
    }

@app.get("/Employees")
def get_employee():
    return Employees

@app.get("/Employees/{id}")
def get_employee_id(id:int):
    if(id>len(Employees)):
        return{"message":"Not Found"}
    else:
        return Employees[id]
    
@app.delete("/Employees/{id}")
def delete_employee(id:int):
    if(id>len(Employees)):
        return {"message":"Invalid Id"}
    else:
        Employees.pop(id)
        return {"message":"employee deleted successfully"}
    
@app.put("/Employees/{id}")
def update_Employee(employee:Employee , id:int):
    Employees[id]=employee

    return {
        "message":"employee updates successfully",
        "employee":Employees[id]
    }

