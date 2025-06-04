from pydantic import BaseModel,EmailStr,AnyUrl,Field ,field_validator
from typing import List,Dict, Optional, Annotated # for two level validation we use this 


class Patient(BaseModel):
    email: EmailStr
    name : str
    age : int 
    weight : float
    married: bool
    allergies:List[str]
    contact_details: Dict[str, str]
    
    
    
# filed validaotr to check specific domin name
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        
        valid_domain=['hdfc.com','icici.com']
        
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError("Not a valid domain")
        return value


# field validator name should be always in Capital letters
    @field_validator('name')
    @classmethod
    def capita_name_patient(cls , value):
        return value.upper()
    
# this throw will error because it takes value before type coercion     
    
    # @field_validator('age',mode='before')
    # @classmethod
    # def age_validation(cls,value):
    #     if 0< value < 55:
    #         return value
    #     else :
    #         raise ValueError("age is betwen 0 to 60")
        
    # this throw will not throw  error because it takes value after  type coercion     
    
    @field_validator('age',mode='after')
    @classmethod
    def age_validation(cls,value):
        if 0< value < 55:
            return value
        else :
            raise ValueError("age is betwen 0 to 60")


#field validator for age 
 





def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)

    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')
    
 
patient_info={'name':'nitish','age':'23','email':'bhudhanzade02@hdfc.com','linkedin_url':'https://www.linkedin.com/in/bhushan-zade-491a36332/','weight':24.3,'married':True,'allergies':['cold','pollen'],'contact_details':{'email':'abc@gmail.com','phone':'333234234'}}    

Patient1=Patient(**patient_info) # validation --> type coercion     

# insert_patient_data(Patient1)
update_patient_data(Patient1)



#field validator can be used in two modes before and after mode 
