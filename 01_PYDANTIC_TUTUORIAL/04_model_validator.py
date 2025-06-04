# field validator are used in only on one field but if you have two validation on both fields at once then we use model validator in this we combine two and more fields and do field validation
#for example if you want to do validation on on the bais of age is less you have to add emergency Number
 

from pydantic import BaseModel,EmailStr,AnyUrl,Field ,field_validator,model_validator
from typing import List,Dict, Optional, Annotated # for two level validation we use this 


class Patient(BaseModel):
    email: EmailStr
    name : str
    age : int 
    weight : float
    married: bool
    allergies:List[str]
    contact_details: Dict[str, str]
    
    
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older tha 60 must have an emeergency conatact')
    
    

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)

    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')
    
 
patient_info={'name':'nitish','age':'83','email':'bhudhanzade02@hdfc.com','linkedin_url':'https://www.linkedin.com/in/bhushan-zade-491a36332/','weight':24.3,'married':True,'allergies':['cold','pollen'],'contact_details':{'email':'abc@gmail.com','emergency':'333234234'}}    

Patient1=Patient(**patient_info) # validation --> type coercion     

# insert_patient_data(Patient1)
update_patient_data(Patient1)





    