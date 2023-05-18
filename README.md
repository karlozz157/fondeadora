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

## Plus

#### Get transactions by user_id
```bash
curl -X POST http://localhost:6969/user/{user_id}/transactions
```

#### Add create report to crontab
```
0 0 * * * curl -X POST "http://0.0.0.0:8000/report?date=$(date +\%Y-\%m-\%d)" 
```
