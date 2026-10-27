from pydantic import BaseModel

class Patient(BaseModel):

    name: str
    age: int
    weight: float

def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("Inserted")


def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("Updated")

patient_info = {'name': 'Mehedi', 'age': 25, 'weight': 56}

patient1 = Patient(**patient_info)

update_patient_data(patient1)