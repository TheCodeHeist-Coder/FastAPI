# # # from pydantic import BaseModel
# # # from typing import List, Dict, Optional

# # #! Example 01
# # # class Patient(BaseModel):
# # #     name: str
# # #     age: int


# # # def insert_patient_data(patient: Patient):
# # #     print(patient.name)
# # #     print(patient.age)
# # #     print('Patient added...')

# # # patient_info = {'name': 'raj', 'age': 20}

# # # patient1 = Patient(**patient_info)    

# # # insert_patient_data(patient1)



# # #! example 02
# # # class Patient(BaseModel):
# # #     name: str
# # #     age: int
# # #     weight: float
# # #     married: Optional[bool] = False
# # #     allergies: Optional[List[str]] = None  
# # #     contact_details: dict[str, str]



# # # def update_patient_data(patient: Patient):
# # #     print(patient.name)
# # #     print(patient.age)
# # #     print(patient.married)
# # #     print(patient.allergies[0])



# # # patient_info = {'name': 'raj', 'age': 18, 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

# # # patient1 = Patient(**patient_info)

# # # update_patient_data(patient1)



# # #! example 03

# # # from pydantic import BaseModel, EmailStr, AnyUrl, Field
# # # from typing import List, Dict, Optional,Annotated

# # # class Patient(BaseModel):
# # #     name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Rajkumar', 'Bruce Banner'])]

# # #     email: EmailStr

# # #     age: int = Field(gt = 0, lt=120)

# # #     linkedIn: AnyUrl
    
# # #     weight: float = Field(gt=0, strict=True)

# # #     married: Annotated[bool, Field(default=None, description='Is the patient married or not')]

# # #     allergies: Annotated[Optional[List[str]], Field(default=None ,max_length=5)] 

# # #     contact_details: dict[str, str]



# # # def update_patient_data(patient: Patient):
# # #     print(patient.name)
# # #     print(patient.email)
# # #     print(patient.married)
  



# # # patient_info = {'name': 'raj','email': 'raj@gmail.com', 'age': 18, 'weight': 56.3,'married': True,'linkedIn': 'https://linkedin/raj.com', 'contact_details': { 'phone': '7326763269'}}    

# # # patient1 = Patient(**patient_info)

# # # update_patient_data(patient1)


# # #! Example 04

# # #? Field validator... 
# # # from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
# # # from typing import List, Dict, Optional,Annotated

# # # class Patient(BaseModel):
# # #     name: str
# # #     age: int
# # #     email: EmailStr
# # #     weight: float
# # #     married: Optional[bool] = False
# # #     allergies: Optional[List[str]] = None  
# # #     contact_details: dict[str, str]



# # #   #? email should be of specific domains... 
# # #     @field_validator('email')
# # #     @classmethod
# # #     def emailValidator(cls, value):
# # #         valid_domains = ['hdfc.com', 'icici.com']
# # #         domain_name = value.split('@')[-1]

# # #         if domain_name not in valid_domains:
# # #             raise ValueError('Not a valid domain')

# # #         return value 

# # #      #?  name should be in cappital
# # #     @field_validator('name')
# # #     @classmethod
# # #     def transform_name(cls, value):
# # #         return value.upper()


# # #   #? field_validator work in two modes: 'bofore' and 'after'(by default)
# # #     @field_validator('age', mode='before') 
# # #     @classmethod
# # #     def validate_age(cls, value):
# # #         if 0 < value < 100:
# # #             return value
# # #         else:
# # #             raise ValueError("Age should be in between 0 and 100")          



# # # def update_patient_data(patient: Patient):
# # #     print(patient.name)
# # #     print(patient.age)
# # #     print(patient.married)
# # #     print(patient.allergies)



# # # patient_info = {'name': 'raj', 'age': '18','email': "raj@hdfc.com", 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '7326763269'}}    

# # # patient1 = Patient(**patient_info)   #? validation performed

# # # update_patient_data(patient1)



# # #! Example 05
# # #? model validators(perform validation on more than 1 fields)

# # # from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
# # # from typing import List, Dict, Optional,Annotated

