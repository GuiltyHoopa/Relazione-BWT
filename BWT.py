x = input("inserisci parola ")
BMTX = x+"$"

for i in range(len(BMTX)):
    Rotation = BMTX[i:] + BMTX[:i]
    print (Rotation)
    
    

    
