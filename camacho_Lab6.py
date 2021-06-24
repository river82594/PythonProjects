#River Camacho
#Lab 6
#3/31/2019

#Program Title
#Day at the Races


#Both of these programs are used to track the horse races and the
#amount earned for each horse.

#This program will read in the horse's names and amounts and
#write them to a file



def main():
    try:    
        #Open a file named race.txt
        outfile = open('race.txt', 'w')

        #Establish Loop
        another = "y"
        while another == "y":
                
            #Get the horse's name
                horse_name = input("Enter the horses name:")
            
            #Get the amount earned
                amount_earned = float(input("Enter the amount earned for horse:"))
            #Input Validation
                while amount_earned <= 0:
                    print("Error must be a positive integer.")
                    amount_earned = float(input("Enter the amount earned for horse:"))
                

            

            #Write the horse's names
                outfile.write(horse_name + '\n')

            #Write the amount earned.
                outfile.write(str(format(amount_earned, ',.2f')) +'\n')

            #Ask for next entry.
                another = input("ENTER y FOR NEXT ENTRY:")

        #Close the file
        outfile.close()
        print("Data appended to race.txt")


    
    except:
            print("Error")

    
    
        

      
        
        
main()



        

   
