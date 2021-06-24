#River Camacho
#Lab 6
#3/31/2019

#Program Title
#Day at the Races


#Both of these programs are used to track the horse races and the
#amount earned for each horse.


#This program will read the data from the file and produce a
#report to the screen.

def main():



    try:
        total = 0
        count = 0
        print()
        print("Today's Winnings at Belmont Park")
        print("-------------------------------------")

        #Open the race.txt file
        race_file = open('race.txt', 'r')

        #Read the value from the file and
        #accumulate them
        horse = race_file.readline()

        while horse != '':

            #Read the amount field
            amount_earned = float(race_file.readline())
            count+= 1
            total += amount_earned
            average = total / count

            #Strip the \n from the horse names.
            horse = horse.rstrip('\n')

            #Display the record
            print('Horse:', horse)
            print('Purse:$', format(amount_earned, ',.2f'))
            
            #Read the next entry
            horse = race_file.readline()

        print('Total Purse for the day is: $', format(total, ',.2f'))
        print('The average purse for the day is: $', format(average, ',.2f'))

            

        #Close the file.
        race_file.close()
        
    except IOError:
              print('An error occured trying to read the file.')

    except ValueError:
              print('Non-numeric data found in the file.')

    except:
              print("An error occured.")
main()
    
