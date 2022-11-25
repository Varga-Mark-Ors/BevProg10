def main():
    li=[2,4,8,3,9,7,1]
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
    print(li1)    
    ossz=0
    for i in li1:
        ossz=ossz+i
    print(ossz)
if __name__=="__main__":
    main()