# # # class Patient(BaseModel):
# # #     name: str
# # #     age: int
# # #     weight: float
# # #     married: Optional[bool] = False
# # #     allergies: Optional[List[str]] = None  
# # #     contact_details: dict[str, str]


# # # @model_validator(mode='after')
# # # def validate_emergency_contact(self):
# # #     if self.age > 60 and 'emergency' not in self.contact_details:
# # #         raise ValueError('Patient older than 60 must have an emergency contact details')
# # #     return self

# # # def update_patient_data(patient: Patient):
# # #     print(patient.name)
# # #     print(patient.age)
# # #     print(patient.married)
# # #     print(patient.allergies[0])



# # # patient_info = {'name': 'raj', 'age': 20, 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

# # # patient1 = Patient(**patient_info)

# # # update_patient_data(patient1)


# # #! computed fields... (to create a new field w/o intervance of user like BMI(achieved by user's H and W))

# # from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, computed_field
# # from typing import List, Dict, Optional

# # class Patient(BaseModel):
# #     name: str
# #     age: int
# #     weight: float
# #     height: float
# #     married: Optional[bool] = False
# #     allergies: Optional[List[str]] = None  
# #     contact_details: dict[str, str]

# #     @computed_field
# #     @property
# #     def bmi(self) -> float:
# #        bmi = (self.weight/(self.height**2),2)
# #        return bmi



# # def update_patient_data(patient: Patient):
# #     print(patient.name)
# #     print(patient.age)
# #     print(patient.bmi)
# #     print(patient.married)
# #     print(patient.allergies[0])

# # patient_info = {'name': 'raj', 'age': 18, 'weight': 56.3,'height': 165.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

# # patient1 = Patient(**patient_info)

# # update_patient_data(patient1)




# #! # from pydantic import BaseModel
# # from typing import List, Dict, Optional

# #! Example 01
# # class Patient(BaseModel):
# #     name: str
# #     age: int


# # def insert_patient_data(patient: Patient):
# #     print(patient.name)
# #     print(patient.age)
# #     print('Patient added...')

# # patient_info = {'name': 'raj', 'age': 20}

# # patient1 = Patient(**patient_info)    

# # insert_patient_data(patient1)



# #! example 02
# # class Patient(BaseModel):
# #     name: str
# #     age: int
# #     weight: float
# #     married: Optional[bool] = False
# #     allergies: Optional[List[str]] = None  
# #     contact_details: dict[str, str]



# # def update_patient_data(patient: Patient):
# #     print(patient.name)
# #     print(patient.age)
# #     print(patient.married)
# #     print(patient.allergies[0])



# # patient_info = {'name': 'raj', 'age': 18, 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

# # patient1 = Patient(**patient_info)

# # update_patient_data(patient1)



# #! example 03

# # from pydantic import BaseModel, EmailStr, AnyUrl, Field
# # from typing import List, Dict, Optional,Annotated

# # class Patient(BaseModel):
# #     name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Rajkumar', 'Bruce Banner'])]

# #     email: EmailStr

# #     age: int = Field(gt = 0, lt=120)

# #     linkedIn: AnyUrl
    
# #     weight: float = Field(gt=0, strict=True)

# #     married: Annotated[bool, Field(default=None, description='Is the patient married or not')]

# #     allergies: Annotated[Optional[List[str]], Field(default=None ,max_length=5)] 

# #     contact_details: dict[str, str]



# # def update_patient_data(patient: Patient):
# #     print(patient.name)
# #     print(patient.email)
# #     print(patient.married)
  



# # patient_info = {'name': 'raj','email': 'raj@gmail.com', 'age': 18, 'weight': 56.3,'married': True,'linkedIn': 'https://linkedin/raj.com', 'contact_details': { 'phone': '7326763269'}}    

# # patient1 = Patient(**patient_info)

# # update_patient_data(patient1)


# #! Example 04

# #? Field validator... 
# # from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
# # from typing import List, Dict, Optional,Annotated

# # class Patient(BaseModel):
# #     name: str
# #     age: int
# #     email: EmailStr
# #     weight: float
# #     married: Optional[bool] = False
# #     allergies: Optional[List[str]] = None  
# #     contact_details: dict[str, str]



