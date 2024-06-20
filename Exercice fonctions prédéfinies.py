from math import sqrt
a = float(input("Quelle est le côté a ? "))
b = float(input("Quelle est le côté b ? "))
c = float(input("Quelle est le côté c ? "))
d = (a + b + c)/2  
e = sqrt(d*(d-a)*(d-b)*(d-c)) 
print("Longueur des côtés =", a, b, c)
print("Le périmètre est de ", d*2, "et l'aire est de ", e)

