import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import click
from app.curr_exchange_api import CurrencyExchangeAPI
from app.utils import to_float


@click.command()
@click.option("--file", prompt="File path", help="Input file path.")
@click.option("--targetcurrency", prompt="Destination Currency", help="The destination currency to convert to.")
def exchange(
    file: str,
    targetcurrency: str
):
    """
    Currency Exchange by specifying the quotes of source and destination.

    """

    api = CurrencyExchangeAPI()
    output = []
    currency_exchange_rate = {}

    if not os.path.exists(file):
        print('Invalid input JSON file path.') 
        return False


    with open(file) as f:
        for line in f:
            try:   
                data = json.loads(line)

                if not data["value"] or not data["currency"]:
                    print ("Invalid input data format.")
                    continue
                
            except Exception as e:
                print ("Invalid input data format.")
                continue

            if data["currency"] not in currency_exchange_rate:
                try:            
                    response = api.get_exchange(source=data["currency"], destination=targetcurrency)
                    if response.status_code != 200:
                        error_msg = "An error occurred during the call to Currency Exchange API."
                        if response.text != None and response.text != "":
                            error_msg = response.text
                        print (error_msg)
                        continue
                    
                    exchange_rate = to_float(response.text)
                    if exchange_rate == 0:
                        error_msg = "An error occurred during calculating currency value."
                        print (error_msg)
                        continue

                    currency_exchange_rate[data["currency"]] = exchange_rate

                except Exception as e:
                    print (e)
                    continue

            converted_value = currency_exchange_rate[data["currency"]] * data["value"]
            converted_value = to_float(format(converted_value, ".2f"))

            print ({
                "value": converted_value,
                "currncy": targetcurrency
            })


if __name__ == "__main__":
    exchange()
