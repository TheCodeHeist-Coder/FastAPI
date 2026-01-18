###### JUST LEARNING `FastAPI` FOR MY PROJECTS, BECAUSE I NEED IT RIGHT NOW ######



# FastAPI :-
#? FastAPI is a modern, high-performance web framework for building APIs with python

#!! Build with  `Starlette` and `Pydantic`.


# Process to use FastAPI...
1. from fastapi import FastAPI
2. create an instance of FastAPI
3. Create Routes Like This ->
*** @app.get("/")
       def hello():
           return {'message': 'Hello! Raj'}


##### Path function in fastApi..(`https://fastapi.tiangolo.com/tutorial/path-params/?h=path`)

-> it is used to provide `metadata`, `validation rules`, and `documentation hints` for path parameters in your API endpoints.           
* Title
* Description
* Example
* ge, gt, le, it -> `it is for validation`
* Min_length
* Max_length
* regex

 **EXAMPLE :-
 @app.get("/patient/{patient_id}")
 def view_patient(patient_id: str = Path(... , description='ID of the patient in the DB', example='P001')):

** Here in the Path()
* `...` indicates that param is must
* `description` tells about the params(like why? and how?)
* `example`  we can set an dummy example to understand the route



##### HTTP STATUS CODES...(In short)
-> help the client to understand :-
   1. whether the request was successful.
   2. whether something wrong.
   3. and what kind of issue occured(if any)

* 2xx -> `SUCCESS`
       201 -> success, 200 -> OK, 204 -> success but no data returned

* 3xx -> `REDIRECTION`

* 4xx -> `CLIENT ERROR`
       400 -> Bad Request, 401 -> Unauthorized, 403 -> Forbidden, 404 -> Not Found

* 5xx -> `SERVER ERROR`
       500 -> Internal Server Error, 502 -> Bad Gateway, 503 -> Service Unavailable


##### HTTPException :-(`https://fastapi.tiangolo.com/reference/exceptions/?h=httpexc`)
** -> It is a special built-in exception in FastAPI used to return custom HTTP error responses when something goes wrong in your API



###### Query Parameters(`https://fastapi.tiangolo.com/tutorial/query-params/?h=query`)

 -> Used to pass additional data
 -> appended to the end of the URL

 ex:-  `/patients?city=Delhi&sort_by=age`

 Here,
 * `?` -> start of the query parameter
 * Each parameter is a key-value pair: `kay=value`
 * Multiple parameters are separated by `&`

 In the above exmaple :-
 * city=Delhi  -> is a query parameter for filtering
 * sort_by    -> query parameter for sorting

** `Query()` is a utility function provided by FastAPI to declare, validate, and document query parameter in your API endpoints like :-

It allow you to :-
* set default values
* Enforce validation rules
* Add metadata like description, title, examples

`** HERE Query() is like Path()`






#### Pydantic (`https://fastapi.tiangolo.com/features/?h=pyda`)

### WHY PYDANTIC??  (type validation)
 => Let's take an example:-
 * Here i am expecting integer as age but i pass string still  it is working(dynamic typing). We can use type hunting like `name:str, name:int` but it doesn't give errors sometimes...
 ```python
def insert_patient_data(name, age):
    print(name)
    print(age)
    print('Inserted into Database')

    insert_patient_data("raj", "twenty")    
 ```


 ### 1. Define a Pydantic model that represents the ideal schema of the data
 * This include the expected fields, their types, and validation costraints(e.g. gt = 0 for +ve numbers)

 ### 2. Instantiate the model with raw input data(usually a dictionary or JSON-like structure)
 * Pydantic will automatically validate the data and coerce it into the correct pyhton types(if possoble)
 * if the data does't meet the model's requirements, pydantic raises a `validationError`

 ### 3. Pass the validated model objects to functions or use it throughout your codebase
 * This insures that every part of your program works with `clean`, `type-safe`, and `logically valid data`

 ### Example of type-validations...

 ```python
 from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool] = False
    allergies: Optional[List[str]] = None  
    contact_details: dict[str, str]

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies[0])

patient_info = {'name': 'raj', 'age': 18, 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

patient1 = Patient(**patient_info)

update_patient_data(patient1)

 ```


 ### Data validations....
 ```python

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Rajkumar', 'Bruce Banner'])]

    email: EmailStr

    age: int = Field(gt = 0, lt=120)

    linkedIn: AnyUrl
    
    weight: float = Field(gt=0, strict=True)

    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]

    allergies: Annotated[Optional[List[str]], Field(default=None ,max_length=5)] 
    
    contact_details: dict[str, str]


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.married)
  

patient_info = {'name': 'raj','email': 'raj@gmail.com', 'age': 18, 'weight': 56.3,'married': True,'linkedIn': 'https://linkedin/raj.com', 'contact_details': { 'phone': '7326763269'}}    

patient1 = Patient(**patient_info)

update_patient_data(patient1)
 ```

 ### field_validators...
 ```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: Optional[bool] = False
    allergies: Optional[List[str]] = None  
    contact_details: dict[str, str]



  #? email should be of specific domains... 
    @field_validator('email')
    @classmethod
    def emailValidator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value 

     #?  name should be in cappital
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()


  #? field_validator work in two modes: 'bofore' and 'after'(by default)
    @field_validator('age', mode='before') 
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")          



def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)



patient_info = {'name': 'raj', 'age': '18','email': "raj@hdfc.com", 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '7326763269'}}    

patient1 = Patient(**patient_info)   #? validation performed

update_patient_data(patient1)

 ```


 ### model_validators(perform validation on more than 1 fields)
```python


from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: Optional[bool] = False
    allergies: Optional[List[str]] = None  
    contact_details: dict[str, str]


@model_validator(mode='after')
def validate_emergency_contact(self):
    if self.age > 60 and 'emergency' not in self.contact_details:
        raise ValueError('Patient older than 60 must have an emergency contact details')
    return self

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies[0])



patient_info = {'name': 'raj', 'age': 20, 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

patient1 = Patient(**patient_info)

update_patient_data(patient1)

```


### computed_field(should be used inside model)
```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, computed_field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    married: Optional[bool] = False
    allergies: Optional[List[str]] = None  
    contact_details: dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
       bmi = (self.weight/(self.height**2),2)
       return bmi



def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.bmi)
    print(patient.married)
    print(patient.allergies[0])

patient_info = {'name': 'raj', 'age': 18, 'weight': 56.3,'height': 165.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

patient1 = Patient(**patient_info)

update_patient_data(patient1)

```


### Nested Models
```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, computed_field
from typing import List, Dict, Optional

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address


address_dict = {'city': 'hathras', 'state':'uttar-pradesh', 'pin':'268421'} 

address1 = Address(**address_dict)


patient_dict = {'name':'raj', 'gender':'male','age': 20, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
```

### Export in the form of dict and json...
```python

from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, computed_field
from typing import List, Dict, Optional

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


address_dict = {'city': 'hathras', 'state':'uttar-pradesh', 'pin':'268421'} 
address1 = Address(**address_dict)


patient_dict = {'name':'raj', 'gender':'male','age': 20, 'address': address1}
patient1 = Patient(**patient_dict)

#? convert patient into dictionary
temp = patient1.model_dump()

#? convert into json
temp2 = patient1.model_dump_json()
print(temp2)
print(type(temp2))  #? type string

#? want to specific things export
temp3 = patient1.model_dump(include=['name', 'age'])   #? we can exclude also instead of include...
print(temp3)
```