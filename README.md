# Currency Exchange API
This directory contains an example of Python script to create a command line interface to Currency Exchange<br />
- Python CLI: Click <br />

Using Currency Exchange API developed by fyhao.

<hr />

## Usage
## To check CLI help
```
python ./app/main.py --help
```

### To get currency exchange by specifying the quotes of source and destination.
Parameters:<br />
- file: string, Input file path that contains a single JSON object per each line.<br />
- targetcurrency: string, The destination currency to convert to.<br />
Example input file data:
```
{ "value": 10, "currency": "EUR" }
{ "value": 100, "currency": "USD" }
{ "value": 1000, "currency": "JPY" }
```

Example command:<br />
To use prompt for input parameters
```
python ./app/main.py
```
Or manually set input parameters
```
python ./app/main.py --file=./input.txt --targetcurrency=JPY
```

<hr />

## Setup
### Prerequisites
- Python 3.9.7
- pip

### Setup for local running 
1. Set important environment variables in currency_exchange_cli/run.ps1
2. Open powershell then run the command this below command to setup
```
$ run.ps1
```
3. Now the cli is ready to call

<hr />

## Additional Information 
How to get Rapid API Application key 
1. Browse to https://rapidapi.com and create new user or login with exist user account. 
2. Browse to https://rapidapi.com/fyhao/api/currency-exchange or search for API called "Currency Exchange" by fyhao. RapidAPI will automatically create a new app for this API. 
3. Browse to https://rapidapi.com/developer/, select new app that created under My apps then select Security menu. The Application Key will be shown on the screen.

<hr />

## References
- https://click.palletsprojects.com/en/8.0.x/
- https://rapidapi.com/fyhao/api/currency-exchange