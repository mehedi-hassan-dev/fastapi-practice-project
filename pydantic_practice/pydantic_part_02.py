from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    age: int
    weight: float = 57.8  # default value set
    married: Optional[bool] = None  # Optional value set akhane value pass kortew paro abar na paro
    allergies: List[str]
    contact_details: Dict[str, str]

def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted")


patient_info = {'name': 'Mehedi', 'age': 25,'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': '01347493'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)