import random
########## Functions
def manual_weekday(date):
    """
    Goal: My own version of the weekday calculator. It proceeds in the same way as I do in my head. First the month, then the month and the day.
    in the end we consider exceptions such as years above 2000 and under 1900
    Input: Date as string in the dd.mmm.yyyy year format
    Output: Weekday as string
    """
    day, month, year = date.split('.')
    # Step 1: Get Key from Year
    key = year[-2:]
    key = int(key)
    key = key + key//4
    # Step 2: Add Month
    month_index = {"01": 1, "02": 4, "03": 4, "04":0 , "05": 2, "06": 5,
                   "07": 0, "08": 3, "09": 6, "10": 1, "11": 4, "12": 6}
    key = key + month_index[month]
    # Step 3: Add Day
    key = key + int(day)
    # Step 4: Calculate weekday
    weekdays_index = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    rest = abs(key%7)
    weekday = weekdays_index[rest]
    # 2000 Exception
    if 2099 > int(year) >= 2000:
        rest = rest -1
        weekday = weekdays_index[rest]
    # 1900 Exception
    if int(year)< 1900:
        weekday = weekdays_index[rest+2]
    # Leap Year Exception
    if int(year) % 4 == 0 and (int(month) == 1 or int(month) == 2):
        weekday = weekdays_index[rest-1]
    return weekday

def auto_weekday(date):
    """
    Goal: Use the datetime library to automatically tell the weekday
    Input: Date as string in the dd.mmm.yyyy year format
    Output: Weekday as string
    """
    try:
        # Convert the input date string to a datetime object
        date_obj = datetime.strptime(date, "%d.%m.%Y")
        # Get the weekday number (0: Monday, 1: Tuesday, ..., 6: Sunday)
        weekday_number = date_obj.weekday()
        # Map the weekday number to the corresponding weekday name
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekdays[weekday_number]
    except ValueError:
        return "Invalid date format. Please enter in the format dd.mm.yyyy."

def generate_random_date(year_start, year_end):
    day = random.randint(1, 28)  # You can adjust the range of days as needed
    month = random.randint(1, 12)
    year = random.randint(int(year_start), int(year_end))  # You can adjust the range of years as needed

    # Ensure that the day and month are represented as two digits
    day_str = str(day).zfill(2)
    month_str = str(month).zfill(2)
    year_str = str(year)

    date_string = f"{day_str}.{month_str}.{year_str}"
    return date_string

def application():
    print("_________")
    print("WEEKDAY TRAINER")
    print("_________")
    print("Choose a start and end year and then calculate the given date in your head. Insert your result. Try to max the Streak!") 
    # Load Highscore
    try:
        # Attempt to read the 'level' value from the file 'level_data.txt'
        with open("highscore.txt", "r") as file:
            highscore = int(file.read())
    except FileNotFoundError:
        # If the file is not found, set a default value for 'level'
        highscore = 1  # Set a default value (change this to your desired default)

    print("Your highscore is: " + str(highscore))
    year_start = input("START YEAR: ")
    year_end = input("END YEAR: ")
    level = 1
    # The Game
    while True:
        date = generate_random_date(year_start, year_end)
        print("_________")
        print("LEVEL " + str(level))
        print("DATE IS: " + date)
        answer = input("Weekday: ")
        if answer == manual_weekday(date):
            print("Right!")
            reset = False
            level = level + 1
        elif answer != manual_weekday(date):
            print("Wrong! It was a " + manual_weekday(date))
            break
    print("ENDE! You reached Level: " + str(level))
    print("Your highscore is: " + str(highscore))
    if level > highscore:
        highscore = level
        with open("highscore.txt", "w") as file:
            file.write(str(highscore))

application()
