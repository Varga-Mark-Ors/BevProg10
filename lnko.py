def lnko(a,b):
    while not (a==b):
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def lnkorec(a,b):
    if a==b:
        return a
    elif a>b:
        return lnkorec(a-b,b)
    else:
        return lnkorec(a,b-a)

def main():

    print(lnkorec(18,4))

if __name__=="__main__":
    main()