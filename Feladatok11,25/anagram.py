def main():
    s1=input(('Elso mondat='))
    s2=input(('Masodik mondat='))
    l1=list(s1.upper())
    l2=list(s2.upper())
    a1=[0]*26
    a2=[0]*26

    for i in l1:
        b=ord(i)-65
        if (b>=0) and (b<=26):
            a1[b]=a1[b]+1

    for i in l2:
        b=ord(i)-65
        if (b>=0) and (b<=26):
            a2[b]=a2[b]+1
    
    if a1==a2:
        print("Anagramja")
    else:
        print("Nem az anagramja") 
if __name__=="__main__":
    main()