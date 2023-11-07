import requests
from flight_search import FlightSearch

SHEETY_ENDPOINT = "https://api.sheety.co/8836c7947462e4e84ce2fea8bf8905c8/flightDeals/1Sheets"

# This class responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self) -> None:
        self.flight_search = FlightSearch()

        sheety_response = requests.get(url=SHEETY_ENDPOINT)
        sheety_response.raise_for_status()
        self.sheet_data = sheety_response.json()["1Sheets"]
        
    def get_sheet_data(self) -> list:
        return self.sheet_data

    def get_lowest_prices(self) -> list:
        """Returns all the lowest prices (per destination) from the google sheet."""
        respone = requests.get(url=SHEETY_ENDPOINT)
        respone.raise_for_status()
        data = respone.json()["1Sheets"] # list of dicts (dict = row in the sheet)

        lowest_prices = []
        for dest in data:
            lowest = {
                "city": dest["city"],
                "price": dest["lowestPrice"]
            }
            lowest_prices.append(lowest)
        return lowest_prices
    
    def update_iata(self) -> None:
        """Updates IATA values for each city in the google sheet."""
        # get relevant IATA value for each city using FlightSearch module.
        for row in self.sheet_data:
            iata = self.flight_search.get_IATA(row["city"])
            sheet_inputs = {
                "1Sheet": {
                    "iata": iata
                }
            }
            # update the "sheet_data" variable.
            row["iata"] = iata

            # update the google sheet.
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{row['id']}", json=sheet_inputs)
            response.raise_for_status()
   
    def update_flight(self, city:str, price:int) -> None:
        """Updates google sheet with the found flight."""
        row = [row for row in self.sheet_data if row["city"] == city]
        sheet_inputs = {
            "1Sheet": {
                "lowestPrice": price
            }
        }
        # update the "sheet_data" variable.
        row[0]["price"] = price

        # update the google sheet.
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{row[0]['id']}", json=sheet_inputs)
        response.raise_for_status()