# #   #? email should be of specific domains... 
# #     @field_validator('email')
# #     @classmethod
# #     def emailValidator(cls, value):
# #         valid_domains = ['hdfc.com', 'icici.com']
# #         domain_name = value.split('@')[-1]

# #         if domain_name not in valid_domains:
# #             raise ValueError('Not a valid domain')

# #         return value 

# #      #?  name should be in cappital
# #     @field_validator('name')
# #     @classmethod
# #     def transform_name(cls, value):
# #         return value.upper()


# #   #? field_validator work in two modes: 'bofore' and 'after'(by default)
# #     @field_validator('age', mode='before') 
# #     @classmethod
# #     def validate_age(cls, value):
# #         if 0 < value < 100:
# #             return value
# #         else:
# #             raise ValueError("Age should be in between 0 and 100")          



# # def update_patient_data(patient: Patient):
# #     print(patient.name)
# #     print(patient.age)
# #     print(patient.married)
# #     print(patient.allergies)



# # patient_info = {'name': 'raj', 'age': '18','email': "raj@hdfc.com", 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '7326763269'}}    

# # patient1 = Patient(**patient_info)   #? validation performed

# # update_patient_data(patient1)



# #! Example 05
# #? model validators(perform validation on more than 1 fields)

# # from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
# # from typing import List, Dict, Optional,Annotated

# # class Patient(BaseModel):
# #     name: str
# #     age: int
# #     weight: float
# #     married: Optional[bool] = False
# #     allergies: Optional[List[str]] = None  
# #     contact_details: dict[str, str]


# # @model_validator(mode='after')
# # def validate_emergency_contact(self):
# #     if self.age > 60 and 'emergency' not in self.contact_details:
# #         raise ValueError('Patient older than 60 must have an emergency contact details')
# #     return self

# # def update_patient_data(patient: Patient):
# #     print(patient.name)
# #     print(patient.age)
# #     print(patient.married)
# #     print(patient.allergies[0])



# # patient_info = {'name': 'raj', 'age': 20, 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

# # patient1 = Patient(**patient_info)

# # update_patient_data(patient1)


# #! computed fields... (to create a new field w/o intervance of user like BMI(achieved by user's H and W))

# from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, computed_field
# from typing import List, Dict, Optional

# class Patient(BaseModel):
#     name: str
#     age: int
#     weight: float
#     height: float
#     married: Optional[bool] = False
#     allergies: Optional[List[str]] = None  
#     contact_details: dict[str, str]

#     @computed_field
#     @property
#     def bmi(self) -> float:
#        bmi = (self.weight/(self.height**2),2)
#        return bmi



# def update_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print(patient.bmi)
#     print(patient.married)
#     print(patient.allergies[0])

# patient_info = {'name': 'raj', 'age': 18, 'weight': 56.3,'height': 165.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

# patient1 = Patient(**patient_info)

# update_patient_data(patient1)



# # from pydantic import BaseModel
# # from typing import List, Dict, Optional

# #! Example 01
# # class Patient(BaseModel):
# #     name: str
# #     age: int


# # def insert_patient_data(patient: Patient):
# #     print(patient.name)
# #     print(patient.age)
# #     print('Patient added...')

# # patient_info = {'name': 'raj', 'age': 20}

# # patient1 = Patient(**patient_info)    

# # insert_patient_data(patient1)



# #! example 02
# # class Patient(BaseModel):
# #     name: str
# #     age: int
# #     weight: float
# #     married: Optional[bool] = False
# #     allergies: Optional[List[str]] = None  
# #     contact_details: dict[str, str]



# # def update_patient_data(patient: Patient):
# #     print(patient.name)
# #     print(patient.age)
# #     print(patient.married)
# #     print(patient.allergies[0])



# # patient_info = {'name': 'raj', 'age': 18, 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

# # patient1 = Patient(**patient_info)

# # update_patient_data(patient1)



# #! example 03

# # from pydantic import BaseModel, EmailStr, AnyUrl, Field
# # from typing import List, Dict, Optional,Annotated

