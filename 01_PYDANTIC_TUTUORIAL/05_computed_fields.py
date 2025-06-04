
from pydantic import BaseModel,EmailStr,AnyUrl,Field ,field_validator,model_validator,computed_field
from typing import List,Dict, Optional, Annotated # for two level validation we use this 


class Patient(BaseModel):
    email: EmailStr
    name : str
    age : int 
    weight : float #kgs
    height : float #mts
  
    married: bool
    allergies:List[str]
    contact_details: Dict[str, str]
    
    
    @computed_field()
    @property
    def calculate_bmi(self) -> float:
        bmi =round(self.weight/(self.height**2),2)
        return bmi

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)

    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('BMI',patient.calculate_bmi)
    print('updated')
    
 
patient_info={'name':'nitish','age':'83','email':'bhudhanzade02@hdfc.com','linkedin_url':'https://www.linkedin.com/in/bhushan-zade-491a36332/','weight':24.3,'height':'1.7','married':True,'allergies':['cold','pollen'],'contact_details':{'email':'abc@gmail.com','emergency':'333234234'}}    

Patient1=Patient(**patient_info) # validation --> type coercion     

# insert_patient_data(Patient1)
update_patient_data(Patient1)
