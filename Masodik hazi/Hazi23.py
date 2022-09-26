def main():

    Szam=int(input('Ertek='))
    s=Szam
    s1=0

    while s>0:
        s1=(s1*10)+s % 10
        s=s // 10

    if s1==Szam:
        print('Tukor')
    else:
        print('Nem tukor')
        
if __name__=="__main__":
    main()