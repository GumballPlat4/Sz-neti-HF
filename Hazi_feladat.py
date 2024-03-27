def beolvasas():
    lista=[]
    with open ("adatok.txt","r",encoding="UTF-8") as fm:
        for sor in fm:
            lista.append(int(sor.strip()))
    return lista