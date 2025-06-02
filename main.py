# learning of production ready fast api codes 

# for virtual and creationa and activation commands
# python -m venv myenv
# myenv\Scripts\Activate
# uvicorn main:app --reload


from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
        
    return data
        


@app.get("/")
def hello():
    return {'message':'Patients Maagement system'}


@app.get("/about")
def about():
    return {'message':'A fully functional api to manage systrem record '}



@app.get('/view')
def view():
    data= load_data()
    
    return data


# @app.get("/patient/{patient_id}")
# def view_patient(patient_id:str):
#     data =load_data()
    
#     if patient_id in data:
#         return data[patient_id]
#     return {'error':"Patient Not Found"}

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path (..., description='Id of the paient in DB',example ='P001') ):
    data=load_data()
    
    if patient_id in data:
        return data[patient_id]
    return HTTPException(status_code=404,detail='patient not found')



@app.get('/github/bhushanzade02')
def view_git():
    return {"Message":"You have good github repository"}


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):
    valid_fields = ['height','weight','bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400 ,detail=f'invalid field select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException (status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()
    
    sort_order =True if order=='desc' else False
    
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    
    
    return sorted_data
#/sort?sort_by=bmi&order=desc