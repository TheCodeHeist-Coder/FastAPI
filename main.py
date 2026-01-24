from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal


#? Create an Instance of FastAPI
app = FastAPI()

#! Creating basic Routes... 
# @app.get("/")
# def hello():
#     return {'message': 'Hello! Raj'}

# @app.get("/about")
# def about():
#     return {'message': "This is a about point"}    


#! Pydantic Code... 
class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City, where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')] 
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(...,gt=0, description='height of the patient' )]
    weight: Annotated[float, Field(..., gt=0,description='Weight of the patient')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight/(self.height ** 2)
        return bmi


    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Under weight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return "Obese"               





#! Practise... 
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data    

def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f)  
    


@app.get("/")
def hello():
    return {"message": "Patient Management System"}


@app.get("/about")
def about():
    return {"Message": "This is just only for learning about FastAPI...OKK!"}   


#? get all the patients
@app.get("/view")
def view():
    data = load_data()
    return data


#? get a specific user with the helps of params...
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', examples='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='patient not found') 



#? Query parameters

@app.get("/sort")
def sort_patients(sort_by: str = Query(... , description="sort on the basis of height, weight and bmi" ), order: str = Query('asc', description="Sort in ascending or descending order" )):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid fields select from")

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select')


    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order) 

    return sorted_data      



@app.post('/create')
def create_patient(patient: Patient):

    # load existing data
      data = load_data()
      
    # check if the patient is already exists
      if patient.id in data:
          raise HTTPException(status_code=400, detail='Patient already exist')



    # new patient add to the DB
      data[patient.id] = patient.model_dump(exclude=['id'])


      # save into the json file
      save_data(data)


      return JSONResponse(status_code=201, content={'message': 'Patient created successfully...'})