#River Camacho
#In-Class Assignment Ch. 6 Part 1
#3/25/2019

#This program demonstrates how to write charchters
#and numbers to a text file.


def main():

    #Open a file for writing.
    myfile = open('River_Camacho.txt', 'w')

    #Write Names
    myfile.write('River Camacho\n')
    myfile.write('Jermey Estrada\n')

    #Write Ages
    myfile.write(str(24) + '\n')
    myfile.write(str(25) + '\n')

    #Close the file
    myfile.close()

#Call Main Funciton
main()
    

    

