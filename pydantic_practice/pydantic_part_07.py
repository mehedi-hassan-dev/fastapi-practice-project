from pydantic import BaseModel, EmailStr, computed_field
from typing import  Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float  # kg
    height: float  # meter
    contact_deatils: Dict[str, str]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


def insert_patient_data(patient:Patient):

    print(f'Name: {patient.name}')
    print(f'Age: {patient.age}')
    print(f'Email: {patient.email}')
    print(f'Contact info: {patient.contact_deatils}')
    print(f'Calculate BMI: {patient.bmi}')
    print("Inserted")


patient_info = {'name': 'Mehedi', 'email': 'abc@gmail.com', 'age': 65, 'weight': 75.2, 'height':1.72, 'contact_deatils': {'phone': '013654857', 'emergency': '25373948'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)