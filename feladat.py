def sum(li):
    if len(li)==1:
        return li[0]
    return li[0]+sum(li[1:])

def main():

    print(sum([1,2,3,4,5]))

if __name__=="__main__":
    main()