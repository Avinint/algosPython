the_list = [20, 35, -15, 7, 55, 1, -22]

def tribulle(in_list):
    for lastUnsortedIndex in range (len(in_list) - 1, 0, -1):
        for i in range(0, lastUnsortedIndex):
            if in_list[i] > in_list[i + 1]:
                in_list[i], in_list[i+1] =  in_list[i+1], in_list[i]

tribulle(the_list)
print(the_list)