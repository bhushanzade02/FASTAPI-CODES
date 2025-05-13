from fastapi import FastAPI 
app =FastAPI()


@app.get("/")
def hello():
    return {'message':'Hello World'}


@app.get('/about')
def about():
    return {'mesage':'Machine learning is Good to Learn'}



# how to enable virtual environment 
# python -m venv myenv
# myenv\Scripts\activate
# uvicorn main::app --reload