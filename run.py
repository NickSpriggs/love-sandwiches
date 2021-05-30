import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('credentials.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figure input from user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10, 20, 30, 40, 50, 60\n")

    data_str = input("Enter your data here: ")

    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, convert all string values into integers.
    Raise ValueError, if strings cannot be converted into int,
    or if there aren't exactly 6 values
    """

    try:
        [int(value) for value in values] # Converts list of strings into list of ints
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you input: {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        # The ValueError object here contains all the details of the error raise in the try block

get_sales_data()


