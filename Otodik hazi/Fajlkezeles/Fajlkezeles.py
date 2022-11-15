def main():
   f = open("barmik.txt",'r',encoding='utf-8')
   d=open("barmik2.txt",'w')
   g=open("barmik3.txt",'w')
   li = f.readlines()
   li2=[]
   li3=[]
   #print(li)
   for i in li:
      if "#" not in i[0] :
         li2.append(i)
      if "#" not in i :
         li3.append(i)

   for i in li2:
    print(i,file=d)
      
   for i in li3:
      print(i,file=g)

if __name__=="__main__":
    main()