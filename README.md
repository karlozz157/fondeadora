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
![image](https://github.com/karlozz157/fondeadora/assets/4811721/656075aa-1835-4b7c-bc85-112c1fca3843)

#### Get the transactions by date
![image](https://github.com/karlozz157/fondeadora/assets/4811721/c3455020-87cb-4d08-b90b-b99792e91b34)

#### Create report (right the endpoit is giving an error but you can run the tests)
![image](https://github.com/karlozz157/fondeadora/assets/4811721/79dee99f-91ea-4cf9-9baf-f72d338c2789)

#### tests
![image](https://github.com/karlozz157/fondeadora/assets/4811721/3f39a179-4319-4f68-8252-bf7e8549fc26)

#### Get the transactions by user_id
![image](https://github.com/karlozz157/fondeadora/assets/4811721/8c69f2dc-9a70-45d2-b015-e29fef7f2da7)

