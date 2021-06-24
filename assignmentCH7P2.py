#River Camacho Assignment Ch 7 Part 2




def main():

    list_1 = [1,2,3,4,5]


    list_2 = [100,200,300,400,500]


    list_3 = list_1 + list_2

    list_3.sort()

    print("Orgiginal Combined Sorted List", list_3)

    print("Total is:", total_list(list_3))

    print("Min is:", min(list_3))

    print("Max is:", max(list_3))



def total_list(value_list):

    total = 0

    for num in value_list:
        total += num

    return total

main()

    

        
