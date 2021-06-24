#River Camacho
#Lab 8

#This program opens a file and then
#counts the upper case, lowercase, digits, and spaces.

def main():

    infile = open('textfile.txt','r')

    file = infile.readlines()

    cap_count=0

    low_count=0

    space_count=0

    dig_count=0

    for lines in file:

        for ch in lines:

            if ch.isupper():
                cap_count+=1

            elif ch.islower():
                low_count+=1

            elif ch.isspace():
                space_count+=1

            elif ch.isdigit():
                dig_count+=1

    print("Upper Case:", cap_count)

    print("LowerCase:", low_count)

    print("Spaces:", space_count)

    print("Digits:", dig_count)


main()
