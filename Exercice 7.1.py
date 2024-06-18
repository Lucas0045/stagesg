ch =input("Entrer une chaine de caractères")
i = 0
resul = ""
while i < len(ch):
    if ch[i-1] != ch[i]:
        resul = resul + ch[i]
    i = i + 1
print(resul)