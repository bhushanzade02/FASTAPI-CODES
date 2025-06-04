from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict, Optional, Annotated # for two level validation we use this 


class Patient(BaseModel):
    # name: str = Field(max_length=50)
    name : Annotated[str, Field(max_length=50,title='name of the patient', description="give name of patient less thsn 50 characters",example= 'bhushan')]
    age : int=Field(gt=0,lt=60)
    email: EmailStr
    linkedin_url:AnyUrl
    # weight : float =Field(gt=0)
    weight : Annotated[float, Field( gt=0,strict=True )]
    # married :Optional[bool] =None   # ypu also set this default as True or False    
    married: Annotated[bool, Field(default= None,description="patien is maried or not")]
    allergies:Annotated[Optional[ List[str] ],Field(default=None,max_length=5) ]
    # if we use sadha list [] then this only chck it is list but if you use this List[] it chekcs lsit and data inside this list will be string hum bata rhe allergies khud mein list honga but uska hr item string honga
    contact_details: Dict[str, str] #contct_deatils are dictionary but uska hr element string honga


#above all fileds are required in pydntic model in patient_info in our case but what if you habve to make optional filed in pydantic model then we simply import optional from typing lets makemarriage column optional  but jb bhi aap kisiko optional banate hoto to usr deafault value none deni pdti hain 

# pydantic gives builtn in function for email validation  
# from pydantic import Emailstr

# you can validate any url by EmailStr

# for custom data vlaidation use filed form pydantic exmaple applying filed function on it should be between 0 to 60 yeasrs .. field function is wrok not inly data validation but also to attach meatdata so let apply on name  znd also you assigned deafuklt by field fuctipn apply onmrriage

# field function strict function on weight it doesnt do type coversion of strict =TRUE


#field Validator


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('inserted')
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')
    
 
patient_info={'name':'nitish','age':'40','email':'bhudhanzade02@gmail.com','linkedin_url':'https://www.linkedin.com/in/bhushan-zade-491a36332/','weight':24.3,'married':True,'allergies':['cold','pollen'],'contact_details':{'email':'abc@gmail.com','phone':'333234234'}}    

Patient1=Patient(**patient_info)

# insert_patient_data(Patient1)
update_patient_data(Patient1)
