def BWT(x):

    BWT = x+"$"
    Rotation = []
    for i in range(len(BWT)):
        Rotation.append(BWT[i:] + BWT[:i])
    
    for i in range(1, len(Rotation)):
        chiave = Rotation[i]
        j = i - 1

        while j >= 0 and Rotation[j] > chiave:
            Rotation[j + 1] = Rotation[j]
            j -= 1
        Rotation[j + 1] = chiave

    return Rotation






    

    
