from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

TRIP_SEARCH_RANGE = 2*30 # 2 month

data_manager = DataManager()
flight_search = FlightSearch()

### ----------------- Update IATA values for each city. ----------------- ###
# # Run only once.
# # If you want to add more destination cities:
# #     - add to the google sheet the names of the cities.
# #     - run the line below again.

# data_manager.update_iata()

### ----------------- Search flights. ----------------- ###
tommorow = datetime.now() + timedelta(days=1)
search_range = datetime.now() + timedelta(days=TRIP_SEARCH_RANGE)
lowest_prices = data_manager.get_lowest_prices()
sheet_data = data_manager.get_sheet_data()

for dest in sheet_data:
    flight = flight_search.search_flight(
        date_from=tommorow.strftime("%d/%m/%Y"), 
        fly_to=dest["iata"],
        date_to=search_range.strftime("%d/%m/%Y"),
        lowest_prices = lowest_prices
    )
    if flight != None:
        if flight.price < int(dest["lowestPrice"]):
            # update google sheet
            data_manager.update_flight(flight.arrival_city_name, flight.price)
            print("Sheet updated!")

