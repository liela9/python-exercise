DEPARTURE_AIRPORT = "TLV"

# This class responsible for structuring the flight data.
class FlightData:
    def __init__(self, arrival_airport_code, arrival_city_name, departure_date, arrival_date, price, airlines, available_seats) -> None:
        self.departure_airport_code = DEPARTURE_AIRPORT
        self.arrival_airport_code = arrival_airport_code
        self.arrival_city_name = arrival_city_name
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.price = price
        self.airlines = airlines
        self.available_seats = available_seats
