travel = input("Quelle est la phrase ?")
L = []
L = travel.split('.')
travel.replace(".","")
L = travel.split(' ') 
i = 0
while i < len(L):
    if L[i]!=L[i-1]:
        print(L[i])
    i=i+1
L.sort()
print("Il y a ",len(L), "mots")