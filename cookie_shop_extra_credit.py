"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""


def bake_cookies(filepath): #calls check_if_file_edited(filepath)
    """
    Opens up the CSV data file from the path specified as an argument.
    - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
    - Creates a dictionary with the data from each line.
    - Adds each dictionary to a list of all cookies that is returned.

    :param filepath: The path to the data file.
    :returns: A list of all cookie data, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.

    check_if_file_edited(filepath) #checks if dietary restrictions have been added to the file and adds them if they haven't been added yet

    file = open(filepath, mode='r')
    lines = file.readlines()
    file.close()
    
    all_cookies = []
    
    for line in lines:
        line = line.strip()
        separated = line.split(',')
        if not separated[0].isdigit():
            continue
        dictionary = {}
        dictionary['id'] = int(separated[0])
        dictionary['title'] = str(separated[1])
        dictionary['description'] = str(separated[2])
        dictionary['price'] = float(separated[3][1:])
        if separated[4] == 'True':                 #stores values for 'sugar_free', 'gluten free', and 'contains nuts' as booleans
            dictionary['sugar_free'] = True
        elif separated[4] == 'False':
            dictionary['sugar_free'] = False   

        if separated[5] == 'True':
            dictionary['gluten_free'] = True  
        elif separated[5] == 'False':
            dictionary['gluten_free'] = False  

        if separated[6] == 'True':
            dictionary['contains_nuts'] = True
        elif separated[6] == 'False': 
            dictionary['contains_nuts'] = False

        all_cookies.append(dictionary)

    return all_cookies
    

def welcome():
    """
    Prints a welcome message to the customer in the format:

      Welcome to the Python Cookie Shop!
      We feed each according to their need.

    """
    # write your code for this function below this line
    print("Welcome to the Python Cookie Shop!\nWe feed each according to their need.\n")


def get_cookie_from_dict(id, cookies):
    """
    Finds the cookie that matches the given id from the full list of cookies.

    :param id: the id of the cookie to look for
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: the matching cookie, as a dictionary
    """
    # write your code for this function below this line
    for cookie in cookies:
        if int(id) == cookie['id']:
            return cookie


def solicit_quantity(id, cookies):  #calls get_cookie_from_dict(id, cookies)
    """
    Asks the user how many of the given cookie they would like to order.
    - Validates the response.
    - Uses the get_cookie_from_dict function to get the full information about the cookie whose id is passed as an argument, including its title and price.
    - Displays the subtotal for the given quantity of this cookie, formatted to two decimal places.
    - Follows the format (with sample responses from the user):

        My favorite! How many Animal Cupcakes would you like? 5
        Your subtotal for 5 Animal Cupcake is $4.95.

    :param id: the id of the cookie to ask about
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: The quantity the user entered, as an integer.
    """
    # write your code for this function below this line
    cookie = get_cookie_from_dict(id, cookies)
    if cookie['title'][-1] == 's':
        while True:
            num_cookie = input(f"My favorite! How many {cookie['title']} would you like? ")
            if num_cookie.isdigit():
                break
        num_cookie = int(num_cookie)
        total_price = num_cookie * cookie['price']
        if num_cookie == 1:
            print(f"Your subtotal for {num_cookie} {cookie['title'][:-1]} is ${format(total_price, '.2f')}.\n")
        else:
            print(f"Your subtotal for {num_cookie} {cookie['title']} is ${format(total_price, '.2f')}.\n")
    else:
        while True:
            num_cookie = input(f"My favorite! How many {cookie['title']}s would you like? ")
            if num_cookie.isdigit():
                break
        num_cookie = int(num_cookie)
        total_price = num_cookie * cookie['price']
        if num_cookie == 1:
            print(f"Your subtotal for {num_cookie} {cookie['title']} is ${format(total_price, '.2f')}.\n")
        else:
            print(f"Your subtotal for {num_cookie} {cookie['title']}s is ${format(total_price, '.2f')}.\n")
    return num_cookie


def solicit_order(cookies): #calls solicit_quantity(id, cookies)
    """
    Takes the complete order from the customer.
    - Asks over-and-over again for the user to enter the id of a cookie they want to order until they enter 'finished', 'done', 'quit', or 'exit'.
    - Validates the id the user enters.
    - For every id the user enters, determines the quantity they want by calling the solicit_quantity function.
    - Places the id and quantity of each cookie the user wants into a dictionary with the format
        {'id': 5, 'quantity': 10}
    - Returns a list of all sub-orders, in the format:
        [
          {'id': 5, 'quantity': 10},
          {'id': 1, 'quantity': 3}
        ]

    :returns: A list of the ids and quantities of each cookies the user wants to order.
    """
    # write your code for this function below this line
    order_list = []

    while True:
        id_cookie = input("Please enter the id of any cookie you would like to purchase. (Enter 'finished', 'done', 'quit', or 'exit' if you have finished ordering): ")
        if id_cookie in ['finished', 'done', 'quit', 'exit']:
            break
        elif id_cookie.isdigit(): 
            id_cookie = int(id_cookie)
            for cookie in cookies:
                if id_cookie == cookie['id']:
                    order_dict = {}
                    order_dict['id'] = id_cookie
                    order_dict['quantity'] = solicit_quantity(id_cookie, cookies)
                    order_list.append(order_dict)
    
    return order_list


def display_order_total(order, cookies):
    """
    Prints a summary of the user's complete order.
    - Includes a breakdown of the title and quantity of each cookie the user ordereed.
    - Includes the total cost of the complete order, formatted to two decimal places.
    - Follows the format:

        Thank you for your order. You have ordered:

        -8 Animal Cupcake
        -1 Basboosa Semolina Cake

        Your total is $11.91.
        Please pay with Bitcoin before picking-up.

        Thank you!
        -The Python Cookie Shop Robot.

    """
    # write your code for this function below this line
    print("\nThank you for your order. You have ordered:\n")

    total_price = 0

    for ord in order:
        for cookie in cookies:
            if ord['id'] == cookie['id']:
                title = cookie['title']
                if ord['quantity'] == 1:
                    if title[-1] == 's':
                        print(f"-1 {title[:-1]}")
                    else:
                        print(f"-1 {title}")
                else:
                    if title[-1] == 's':
                        print(f"-{ord['quantity']} {title}")
                    else:
                        print(f"-{ord['quantity']} {title}s")
                total_price += ord['quantity'] * cookie['price']

    print(f"\nYour total is ${format(total_price, '.2f')}.")
    print("Please pay with Bitcoin before picking-up.\n")
    print("Thank you!")
    print("-The Python Cookie Shop Robot.")


def check_if_file_edited(filepath): #new function for extra credit      #calls add_diet_to_file(filepath)
    file = open(filepath, mode='r')
    lines = file.readlines()
    file.close()

    if 'sugar_free' not in lines[0] and 'gluten_free' not in lines[0] and 'contains_nuts' not in lines[0]:
        add_diet_to_file(filepath)  #adds the dietary restrictions to cookies.csv only if they haven't been added yet


def add_diet_to_file(filepath): #new function for extra credit
    file = open(filepath, mode='r')
    lines = file.readlines()
    file.close()

    first_row = "id,title,description,price,sugar_free,gluten_free,contains_nuts\n"

    new_diet_all = {
        1: {'sugar_free': True, 'gluten_free': False, 'contains_nuts': False},
        2: {'sugar_free': False, 'gluten_free': True, 'contains_nuts': False},
        3: {'sugar_free': False, 'gluten_free': True, 'contains_nuts': False},
        4: {'sugar_free': True, 'gluten_free': True, 'contains_nuts': False},
        5: {'sugar_free': False, 'gluten_free': True, 'contains_nuts': True},
        6: {'sugar_free': False, 'gluten_free': True, 'contains_nuts': False},
        7: {'sugar_free': False, 'gluten_free': True, 'contains_nuts': False},
        8: {'sugar_free': False, 'gluten_free': True, 'contains_nuts': True},
        9: {'sugar_free': True, 'gluten_free': True, 'contains_nuts': False},
        10: {'sugar_free': False, 'gluten_free': False, 'contains_nuts': False}}

    list_new_lines = [first_row]    #list containing updated lines, headers are pre-added already in the first row
    
    for line in lines[1:]:  #skips first row since it contains the names of the keys or headers
        line_turned_list = line.strip().split(',')
        id_cookie = int(line_turned_list[0])
        diets_cookie = new_diet_all[id_cookie]
        edited_line = line.strip() + f",{diets_cookie['sugar_free']},{diets_cookie['gluten_free']},{diets_cookie['contains_nuts']}\n"
        list_new_lines.append(edited_line)
    
    # writes list_new_lines into cookies.csv, overwriting original text
    file = open(filepath, mode='w')
    for line in list_new_lines:
        file.write(line)
    file.close()


def ask_allergies_and_display(cookies): #new function for extra credit
    print("We'd hate to trigger an allergic reaction in your body. So please answer the following questions:\n")
    
    while True:
        nuts_allergic = input("Are you allergic to nuts? ").lower()
        if nuts_allergic in ['yes', 'y', 'no', 'n']:
            break
    while True:
        gluten_allergic = input("Are you allergic to gluten? ").lower()
        if gluten_allergic in ['yes', 'y', 'no', 'n']:
            break
    while True:
        is_diabetic = input("Do you suffer from diabetes? ").lower()
        if is_diabetic in ['yes', 'y', 'no', 'n']:
            break
    
    friendly_cookies = []

    for cookie in cookies:
        include_cookie = True

        if nuts_allergic in ['yes', 'y']:
            if cookie['contains_nuts']:
                include_cookie = False
        if gluten_allergic in ['yes', 'y']:
            if not cookie['gluten_free']:
                include_cookie = False
        if is_diabetic in ['yes', 'y']:
            if not cookie['sugar_free']:
                include_cookie = False

        if include_cookie == True:
            friendly_cookies.append(cookie)

    if nuts_allergic in ['yes', 'y']:
        n = "without nuts, "
    else:
        n = ""

    if gluten_allergic in ['yes', 'y']:
        g = "without gluten, "
    else:
        g = ""

    if is_diabetic in ['yes', 'y']:
        s = "without sugar, "
    else:
        s = ""

    #displays user-friendly cookies
    print(f"\nGreat! Here are the cookies {n}{g}{s}that we think you might like:\n")
    for cookie in friendly_cookies:
        print(f"#{cookie['id']} - {cookie['title']}")
        print(cookie['description'])
        print(f"Price: ${format(cookie['price'], '.2f')}\n")


def run_shop(cookies):
    """
    Executes the cookie shop program, following requirements in the README.md file.
    - This function definition is given to you.
    - Do not modify it!

    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    welcome()
    ask_allergies_and_display(cookies)    #replaced def display_cookies(cookies) from cookie_shop.py
    order = solicit_order(cookies)
    display_order_total(order, cookies)
    