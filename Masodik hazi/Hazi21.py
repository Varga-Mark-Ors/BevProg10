def korterulet(r):
    import math
    Kort=(r*r)*math.pi
    print('Kor terulete=',Kort)
    return Kort

def teglalap(a,b):
    Tegla=a*b
    print('Teglalap terulete=',Tegla)
    return Tegla

def Kupterf(KT,a):
    Kupt=(KT*a)/3
    return Kupt

def main():
    
    r=int(input('Sugar: '))
    a=int(input('Hossza:'))
    b=int(input('Szelessege:'))
    KT=korterulet(r)
    TT=teglalap(a,b)
    Kupter=Kupterf(KT,a)
    print('Kup terfogata=',Kupter)

if __name__=="__main__":
    main()