def date_converter(date):

    month_dict = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12",
    }

    temp_1 = date.split(", ")
    temp_2 = temp_1[0].split(" ")

    month = temp_2[0]
    numerical_month = month_dict.get(f"{month}")

    day = temp_2[1]

    if len(day) == 1:
        day = "0" + day

    year = temp_1[1]

    numerical_date = year + numerical_month + day

    return numerical_date
    

def time_converter(time):

    temp_1 = time.split(" ")
    temp_2 = temp_1[0].split(":")

    hours = temp_2[0]
    minutes = temp_2[1]

    if temp_1[1] == "PM" and hours != "12":
        hours = str(int(hours) + 12)
    if temp_1[1] == "AM" and hours == "12":
        hours = "00"

    if len(hours) == 1:
        hours = "0" + hours

    converted_time = hours + minutes
    
    return converted_time