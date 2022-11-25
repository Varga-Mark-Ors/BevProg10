def main():
    li=input('Oldalak:')
   # print(li)
    li1=li.split(sep=',')
  #  print(li1)
    c=0
    b=0
    for a in li1:
        if  '-' in a:
            c=a.split(sep='-')
            b1=int(c[0])
            b2=int(c[1])
            while b1<=b2:
                print(b1)
                b1=b1+1
        else: print(a)
if __name__=="__main__":
    main()