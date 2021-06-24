#River Camacho
#Complete
#This program will usse a seperate module to calculate
#the distance in meters based on the object's falling distance.


import distance

def main():
    total = 0
    #Print Table Headings
    print()
    print('Time \t Falling Distance')
    print('---------------------------')
    #Count Controlled Loop
    for time in range(1,11):
        total += time
        print(time, '\t', format(distance.falling(time), ',.2f'))

main()
    


    
    
    









    









