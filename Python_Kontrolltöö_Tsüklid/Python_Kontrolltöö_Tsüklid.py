from math import *
from random import *

#3
quention=0.0
while type(quention) !=int:
    try:
        quention=int(input("sisestage number"))
    except:
       TypeError
fil=0
fil1=1
while quention > 0:
    answer_of = quention % 10
    fil = fil + answer_of
    fil1 = fil1 * answer_of
    quention = quention // 10
print("Arvude summa antud arvust: " + str(fil))
print("Antud arvu korrutis: " + str(fil1))


#4
a=input()

even = 0
odd = 0

for i in a:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even: %d, odd: %d)" % (even,odd))

#5
summ = 0

for i in range(1, 100 + 1):

   summ += i

print(summ)

#1
print()
n=randint(1,9)
print("n")
while n!=1:
   print("    /V\ ")
   print("   / V \ ")
   print("  / V V \  ")
   print(" /VV V VV\ ")
   print()
   n=0

#2
g=float(input("Sisesta arv"))
p = 1
for x in range(1, g, 2): p *= x
print(p)