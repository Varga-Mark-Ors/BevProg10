def main():
    for x in range(1,15,2):
        print(x)
    
    li=['repa','retek','karalabe']
    for word in li:
        print(word)

    i=0
    while i<10:
        print(i)
        i=i+1

    i=0
    while True:
        print(i,end='\n\n')
        if (i>8):
            break
        i+=1
if __name__=="__main__":
    main()