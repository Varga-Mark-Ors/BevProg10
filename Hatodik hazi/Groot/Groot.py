import sys

def main():
    a=sys.argv[0]
    b=a.replace(".py","")
    print(b)
if __name__ == "__main__":
    main()