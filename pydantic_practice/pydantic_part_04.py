from pydantic import BaseModel, Field
from typing import Annotated

class Patient(BaseModel):

    name: str = Annotated[str, Field(max_length= 50, title= 'Name of the patient', description= 'Give the name of the patient in less than 50 chars', examples= ['Mehedi', 'Babu'])]

    weight: Annotated[float, Field(gt=0, strict= True)]
    
    married: Annotated[bool, Field(default= None, description= 'Is the patient married or not')]

    
def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.weight)
    print(patient.married)

    print("Inserted")


patient_info = {'name': 'Mehedi', 'weight': 71.3, 'married':"No"}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)