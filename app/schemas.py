from pydantic import BaseModel

class Employee(BaseModel):
    EmployeeID:int
    Name:str
    Department:str
    Salary:int
    Email:str