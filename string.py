def main():
    txt='Hello, world!'
    tobbsoros="""tobb
    sorba
    van"""

    print(txt[5])
    for x in txt:
        print(x)
    
    print(txt.upper())
    print(txt.lower())
    print(txt.capitalize())
    print(txt.title())
    print("                     siuuuuuuuuuuuuuuuuuuuu             ".strip())
    print(txt.replace("ll","nl"))
    print(txt.split())
    print("1,2,3,4,5,6".split(";"))
    print("Hello, "+"World!")
    print(txt.rfind('o'))
    print(txt[0:5])
    print(len(txt))
    print("a".isalpha())
    print("a".join(txt))
if __name__=="__main__":
    main()