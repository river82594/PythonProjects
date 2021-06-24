#River Camacho
#Lab 9 -Dictionaries

#This is a program that creates a dictionary containing
#course and room numbers.



def main():

    pair_1 = {'CS101':'3004', \
              'CS102':'4501', \
              'CS103':'6755', \
              'NT110':'1244', \
              'CM241':'1411'}

    pair_2 = {'CS101':'Haynes', \
              'CS102':'Alvarado', \
              'CS103':'Rich', \
              'NT110':'Burke', \
              'CM241':'Lee'}

    pair_3 = {'CS101':'8:00 a.m.', \
              'CS102':'9:00 a.m.', \
              'CS103':'10:00 a.m.', \
              'NT110':'11:00 a.m.', \
              'CM241':'1:00 p.m.'}

    while 0 < 1:
        
        entry = input("Enter a course number: ")

        

        if entry in pair_1 and pair_2 and pair_3:

            print('The details for course', entry, 'are:')
            print('Room Number: ', pair_1[entry])
            print('Instructor: ', pair_2[entry])
            print('Meeting Time: ', pair_3[entry])

        else:
            print("That course number is Invalid")
            

    

main()

    


    
    

    
