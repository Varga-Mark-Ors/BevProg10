def main():
    f=open("barmi.txt",'r')
    li=f.read()
    print(li)
    f.close()
   # f=open("barmi.txt","a")
  #  for i in range(0,10):
  #      print(i,file=f)
   # f.close()
if __name__=="__main__":
    main()