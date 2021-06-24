#River Camacho
#Lab 7 List:
#Complete




                            #Rainfall Statistics


#Get User Entry
def rainfall_amounts(months):
    
    #NUM_MONTHS is used as a constant for the size of the list
    NUM_MONTHS = 12

    total_rainfall_list = []

    for month_index in range(NUM_MONTHS):

        month_rain = int(input("Enter the rainfall for " +\
                                 months[month_index] + ": " ))
        total_rainfall_list.append(month_rain)

    return total_rainfall_list
#Total up the Input
def total_rain_calc(total_rainfall_list):

    total_rainfall = 0

    for monthly_rain_index in range(len(total_rainfall_list)):
        total_rainfall += total_rainfall_list[monthly_rain_index]

    return total_rainfall
#Average the total of Input
def average_rainfall(total_rainfall, total_rainfall_list):
    num_months = len(total_rainfall_list)
    average_rain = total_rain_calc(total_rainfall_list) / num_months

    return average_rain

#Establsih Highest Entry
def highest_month( total_rainfall_list, months ):

    highest_rain = max(total_rainfall_list)

    highest_rain_index = total_rainfall_list.index(highest_rain)

    return months[highest_rain_index]

#Establish Lowest Entry
def lowest_month( total_rainfall_list, months ):

    lowest_rain = min(total_rainfall_list)

    lowest_rain_index = total_rainfall_list.index(lowest_rain)

    return months[lowest_rain_index]


#Print Output
def print_rainfall_stats(total_rainfall_list, months, total_rainfall, \
                         average_rainfall, highest_month, lowest_month):

    print("___________________________________________________________________")

    print()
    print("Here is the data you entered, \
along with the calculations.")
    print()

    print("___________________________________________________________________")
    print()
    print()
    print()
    

    for month_index in range(len(months)):

        print("Enter the rainfall for",\
              months[month_index] + ":",\
              total_rainfall_list[month_index])

    print("Total Rainfall: " + str(format(total_rainfall, ',.2f')), \
              "Average Rainfall: " + str(format(average_rainfall, ',.2f')), \
              "Highest Rainfall: " + highest_month, \
              "Lowest Rainfall: " + lowest_month, sep = "\n")


#List months and Call all functions    
def main():


    #List of Months
    months = ['January', 'Febuary', 'March', \
              'April', 'May', 'June', \
              'July', 'August', 'September', \
              'October', 'Novermber', 'December']

    

    

    total_rainfall_list = []

    total_rainfall_list = rainfall_amounts(months)

    total_rainfall = total_rain_calc(total_rainfall_list)

    average_monthly_rain = average_rainfall(total_rainfall, \
                                            total_rainfall_list)
    highest_month_rain = highest_month(total_rainfall_list, months)

    lowest_month_rain = lowest_month(total_rainfall_list, months)

    print_rainfall_stats(total_rainfall_list, months, total_rainfall, \
                         average_monthly_rain, highest_month_rain, \
                         lowest_month_rain)
    
    

                  
main()

    
