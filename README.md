# Diagnosis API running on docker Postgres, Gunicorn, and Nginx


#To get the application running ensure you have docker running on server

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
2. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
3. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
2. Build the images and run the containers:

    ```
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1439](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
    
#####  UPLOADING ICD-CODES  
 1.To upload sample ICD-CODES,navigate below url
  ```
    http://localhost:8000/upload
```

#### TESTING API's
pass default ICD=ICD-10 to get codes under ICD-10 updates
```
    http://127.0.0.1:8000/codes/all?ICD=ICD-10
```
sample response (response is paginated in batches of 10)
```
    {
    "count": 71616,
    "next": "http://127.0.0.1:8000/codes/all?ICD=ICD-10&page=2",
    "previous": null,
    "results": [
        {
            "id": 188591,
            "created": "2021-02-08T17:57:05.645994Z",
            "category_code": "A00",
            "diagnosis_code": "0",
            "full_code": "A000",
            "ab_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
            "full_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
            "category_title": "Cholera"
        },
        {
            "id": 188592,
            "created": "2021-02-08T17:57:05.650062Z",
            "category_code": "A00",
            "diagnosis_code": "1",
            "full_code": "A001",
            "ab_description": "Cholera due to Vibrio cholerae 01, biovar eltor",
            "full_description": "Cholera due to Vibrio cholerae 01, biovar eltor",
            "category_title": "Cholera"
        },
       
    ]
```
call paginated 'next' value to get the next page data

```
http://127.0.0.1:8000/codes/all?ICD=ICD-10&page=2
```
sample response

```
{
    "count": 71616,
    "next": "http://127.0.0.1:8000/codes/all?ICD=ICD-10&page=3",
    "previous": "http://127.0.0.1:8000/codes/all?ICD=ICD-10",
    "results": [
        {
            "id": 188611,
            "created": "2021-02-08T17:57:05.694931Z",
            "category_code": "A022",
            "diagnosis_code": "4",
            "full_code": "A0224",
            "ab_description": "Salmonella osteomyelitis",
            "full_description": "Salmonella osteomyelitis",
            "category_title": "Localized salmonella infections"
        },
        {
            "id": 188612,
            "created": "2021-02-08T17:57:05.697111Z",
            "category_code": "A022",
            "diagnosis_code": "5",
            "full_code": "A0225",
            "ab_description": "Salmonella pyelonephritis",
            "full_description": "Salmonella pyelonephritis",
            "category_title": "Localized salmonella infections"
        },
      
    ]
}
```
Create a new diagnosis code record

```
URL: http://127.0.0.1:8000/codes
ACTION: POST
TYPE: JSON
REQUEST SAMPLE: 
{

    "category_code": "A04212",
    "diagnosis_code": "2",
    "full_code": "A3255",
    "ab_description": "pat test",
    "full_description": "my test details",
    "category_title": "my test title",
    "ICD":"ICD-10"
}

```
Update diagnosis code record

```
http://127.0.0.1:8000/codes?id=260281
ACTION: PUT
TYPE: JSON
REQUEST SAMPLE: 
{
    "category_code": "9S9DFGSDG",
    "diagnosis_code": "1412F",
    "full_code": "AFDGj",
    "ab_description": "pat new update",
    "full_description": "my test details",
    "category_title": "my test kwabena kojo own"
}

```
DELETE diagnosis code record
```
http://127.0.0.1:8000/codes?id=260281
ACTION: DELETE
```

GET diagnosis code recored

```
http://127.0.0.1:8000/codes?id=260281
ACTION: GET
TYPE: JSON
RESPONSE SAMPLE: 
{
    "id": 260212,
    "created": "2021-02-08T20:06:39.856976Z",
    "category_code": "A00",
    "diagnosis_code": "0",
    "full_code": "A000",
    "ab_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
    "full_description": "Cholera due to Vibrio cholerae 01, biovar cholerae",
    "category_title": "Cholera"
}

```
