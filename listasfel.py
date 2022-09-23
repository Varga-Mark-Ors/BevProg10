def main():
    m1="""A rút kiskacsa Hans Christian Andersen 1843-ban íródott, jól ismert meséje.
    A történet alapján több film és televíziós sorozat, illetve számtalan musical és 2009-ben balett verzió is készült. 
    A világ szinte összes nyelvére lefordították. """
    m2="""Az rúd kiskacsa Hans Christiano Anderson 3843-ban íródott, jól ismert meséyeet.
    A történet alapján többb filmek és televíziós sorozatok, illetve számtalan musicalok és 2909-ben balett verzió is készült. 
    Az világ szintes összesen nyelvére lefordították. """
    l1 = list(m1.split())
    l2 = list(m2.split())
    
    for word in l1:
        for wordok in l2:
            if word==wordok:  print(word,end=' ') 
if __name__=="__main__":
    main()