def debi(a,b):
    c=b%2
    while b>0:
        if c==1:
            a.append(1)
        else:
            a.append(0)
        b=b//2
        c=b%2
    return a

def main():
    x=[]
    Szam=int(input('Szam: '))
    y=debi(x,Szam)
    y.reverse()
    print(y)  
if __name__=="__main__":
    main()