# # class Patient(BaseModel):
# #     name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Rajkumar', 'Bruce Banner'])]

# #     email: EmailStr

# #     age: int = Field(gt = 0, lt=120)

# #     linkedIn: AnyUrl
    
# #     weight: float = Field(gt=0, strict=True)

# #     married: Annotated[bool, Field(default=None, description='Is the patient married or not')]

# #     allergies: Annotated[Optional[List[str]], Field(default=None ,max_length=5)] 

# #     contact_details: dict[str, str]



# # def update_patient_data(patient: Patient):
# #     print(patient.name)
# #     print(patient.email)
# #     print(patient.married)
  



# # patient_info = {'name': 'raj','email': 'raj@gmail.com', 'age': 18, 'weight': 56.3,'married': True,'linkedIn': 'https://linkedin/raj.com', 'contact_details': { 'phone': '7326763269'}}    

# # patient1 = Patient(**patient_info)

# # update_patient_data(patient1)


# #! Example 04

# #? Field validator... 
# # from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
# # from typing import List, Dict, Optional,Annotated

# # class Patient(BaseModel):
# #     name: str
# #     age: int
# #     email: EmailStr
# #     weight: float
# #     married: Optional[bool] = False
# #     allergies: Optional[List[str]] = None  
# #     contact_details: dict[str, str]



# #   #? email should be of specific domains... 
# #     @field_validator('email')
# #     @classmethod
# #     def emailValidator(cls, value):
# #         valid_domains = ['hdfc.com', 'icici.com']
# #         domain_name = value.split('@')[-1]

# #         if domain_name not in valid_domains:
# #             raise ValueError('Not a valid domain')

# #         return value 

# #      #?  name should be in cappital
# #     @field_validator('name')
# #     @classmethod
# #     def transform_name(cls, value):
# #         return value.upper()


# #   #? field_validator work in two modes: 'bofore' and 'after'(by default)
# #     @field_validator('age', mode='before') 
# #     @classmethod
# #     def validate_age(cls, value):
# #         if 0 < value < 100:
# #             return value
# #         else:
# #             raise ValueError("Age should be in between 0 and 100")          



# # def update_patient_data(patient: Patient):
# #     print(patient.name)
# #     print(patient.age)
# #     print(patient.married)
# #     print(patient.allergies)



# # patient_info = {'name': 'raj', 'age': '18','email': "raj@hdfc.com", 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '7326763269'}}    

# # patient1 = Patient(**patient_info)   #? validation performed

# # update_patient_data(patient1)



# #! Example 05
# #? model validators(perform validation on more than 1 fields)

# # from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
# # from typing import List, Dict, Optional,Annotated

# # class Patient(BaseModel):
# #     name: str
# #     age: int
# #     weight: float
# #     married: Optional[bool] = False
# #     allergies: Optional[List[str]] = None  
# #     contact_details: dict[str, str]


# # @model_validator(mode='after')
# # def validate_emergency_contact(self):
# #     if self.age > 60 and 'emergency' not in self.contact_details:
# #         raise ValueError('Patient older than 60 must have an emergency contact details')
# #     return self

# # def update_patient_data(patient: Patient):
# #     print(patient.name)
# #     print(patient.age)
# #     print(patient.married)
# #     print(patient.allergies[0])



# # patient_info = {'name': 'raj', 'age': 20, 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

# # patient1 = Patient(**patient_info)

# # update_patient_data(patient1)


# #! computed fields... (to create a new field w/o intervance of user like BMI(achieved by user's H and W))

# from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, computed_field
# from typing import List, Dict, Optional

# class Patient(BaseModel):
#     name: str
#     age: int
#     weight: float
#     height: float
#     married: Optional[bool] = False
#     allergies: Optional[List[str]] = None  
#     contact_details: dict[str, str]

#     @computed_field
#     @property
#     def bmi(self) -> float:
#        bmi = (self.weight/(self.height**2),2)
#        return bmi



# def update_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print(patient.bmi)
#     print(patient.married)
#     print(patient.allergies[0])

