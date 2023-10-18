import requests
from datetime import datetime
from tkinter import *

MY_AREA = "Ramat Gan"
# landmark of Ramat Gan
MY_LATITUDE = 32.068424 
MY_LONGITUDE = 34.824783
BG_PHOTO = "REST-API/shabbat-candles/candles.png"


def get_my_sunset_time():
    """Returns sunset time by location."""
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0 # 12 hours format
    }

    # get sunset data via API request
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status() # raise an exception when the status is not 200.
    data = response.json()
    # print(data)

    sunset = data["results"]["sunset"].split("T")[1].split(":")
    sunset_hour = sunset[0]
    sunset_minutes = sunset[1]

    print(f"{MY_AREA} sunset at {sunset_hour}:{sunset_minutes}")
    return (sunset_hour, sunset_minutes)


def is_time_to_light_candles():
    """Returns True if it is time to light Shabbat candles."""
    sunset_time = get_my_sunset_time()
    sunset_hour = int(sunset_time[0])
    sunset_minutes = int(sunset_time[1])

    week_day = datetime.now().weekday()
    current_hour = datetime.now().hour
    current_minutes = datetime.now().minute

    if week_day == 5 or current_hour == sunset_hour and current_minutes >= sunset_minutes or current_hour > sunset_hour: # if today is friday and it is the sunset time (or after)
        return True 
    return False


def raise_notice():
    """Raise a notice via 'Tkinter' window."""
    FONT = ("Arial", 35, "italic")

    window = Tk()
    window.title("Shabbat Shalom")

    canvas = Canvas(width=640, height=427)
    img = PhotoImage(file=BG_PHOTO)
    canvas.create_image(320, 213, image=img)
    canvas.create_text(440, 213, text="It is time to light \nShabbat candles", fill="white", font=FONT)
    canvas.pack()

    window.mainloop()


run = True
while run:
    if is_time_to_light_candles():
        raise_notice()
        run = False