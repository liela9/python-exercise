import requests
from flight_data import FlightData
from secret_vars import TEQUILA_API_KEY

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
DEPARTURE_AIRPORT = "TLV"
MIN_TRIP_LEN = 5
MAX_TRIP_LEN = 8
CURRENCY = "ILS" # Israeli Shekels

# This class responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self) -> None:
        self.headers = {
            "apikey": TEQUILA_API_KEY
        }

    def find_min_price_flight(self, city:str, data:list, lowest_prices:list) -> dict:
        """Returns the flight to 'city' that has the lowest price (should be less than what is in the google sheet)."""
        # get 'lowest price' from the google sheet by city name.
        lowest_price = [dest["price"] for dest in lowest_prices if dest["city"] == city]

        ret_flight = None
        for flight in data:
            if flight["price"] < lowest_price[0]:
                ret_flight = flight
        return ret_flight

    def get_IATA(self, city_name:str) -> str:
        """Returns the IATA code by city name using 'Tequila' API."""
        query = {"term": city_name}

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=query, headers=self.headers)
        response.raise_for_status()
        iata = response.json()["locations"][0]["code"]
        return iata
    
    def search_flight(self, date_from: str, fly_to:str, date_to:str, lowest_prices:list) -> FlightData:
        """Returns a FlightData object by city with lowest price."""
        query = {
            "fly_from": DEPARTURE_AIRPORT,
            "date_from": date_from,
            "fly_to": fly_to,
            "date_to": date_to,
            "flight_type": "round",
            "nights_in_dst_from": MIN_TRIP_LEN,
            "nights_in_dst_to": MAX_TRIP_LEN,
            "curr": CURRENCY,
            "max_stopovers": 0 # direct flight
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/search", params=query, headers=self.headers)
        response.raise_for_status()

        try:
            data = response.json()["data"]
        except IndexError:
            print(f"No flights found for {fly_to}.")
            return None
        
        min_price_flight = self.find_min_price_flight(data[0]["cityTo"], data, lowest_prices)
        if min_price_flight == None:
            print(f"No cheaper flight found for {fly_to}.")
            return None
        
        new_flight = FlightData(
            arrival_airport_code = min_price_flight["cityCodeTo"],
            arrival_city_name = min_price_flight["cityTo"],
            departure_date = min_price_flight["dTime"],
            arrival_date = min_price_flight["aTime"],
            price = min_price_flight["price"],
            airlines = min_price_flight["airlines"],
            available_seats = min_price_flight["availability"]["seats"]
        )
        print(f"Found: flight to {min_price_flight['cityTo']}, {min_price_flight['price']}₪")
        return new_flight

    