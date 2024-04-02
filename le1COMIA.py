game_library = {'Game name': [], 'Cost':[], 'Quantity': []}

user_database = {"Username" :[], 'Inventory': {'Gamename': [], 'Quantity': []}, "password": [], 'Balance': 0}

admin_username = "admin"
admin_password = "adminpass"
def register():
    while True:
        try:
            username = input("Enter a valid username: ")
            if username in user_database:
                print("User name already exist")
            else:
                print("User name succesfully registerd.")
                register()
            password = input("Enter your password: ")
            if password not in user_database:
                print("password successfully registered.")
            else:
                print("Password already exist.")
                register()
            if len(password) < 8:
                print("Password must be greater than 8 characters")
            
            user_database["Username"] = username
            password['password'] = password
            print("Account successfuly registered.")
            loggedin_main(username)
            
        except ValueError:
            print("Invalid Input. Please try again")

def login():
    while True:
        try:
            username = input("Enter you Username:")
            if username in user_database:
                print("User found")
            else:
                print("Username does not exist")
                login()
            password = input("Enter your password: ")
            if password in user_database:
                print("Successfully logged in.")
            else:
                print("Invalid credentials. Please try again.")
                login()
            loggedin_main(username)
        except ValueError:
            print("Invalid input. Please try again")

def admin_login():
    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter your password: ")
            if username and password != admin_username and admin_password:
                print("Invalid credentials.")
            else:
                print("Admin Menu")
                print("1. Update game details")
                print("2. Log out")
                admin_actions = input("Enter you choice: ")
                if admin_actions == '1':
                    admin_menu()
                elif admin_actions == '2':
                    main()
                else:
                    print("Invalid input")
                    admin_login() 
        except ValueError:
            print("Invalid Input")

def admin_menu():
    while True:
        try:
            admin_input = input("What would you like to do?:")
            print("1. Change cost")
            print("2. Change quantity")

            if admin_input == '1':
                admin_change_price()
            elif admin_input =='2':
                admin_change_quantity()
            else:
                print("Invalid Input. Please try again.")
        except ValueError:
            print("Invalid INput. Please try again.")

def admin_change_price():
    while True:
        try:
            game_name = input("What game mwould you like to change?: ")
            if game_name not in game_library:
                print("Game does not exist!")
            else:
                new_price = input("Input new price: ")
                game_library["Cost"] += new_price
            print("Game price successfully changed.")
        except ValueError:
            print("Invalid input. Please try again")

def admin_change_quantity():
    while True:
        try:
            game_name = input("What game would you like to change:? ")
            if game_name not in game_library:
                print("Game does not exist.")

            else:
                new_quantity = input("Enter the new game quantity: ")
                game_library["Quantity"] += new_quantity
            print("Game quantity successfuly changed.")
        except ValueError:
            print("Invalid input. Please try again.")
        
def loggedin_main(username):
    while True:
        try:
            print(f"Logged in as {username}.")
            print("1. Rent a game")
            print("2. Retrun a game")
            print("3. Top-up Account")
            print("4. Display Inventory")
            print("5. Redeem game rental")
            print("6. Check points ")

            user_input = input("Enter your choice. ")
            if user_input == '1':
                rent_game(username)
            elif user_input == '2':
                return_game(username)
            elif user_input == '3':
                top_up(username)
            elif user_input == '4':
                display_inventory(username)
            elif user_input == '5':
                redeem_game(username)
            elif user_input == '6':
                check_point(username)
            else:
                print("Invalid input. PLease try again")

        except ValueError:
            print("Invalid input. PLease try again")

def rent_game(username):
    while True:
        try:
            game_to_rent = input("What game woud you like to rent?: ")
            if game_to_rent not in game_library:
                print("Game does not exist. ")
                rent_game(username)
            qunatity_to_rent = input("How many would you like to rent?: ")
            if qunatity_to_rent < game_library['Quantity']:
                print("Insuficient Stocks")
            total_cost = qunatity_to_rent * game_library["Cost"]
            if total_cost > user_database['Balance']:
                print("Insufficeint Balance")
            if qunatity_to_rent >= 0:
                print("No game rented.")
                rent_game(username)

            if game_to_rent in user_database:
                user_database['Inventory']['Quantity'][game_to_rent] += qunatity_to_rent
                user_database["Balance"] -= total_cost
            else:
                user_database["Balance"] -= total_cost
                user_database["Inventory"]['Gamename'].append(game_to_rent)
                user_database['Inventory']['Quantity'][game_to_rent] += qunatity_to_rent
            print("Game successfully rented.")
        except ValueError:
            print("Invalid input. Please try again.")
    
def return_game(username):
    pass
def top_up(username):
    pass
def display_inventory(username):
    pass
def redeem_game(username):
    pass
def check_point(username):
    pass

           

def main():
    while True:
        try:
            print("Welcome to the game rental system")
            print("1. Display available games")
            print("2. Regiter User")
            print("3. Log in")
            print("4. Admin Log in")
            print("5. Exit")

            user_input = input("What would you like to do?(Choose from 1 - 5): ")

            if user_input == '1':
                pass
            elif user_input == '2':
                register()
            elif user_input == '3':
                login()
            elif user_input == '4':
                admin_login()
            elif user_input =='5':
                SystemExit()

        except ValueError:
            print("Invalid Input. Please try again.")
main()

            

