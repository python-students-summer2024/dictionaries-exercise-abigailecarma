"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""


def bake_cookies(filepath):
    """
    Opens up the CSV data file from the path specified as an argument.
    - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
    - Creates a dictionary with the data from each line.
    - Adds each dictionary to a list of all cookies that is returned.

    :param filepath: The path to the data file.
    :returns: A list of all cookie data, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    file = open(filepath, mode='r')
    lines = file.readlines()
    file.close()
    
    all_cookies = []    #masterlist containing the dictionaries of each cookie
    
    for line in lines:
        line = line.strip() #to remove \n
        separated = line.split(',') #creates a list of each line with 4 elements
        if not separated[0].isdigit():  #skips the first row since those are just headers
            continue
        dictionary = {}  #dictionary of each cookie/each line
        dictionary['id'] = int(separated[0])
        dictionary['title'] = str(separated[1])
        dictionary['description'] = str(separated[2])
        dictionary['price'] = float(separated[3][1:])
        all_cookies.append(dictionary)
        
    return all_cookies  #masterlist containing the dictionaries of each cookie


def welcome():
    """
    Prints a welcome message to the customer in the format:

      Welcome to the Python Cookie Shop!
      We feed each according to their need.

    """
    # write your code for this function below this line
    print("Welcome to the Python Cookie Shop!\nWe feed each according to their need.\n")


def display_cookies(cookies):
    """
    Prints a list of all cookies in the shop to the user.
    - Sample output - we show only two cookies here, but imagine the output continues for all cookiese:
        Here are the cookies we have in the shop for you:

          #1 - Basboosa Semolina Cake
          This is a This is a traditional Middle Eastern dessert made with semolina and yogurt then soaked in a rose water syrup.
          Price: $3.99

          #2 - Vanilla Chai Cookie
          Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner a combination of cinnamon ands ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?
          Price: $5.50

    - If doing the extra credit version, ask the user for their dietary restrictions first, and only print those cookies that are suitable for the customer.

    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below this line
    print("Here are the cookies we have in the shop for you:\n")
    for cookie in cookies:
        print(f"#{cookie['id']} - {cookie['title']}")
        print(cookie['description'])
        print(f"Price: ${format(cookie['price'], '.2f')}\n")   


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
            return cookie   #dictionary of selected cookie


def solicit_quantity(id, cookies):
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
    cookie = get_cookie_from_dict(id, cookies)  #dictionary of the cookie selected
    if cookie['title'][-1] == 's':  #if cookie title is already plural
        while True:
            num_cookie = input(f"My favorite! How many {cookie['title']} would you like? ")
            if num_cookie.isdigit():    #validates that the response can be converted to integer
                break
        num_cookie = int(num_cookie)
        total_price = num_cookie * cookie['price']  #calculates quantity multiplied by price of selected cookie
        if num_cookie == 1: #to make the cookie noun singular since only 1 cookie is ordered
            print(f"Your subtotal for {num_cookie} {cookie['title'][:-1]} is ${format(total_price, '.2f')}.\n")
        else:   #to make the cookie noun plural (leaves it as it is, since cookie noun is already plural)
            print(f"Your subtotal for {num_cookie} {cookie['title']} is ${format(total_price, '.2f')}.\n")
    else:   #if cookie title is singular
        while True:
            num_cookie = input(f"My favorite! How many {cookie['title']}s would you like? ")
            if num_cookie.isdigit():    #validates that the response is an integer
                break
        num_cookie = int(num_cookie)
        total_price = num_cookie * cookie['price']  #calculates quantity multiplied by price of selected cookie
        if num_cookie == 1: #to make the cookie noun singular since only 1 cookie is ordered (leaves it as it is)
            print(f"Your subtotal for {num_cookie} {cookie['title']} is ${format(total_price, '.2f')}.\n")
        else:   #to make the cookie noun plural 
            print(f"Your subtotal for {num_cookie} {cookie['title']}s is ${format(total_price, '.2f')}.\n")
    return num_cookie   #integer representing quantity of the selected cookie


def solicit_order(cookies):
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
    order_list = [] #list of all sub-orders, its elements are dictionaries

    while True:
        id_cookie = input("Please enter the id of any cookie you would like to purchase. (Enter 'finished', 'done', 'quit', or 'exit' if you have finished ordering): ")
        if id_cookie in ['finished', 'done', 'quit', 'exit']:   #stops loop, stops asking the user for input
            break
        elif id_cookie.isdigit():   #validates that the response can be converted to integer
            id_cookie = int(id_cookie)
            for cookie in cookies:
                if id_cookie == cookie['id']:
                    order_dict = {} #dictionary of selected cookie's id and quantity ordered
                    order_dict['id'] = id_cookie
                    order_dict['quantity'] = solicit_quantity(id_cookie, cookies)
                    order_list.append(order_dict)   #adds dictionary as an element to the list of all sub-orders
    
    return order_list   #list of all sub-orders, its elements are dictionaries


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

    for ord in order:   #order: list of all sub-orders, its elements are dictionaries
        for cookie in cookies:
            if ord['id'] == cookie['id']:   #matches the id from the order and the id from the masterlist of cookies
                title = cookie['title']
                if ord['quantity'] == 1:    #ensures that the cookie noun is singular
                    if title[-1] == 's':  
                        print(f"-1 {title[:-1]}")
                    else:
                        print(f"-1 {title}")
                else:                       #ensures that the cookie noun is plural
                    if title[-1] == 's':
                        print(f"-{ord['quantity']} {title}")
                    else:
                        print(f"-{ord['quantity']} {title}s")
                total_price += ord['quantity'] * cookie['price']    #calculates total price of entire order by adding up all the prices of each sub-order

    print(f"\nYour total is ${format(total_price, '.2f')}.")
    print("Please pay with Bitcoin before picking-up.\n")
    print("Thank you!")
    print("-The Python Cookie Shop Robot.")


def run_shop(cookies):
    """
    Executes the cookie shop program, following requirements in the README.md file.
    - This function definition is given to you.
    - Do not modify it!

    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    welcome()
    display_cookies(cookies)
    order = solicit_order(cookies)
    display_order_total(order, cookies)
