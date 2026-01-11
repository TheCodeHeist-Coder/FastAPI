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