def Szoveg(a,s1,s2,i):
    w=''
    j=1
    for word in a:
        j=j+1
        if word==' ' or j==i:
            if s1==w:
                print(s2)
                print(s1)
            else:    
             print(w)
             w=""
        else:
            w=w+word


def main():

    Text=list(input('Szoveg:'))
    e=len(Text)+1
    Szo1=(input('Keresett szo:'))
    Szo2=(input('Eloszo:'))
    Szoveg(Text,Szo1,Szo2,e)
if __name__=="__main__":
    main()