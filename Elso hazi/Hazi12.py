def main():
    print('Melyik opciot szeretne valasztani?[Kerem szepen azt a szamot adja meg] 1.Pitagorasz  2.Cosinus tetel  3.Sinus tetel')
    c=0
    option =int(input('Opcio: '))
    d=0
    Acos=0
    Bcos=0
    import math 
    if option==1:
        print('Kerem A es B oldalakat!')
        a=int(input('A: '))
        b=int(input('B: '))
        c=a**2+b**2
        d=math.sqrt(c)
        print('Megoldas={0}'.format(d))
    elif option==2:
         print('Kerem A es B oldalakat,meg cos A-t!')
         a=int(input('A: '))
         b=int(input('B: '))
         Acos=float(input('Acos: '))
         c=a**2+b**2-2*a*b*Acos
         d=math.sqrt(c)
         print('Megoldas={0}'.format(d))
    elif option==3:
        print('Kerem A es B oldalakat,meg sin A-t es sin B-t!')
        a=int(input('A: '))
        b=int(input('B: '))
        Acos=float(input('Acos: '))
        Bcos=float(input('Bcos: '))
        c=a//b
        d=Acos//Bcos
        if c==d:
            print('A sinus tetel igaz')
        else:
             print('A sinus tetel nem igaz')
    else:
        print('Nem jo opciot adott meg!')
if __name__=="__main__":
    main()