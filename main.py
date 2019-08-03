def tribulle(liste_tri):
    swap = True
    passage = 0
    while swap:
        swap = False
        passage += 1
        for i in range(0, len(liste_tri) - passage):
            if liste_tri[i] > liste_tri[i + 1]:
                swap = True
                liste_tri[i], liste_tri[i + 1] = liste_tri[i + 1], liste_tri[i]
    return liste_tri
#=============================

def realtribulle(liste_tri):
    for lastUnsortedIndex in range(len(liste_tri) - 1, 0, -1):
        for i in range(0, lastUnsortedIndex):
            if liste_tri[i] > liste_tri[i + 1]:
                liste_tri[i], liste_tri[i + 1] = liste_tri[i + 1], liste_tri[i]
    return liste_tri

the_list = [20, 35, -15, 7, 55, 1, -22]
print(f"REAL  TRIBULLE: {realtribulle(the_list)}")
#==============================

def fact(num):
    if num < 2:
        return 1
    else:
        return num * fact(num - 1)

the_list = [4, 2, 3, 1, 6 ,8]
# print(tribulle(the_list))
# print(fact(6))
# print (int('3'))
# print(max([4,24, 1056, 2]))

 #==========================

def diviser_liste(total):
    amounts = []
    for i in (50, 20, 10, 5, 2, 1):
        amounts.append(total // i)
        total %= i
    return amounts

def diviser_dico(total):
    res = {}
    for i in (50, 20, 10, 5, 2, 1):
        res[i] = total // i
        total %= i
    return res

def processus(valeurs):
   data = [diviser_liste(v) for v in valeurs]
   return [sum(x) for x in zip(*data)]

# print(processus((77, 94, 80)))
#
# print(diviser_dico(147))
# print(diviser_liste(147))

#=======FIZZBUZZ=============

# def fizzbuzz(num):
#
#     for i in range(1,num):
#         fizz = not i % 3
#         buzz = not i % 5
#         if fizz and buzz:
#             print("FizzBuzz")
#         elif fizz:
#             print('Fizz')
#         elif buzz:
#             print("Buzz")
#         else:
#             print(i)

#=========SUPERFIZZBUZZ==========

fizzbuzz = ("fizzbuzz" if x % 5 == 0 and x % 3  == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5  == 0 else str(x)
            for x in range(0, 31))
for f in fizzbuzz:
    print(f)

# print('\n'.join('Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, 31)))

#=====PYTHON intersection entre listes============

list1 = [1,2,3,5]
list2 = [1,2,4,8]
print([l for l in list1 if l in list2])

#====================    UNION des listes   ==========
print(list(set(list1 + list2)))

#====================    ADDITIOn des listes   ==========
print([l + li for l in list1 for li in list2])

#===========================  COMPREHENSIVE DICTS    ==============
dico = {'name': 'john', 'first_name': 'wayne'}
dico = {k.upper():v.upper() for (k,v) in dico.items()}
print(dico.values())

#================= practise

the_list = [20, 35, -15, 7, 55, 1, -22]
def new_tribulle(input_list):
    for l in range(len(input_list) -1, 0, -1):
        for i in range(0, l):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
    return input_list

print(new_tribulle(the_list))