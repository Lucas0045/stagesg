n = int(input("Quelle est le nombre de marches ? "))
h = int(input("Quelle est la hauteur des marches (en cm) ?"))
hauteurParcourue = (n*h*5*7*2/100)
print("Pour ", n, "marches de ", h,"cm, il parcourt ", hauteurParcourue, "m par semaine")