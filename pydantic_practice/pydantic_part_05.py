from pydantic import BaseModel, EmailStr,Field, field_validator

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int


    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']

        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
    

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()


    @field_validator('age', mode= 'before') # akhane after and before type validation use kora hoyese
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.email)
    print("Inserted")


patient_info = {'name': 'Mehedi', 'age': 25, 'email': 'abc@hdfc.com'}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)