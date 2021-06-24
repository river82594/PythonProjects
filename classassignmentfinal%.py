#River Camacho
#In class Assignment Ch. 5 part 2.2
#Partner:
#This program will be calulating the area of a square
#based on a randomly generated integer

import random


def main():
    
    square_side = random.randint(1,101)
    print("Side measurment is", square_side)
    
    print("Area is", square_area(square_side))
    print("Perimeter is", square_perimeter(square_side))

main()
