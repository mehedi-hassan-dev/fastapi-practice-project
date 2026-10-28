from pydantic import BaseModel, EmailStr, model_validator
from typing import  Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    contact_deatils: Dict[str, str]


    @model_validator(mode= 'after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_deatils:
            raise ValueError('Patient older then 60 must have an emergency contact')
        return model


def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.contact_deatils)
    print("Inserted")


patient_info = {'name': 'Mehedi', 'email': 'abc@gmail.com', 'age': 65, 'contact_deatils': {'phone': '013654857', 'emergency': '25373948'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)