import random

def main():
    a=random.randint(1,100)
    #print(a)
    min=1
    max=100
    kindex=(min+max)//2
    #print(kindex)
    while kindex!=a :
        if kindex>a :
            print("My number is smaller, than ", kindex)
            max=kindex
            kindex=(max+min)//2
        elif kindex<a :
            print("My number is bigger, than ",kindex)
            min=kindex
            kindex=(max+min)//2
    print("You guessed it,it was ",kindex)
if __name__=="__main__":
    main()