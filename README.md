# Fondeadora

#### Download the project
```bash
git clone git@github.com:karlozz157/fondeadora.git
```

#### Build 
```bash
cd fodeadora && docker build -t fo .
```

#### Run
```bash
docker run -p 6969:6969 fo
```

#### Populate the database
```bash
curl -X POST http://localhost:6969/seed
```

#### Check the transactions
```bash
curl -X GET http://localhost:6969/report/{date}
```

#### Create the reconciliation report
```bash
curl -X POST http://localhost:6969/report?date={date}
```


## Tests
```bash
pytest tests
```


## Plus

#### Get transactions by user_id
```bash
curl -X POST http://localhost:6969/user/{user_id}/transactions
```

#### Add crontab to create report
```
0 0 * * * curl -X POST "http://0.0.0.0:8000/report?date=$(date +\%Y-\%m-\%d)" 
```


## Evidence
#### Run the seed
![image](https://github.com/karlozz157/fondeadora/assets/4811721/cbd1616f-e791-42b8-9eec-721e9bc7b1ef)

#### Get the transactions by date
![image](https://github.com/karlozz157/fondeadora/assets/4811721/a2849403-f753-4102-8ec0-dee19e6558e7)

#### Create report (right the endpoit is giving an error but you can run the tests)
![image](https://github.com/karlozz157/fondeadora/assets/4811721/66c28f5b-12a3-4fbf-ab26-3842368898c1)

#### tests
![image](https://github.com/karlozz157/fondeadora/assets/4811721/6c84e692-4a21-48f2-a102-cbdfc0e1261e)

#### Get the transactions by user_id
![image](https://github.com/karlozz157/fondeadora/assets/4811721/622e3331-82e5-4d72-b28d-58a2e93b1e9a)

