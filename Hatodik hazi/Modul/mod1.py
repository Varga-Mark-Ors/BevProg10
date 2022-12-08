import modult as m

def main():
    #b=99
    b=int(input("Meddig nezuk?="))
    i=2
    while i<=b:
        if m.is_prime(i)==True:
            print(i,"prim")
        i=i+1
if __name__ == "__main__":
    main()