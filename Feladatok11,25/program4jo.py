def main():
    a=2**1024
    l=str(a)
    li=list(l)
    i=0
    for i in range(len(li)):
        li[i]=int(li[i])
    i=0    
    li1=[]
    for i in range(len(li)-1):
        if li[i]>li[i+1]:
            a=li[i]
            b=li[i+1]
        else:
            a=li[i+1] 
            b=li[i]
        li1.append(a-b) 
        i=i+1        
    ossz=0
    for i in li1:
        ossz=ossz+i
    print(ossz)
if __name__=="__main__":
    main()