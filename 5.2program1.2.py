#River Camacho
#In Class assignment Chapter 5
#Part 1.2:

#This program uses functions to convert
#Kilometer distances to mile distances.

keep_going = 'y'

while keep_going == 'y':

    def main():
        intro()
    #Get the distance in kilometers
        kilo_meters = int(input('Enter the distance you wish\
 to convert from kilometers to miles:'))
    #Convert the distance to miles
        kilo_to_miles(kilo_meters)

    #The intro function displays an intro to the program
    def intro():
        print()
        print('This program converts kilometers to miles.')
        print()
        print('For your reference Miles = Kilometers x 0.6214')
        print()

    #The kilo_to_miles function accepts a distance in kilometers
    #and displays the conversion to miles.

    def kilo_to_miles(kilometers):
        print()
        miles = kilometers * 0.6214
        print('That converts to', format(miles, ',.2f'), 'miles.')
        print()
        

    main()



    
