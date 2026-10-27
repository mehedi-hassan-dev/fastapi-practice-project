from pydantic import BaseModel, EmailStr, AnyUrl, Field

class Patient(BaseModel):

    name: str = Field(max_length= 50)
    age: int = Field(gt=0, lt=120) # akhane age value er range defile kora hoise 0 to 120
    weight: float = Field(gt=0) # age value 0 er ceye soto set korte parbe na
    email: EmailStr
    linkedin_url: AnyUrl
   

def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.linkedin_url)
    print("Inserted")


patient_info = {'name': 'Mehedi', 'age': 25, 'weight': 71.3, 'email': 'mehedi@gmail.com', 'linkedin_url': 'http://linkedin.com/3546'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)