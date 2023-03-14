import math
import sys

a = 1000
#b = 1000
b = a
print(id(a),id(b))

b = 2000
print (id(a),id(b))

type(b)

#10
bool(1)

int("345")
float("345.60")

a,b,c,d,e = 1.5,2.5,3.5,4.5,5.5
print(a+b+c+d+e)
print(round(a)+round(b)+round(c)+round(d)+round(e))
print(int(a)+int(b)+int(c)+int(d)+int(e))
print(math.ceil(a)+math.ceil(b)+math.ceil(c)+math.ceil(d)+math.ceil(e))
round(345.50)

a = 20

if a > 21:
    print("a wieksze od 21")
else:
    print("czy a mniejsze od 21?")

a = 21

if a > 21:
    print("a wieksze od 21")
elif a < 21:
    print("a mniejsze")
else:
    print("a rowne 21")

a="tekst string"
print(sys.getrefcount(a))

c=5252332
print(sys.getrefcount(c))
#zmiana
