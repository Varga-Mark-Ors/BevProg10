def main():
    c1 = """Totya is a hideous duck. His nose is enourmous , his wings look terribe and he
            doesn't have any feather on his head. Even that Totya is always immaculate since
            he spends most of his time in water. It doesn't matter if his bath is freezing or
            boiling he takes a shower every day!"""

    li = list(c1.split())
   # i=0
   # for word in li:
    #    if word in ("hideous","immaculate","freezing","boiling"):
    #        word=input("{0}=".format (word))
    di={
        'hideous':"very ugly",
        "enormous":"very big",
        "boiling":"hot",
        "freezing":"cold"
    }

    for word in li:
        if word in di:
            print(di[word],end=' ')
        else:
            print(word,end=' ')

if __name__ == '__main__':
    main()