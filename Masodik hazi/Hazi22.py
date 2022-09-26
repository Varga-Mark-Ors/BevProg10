def main():

    N=int(input('Hanyadik tag legyen?'))
    f1=0
    f2=1
    i=1
    
    if N==1: print('A fibonacci szam erteke=',f1)
    elif N==2: print('A fibonacci szam erteke=',f2)
    else: 
       while i<N:
        f3=f2+f1
        f1=f2
        f2=f3
        i=i+1
    print('A fibonacci szam erteke=',f2)  

if __name__=="__main__":
    main()