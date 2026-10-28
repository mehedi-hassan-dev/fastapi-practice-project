from pydantic import BaseModel


class Address(BaseModel):

    city: str
    state: str
    pin: str


class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'dhaka', 'state': 'dhanmodhi', 'pin': '125384'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Mehedi', 'gender': 'male', 'age': 25, 'address': address1}

patient1 = Patient(**patient_dict)



# ------------------model export-----------------

dict_formate = patient1.model_dump(include= ['name'])  # akhane include 0 exclude parameter use kora jabe 

print(dict_formate)
print(type(dict_formate))

json_formate = patient1.model_dump_json()

print(json_formate)
print(type(json_formate))