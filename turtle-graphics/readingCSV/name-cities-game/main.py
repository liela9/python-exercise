import pandas
import turtle

SCREEN_WIDTH = 592
SCREEN_HEIGHT = 852
IMAGE = "turtle-graphics/readingCSV/name-cities-game/blank-map-of-israel.gif"
CITIES_CSV_FILE = "turtle-graphics/readingCSV/name-cities-game/israel-cities-not-full.csv"
COOR_CSV_FILE = "turtle-graphics/readingCSV/name-cities-game/coordinates.csv"
DATA_CSV_FILE = "turtle-graphics/readingCSV/name-cities-game/data.csv"
MISSING_CITIES_CSV_FILE = "turtle-graphics/readingCSV/name-cities-game/missing-cities.csv"

screen = turtle.Screen()
cities_list = []
x_coors = []
y_coors = []
data_csv = pandas.read_csv(DATA_CSV_FILE)
guessed_cities = set()

def create_coor_csv_file():
    """
    Creates 'coordinates.csv'.
    Finds coordinates by mouse click on thr screen.
    Runs only once, at first.
    """
    # print all the coordinates we click on the screen (by Israel map).
    def get_mouse_click_coor(x, y):
        print(x, y)
    turtle.onscreenclick(get_mouse_click_coor)
    turtle.mainloop()
    # then we took all the coordinates from the output (terminal) and pasted them to a csv file named 'coordinates.csv'.

def generate_database():
    """Generates our database."""
    global cities_list, x_coors, y_coors 

    # create a list of cities.
    cities = pandas.read_csv(CITIES_CSV_FILE)
    cities_list = cities["Name"].to_list()

    # create lists of the x, y coordinates.
    coordinates = pandas.read_csv(COOR_CSV_FILE)
    x = coordinates["X"].to_list()
    y = coordinates["Y"].to_list()

    # create a dictionary of the cities and the coordinates.
    cities_coor_dict = {
        "Name": cities_list,
        "X": x,
        "Y": y
    }

    # convert the dictionary to a csv file.
    cities_coor_dataframe = pandas.DataFrame(cities_coor_dict)
    cities_coor_dataframe.to_csv("turtle-graphics/readingCSV/name-cities-game/data.csv")
    
    x_coors = data_csv["X"].to_list()
    y_coors = data_csv["Y"].to_list()

def setup_screen():
    """Setup the game screen."""
    screen.title("Israel Cities Game")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.addshape(IMAGE)
    turtle.shape(IMAGE)

def show_on_map(city, x, y):
    """Show the city name on the map."""
    txt = turtle.Turtle()
    txt.color("black")
    txt.penup()
    txt.hideturtle()
    txt.goto(x, y)
    txt.write(city, align="center")

def show_all():
    """Show all cities on the map."""
    i = 0
    while i < len(cities_list):
        show_on_map(cities_list[i], x_coors[i], y_coors[i])
        i += 1

def play():
    """Start game."""
    global guessed_cities

    keep_play = True
    while keep_play:
        input = screen.textinput(title="Enter A City", prompt=f"{len(guessed_cities)} Cities Correct")
        if input == None: # can be 'None' when input is empty or when user clicked 'Cancel'.
            keep_play = False
            continue

        user_answer = input.title() # convert to title case.
        row = data_csv[data_csv["Name"] == user_answer]

        if user_answer in cities_list:
            show_on_map(user_answer, int(row.X.iloc[0]), int(row.Y.iloc[0]))
            guessed_cities.add(user_answer)

        if len(guessed_cities) == len(cities_list):
            keep_play = False

def unguessed_cities():
    """Creates csv file with all the cities the user didn't guess."""
    # create a list with the unguessed cities.
    missing_cities = [city for city in cities_list if city not in guessed_cities]
    
    # create csv file from the list
    missing_cities_dataframe = pandas.DataFrame(missing_cities)
    missing_cities_dataframe.to_csv(MISSING_CITIES_CSV_FILE)


generate_database()
setup_screen()
play()
unguessed_cities()