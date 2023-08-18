myobject=open("myfile.txt",'r')
print(myobject.readline(3))
print("*********data read from file 3 charc***************")
d=myobject.readlines()
print("data read from file ")
for line in d:
 words=line.split()
 print(words)
myobject.close()

