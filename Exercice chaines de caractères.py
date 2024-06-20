chaine="abcdefghijklmnopqrstuvwxyz" * 10
e = 1
while e <= len(chaine):
    print(chaine[:e])
    chaine =chaine[e:]
    e+=1