def main():

    f=open('feladat.txt','r')
    d1=f.readlines()
    for i in d1:
        d1[i]=d1[i]+2
    print(d1)

if __name__=="__main__":
    main()