# patient_info = {'name': 'raj', 'age': 18, 'weight': 56.3,'height': 165.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

# patient1 = Patient(**patient_info)

# update_patient_data(patient1)




#! # from pydantic import BaseModel
# from typing import List, Dict, Optional

#! Example 01
# class Patient(BaseModel):
#     name: str
#     age: int


# def insert_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print('Patient added...')

# patient_info = {'name': 'raj', 'age': 20}

# patient1 = Patient(**patient_info)    

# insert_patient_data(patient1)



#! example 02
# class Patient(BaseModel):
#     name: str
#     age: int
#     weight: float
#     married: Optional[bool] = False
#     allergies: Optional[List[str]] = None  
#     contact_details: dict[str, str]



# def update_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print(patient.married)
#     print(patient.allergies[0])



# patient_info = {'name': 'raj', 'age': 18, 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

# patient1 = Patient(**patient_info)

# update_patient_data(patient1)



#! example 03

# from pydantic import BaseModel, EmailStr, AnyUrl, Field
# from typing import List, Dict, Optional,Annotated

# class Patient(BaseModel):
#     name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Rajkumar', 'Bruce Banner'])]

#     email: EmailStr

#     age: int = Field(gt = 0, lt=120)

#     linkedIn: AnyUrl
    
#     weight: float = Field(gt=0, strict=True)

#     married: Annotated[bool, Field(default=None, description='Is the patient married or not')]

#     allergies: Annotated[Optional[List[str]], Field(default=None ,max_length=5)] 

#     contact_details: dict[str, str]



# def update_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.email)
#     print(patient.married)
  



# patient_info = {'name': 'raj','email': 'raj@gmail.com', 'age': 18, 'weight': 56.3,'married': True,'linkedIn': 'https://linkedin/raj.com', 'contact_details': { 'phone': '7326763269'}}    

# patient1 = Patient(**patient_info)

# update_patient_data(patient1)


#! Example 04

#? Field validator... 
# from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
# from typing import List, Dict, Optional,Annotated

# class Patient(BaseModel):
#     name: str
#     age: int
#     email: EmailStr
#     weight: float
#     married: Optional[bool] = False
#     allergies: Optional[List[str]] = None  
#     contact_details: dict[str, str]



#   #? email should be of specific domains... 
#     @field_validator('email')
#     @classmethod
#     def emailValidator(cls, value):
#         valid_domains = ['hdfc.com', 'icici.com']
#         domain_name = value.split('@')[-1]

#         if domain_name not in valid_domains:
#             raise ValueError('Not a valid domain')

#         return value 

#      #?  name should be in cappital
#     @field_validator('name')
#     @classmethod
#     def transform_name(cls, value):
#         return value.upper()


#   #? field_validator work in two modes: 'bofore' and 'after'(by default)
#     @field_validator('age', mode='before') 
#     @classmethod
#     def validate_age(cls, value):
#         if 0 < value < 100:
#             return value
#         else:
#             raise ValueError("Age should be in between 0 and 100")          



# def update_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print(patient.married)
#     print(patient.allergies)



# patient_info = {'name': 'raj', 'age': '18','email': "raj@hdfc.com", 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '7326763269'}}    

# patient1 = Patient(**patient_info)   #? validation performed

# update_patient_data(patient1)



#! Example 05
#? model validators(perform validation on more than 1 fields)

# from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
# from typing import List, Dict, Optional,Annotated

# class Patient(BaseModel):
#     name: str
#     age: int
#     weight: float
#     married: Optional[bool] = False
#     allergies: Optional[List[str]] = None  
#     contact_details: dict[str, str]


# @model_validator(mode='after')
# def validate_emergency_contact(self):
#     if self.age > 60 and 'emergency' not in self.contact_details:
#         raise ValueError('Patient older than 60 must have an emergency contact details')
#     return self

# def update_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print(patient.married)
#     print(patient.allergies[0])



# patient_info = {'name': 'raj', 'age': 20, 'weight': 56.3,  'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'raj@gmail.com', 'phone': '7326763269'}}    

# patient1 = Patient(**patient_info)

# update_patient_data(patient1)





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