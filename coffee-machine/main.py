from data import MENU, resources

money = 0

def report():
    """Prints the current machine resource values."""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {money}")

def is_resource_sufficient(order):
    """Returns True if there are enough resources at the machine, otherwise returns False."""
    required_water = MENU[order]["ingredients"]["water"]
    required_coffee = MENU[order]["ingredients"]["coffee"]
    required_milk = 0
    if order != "espresso":
        required_milk = MENU[order]["ingredients"]["milk"]

    return resources["water"] >= required_water and resources["milk"] >= required_milk and resources["coffee"] >= required_coffee

def proccess_coins(quarters, dimes, nickles, pennies):
    """Returns the inserted amount by the user."""
    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

def make_coffee(order):
    """Updates machine resources."""
    required_water = MENU[order]["ingredients"]["water"]
    required_coffee = MENU[order]["ingredients"]["coffee"]
    required_milk = 0
    if order != "espresso":
        required_milk = MENU[order]["ingredients"]["milk"]
    
    resources["water"] -= required_water
    resources["milk"] -= required_milk
    resources["coffee"] -= required_coffee

def is_succ_transaction(order):
    """Checks if a single transaction went successfully."""
    required_money = MENU[order]['cost']
    if is_resource_sufficient(order):
        print(f"{order} costs {required_money}. Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))

        inserted_money = proccess_coins(quarters, dimes, nickles, pennies)
        if inserted_money < required_money:
            print("Sorry.that's not enough money. Money refunded.")
            return False
        elif inserted_money > required_money:
            print(f"Here is ${inserted_money - required_money : .2f} in change.")

        # whether there is a change or not (but exact amount), the order succeeded.
        global money
        money += required_money # update machine profit.
        return True
    else:
        print("Sorry, the machine is missing products.")
        return False

def machine_is_on():
    """Run while the machine is ON"""
    while True:
        order = input("\nWhat would you like to order? (espresso/latte/cappuccino) OR FOR STAFF ONLY (report/off): ").lower()
        if order == "off":
            return
        if order == "report":
            report()
        elif is_succ_transaction(order):
            make_coffee(order)
            print(f"Thank you for your order. Enjoy your {order}!")
            
machine_is_on()