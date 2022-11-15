def main():
    #f=open("barmi.txt", 'w')
    #print("How I want a drink alcoholic of course After the heavy lectures involving complex functions", file = f)
    f=open("barmi.txt", 'r')
    li=f.read()
    db=0
    for i in li:
        db=db+1
    db=db//10
    f.close()
    f=open('barmimas.txt','w')
    print(db,file=f)
if __name__ == "__main__":
    main()