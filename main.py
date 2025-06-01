# for virtual and creationa and activation commands
# python -m venv myenv
# myenv\Scripts\Activate
# uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {'message':'Hello World'}


@app.get("/about")
def about():
    return {'message':'Bhushan 1st Api'}