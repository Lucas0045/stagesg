c1 = int(input("Quelle est le premier chiffre ? "))
o = input("Quelle est l'opérateur ? ")
c2 = int(input("Quelle est le deuxième chiffre ? "))
if o=='+' :
    r = c1+c2
elif o=='-' :
    r = c1-c2
elif o=='*' :
    r = c1*c2
elif o=='//' :
    r = c1//c2
elif o=='**' :
    r = c1**c2
elif o=='/' :
    r = c1/c2
elif o=='%' :
    r = c1%c2
print("Le résultat est ", r)