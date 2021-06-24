#River Camacho
#Lab 8 p 2

#This program converts your numeric entry
#into an actual date.





def date_format(user_date):
    user_date_values = user_date.split("/")
    user_month = user_date_values[0]
    user_day = user_date_values[1]
    user_year = user_date_values[2]

    return user_month, user_day, user_year

def main():

    user_date = input("Enter a date in the form mm/dd/yyyy:")

    months = ["January", "Febuary", "March", \
              "April", "May", "June",\
              "July", "August", "September", \
              "October", "November", "December"]

    user_month, user_day, user_year = date_format(user_date)

    user_month_index = int(user_month) - 1

    user_month_name = months[user_month_index]

    new_date_format = user_month_name + " " + user_day + ", " + user_year

    print("You typed " + user_date, "The format of your date was changed \
to " + new_date_format, sep = "\n")

main()
